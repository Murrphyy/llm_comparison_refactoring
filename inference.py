import os
import re
import pandas as pd
import time
from model.llm import LLMHandler
from model.prompt_generator import PromptGenerator
from data_loader.data_loader import DataLoader
from data_loader.data import Data
from evaluate.evaluation import EvaluationType
from evaluate.evaluator import Evaluator


def extract_code_qwen(text):
    # Match Python code blocks inside ```python ... ```
    code_blocks = re.findall(r"```python(.*?)```", text, re.DOTALL)
    
    return "\n".join(block.strip() for block in code_blocks)

def extract_code(response):
    # Match triple backtick blocks (e.g., ```python\n...\n```)
    match = re.search(r"```(?:\w+)?\n(.*?)```", response, re.DOTALL)
    return match.group(1) if match else response  # Return entire response if no match

def parse_problem_data(filename):
    problem_data = {}
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        match = re.match(r"(\w+):\[(.*?)\]", line.strip())
        if match:
            problem_name = match.group(1)
            files = match.group(2).replace("'", "").split(', ')
            problem_data[problem_name] = files
    
    return problem_data

def generate_code(LLM, prompt_generator, data, attempt_count = None):
    message = prompt_generator.generate_prompt(data)
    #print(f"PROMPT = {message}\n")
    if message == None:
        print("Prompt Could not be Created!")
        return None
    
    model_response = LLM.generate_text(message)
    if (LLM.model_name.startswith("Qwen")) and prompt_generator.prompting_type != "few_shot" and attempt_count != 0:
        content = extract_code_qwen(model_response) # qwen has a problematic output which requires filtering            
    else:
        content = extract_code(model_response)
    return content

def save_analysis(df, filepath):
    df.to_csv(filepath)

def write_generated_to_file(generated_file_path,file_name,content):
    if not os.path.exists(generated_file_path):
        os.makedirs(generated_file_path)
    generated_file_path = os.path.join(generated_file_path, file_name)
    f = open(generated_file_path, "w")
    f.write(content)
    f.close() 

def save_rci_attempt(filepath,submission,attempt):     
    f = open(filepath, "a")
    f.write(f"{submission}:{attempt}\n")
    f.close() 

def main():    
    parent_folder = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(parent_folder, 'data/Python_wrapped')
    model_config_path = os.path.join(parent_folder, 'model.yaml')
    prompt_config_path = os.path.join(parent_folder, 'prompts.yaml')
    problems_all = parse_problem_data("data/selected_files.txt")
    

    # Define the column names for analysis csv
    columns = ["problem_id", "sub_id", "wrapped_test", "wrapped sum_cc", "wrapped max_cc", "wrapped cc_rank", "wrapped avg loc", "generated_test", "generated sum_cc", "generated max_cc", "generated cc_rank","generated avg loc","renamed_test"]

    # Create an empty DataFrame with the specified columns
    df_submissions = pd.DataFrame(columns=columns)

    LLM = LLMHandler(model_config_path)

    data_loader = DataLoader()
    evaluator = Evaluator()    
    # Calculate the start time
    start = time.time()

    for problem, files in problems_all.items():
        description_folder = "data/Problem_descriptions"
        description_folder = os.path.join(parent_folder, description_folder)
        description_path = os.path.join(description_folder, problem+".html")
        

        sample_folder_path = os.path.join(folder_path, problem)
        count = 0
        sum_cc_list = []
        max_cc_list = []
        rank_cc_list = []
        problem_id = problem

        if os.path.exists(sample_folder_path):
            problem_implementations = files
            print(f"Imps : {len(problem_implementations)}")
            for imp in problem_implementations:
                prompt_generator_em = PromptGenerator(config_path = prompt_config_path, mode = "extract_method")
                prompt_generator_rm = PromptGenerator(config_path = prompt_config_path, mode = "rename_method")
                attempt_count = 2 # number of additional attempts for rci prompt, otherwise neglect it.

                new_row = []
                new_row.append(problem)
                new_row.append(imp)
                
                file_name = imp
                    
                file_path = os.path.join(sample_folder_path, file_name)
                count += 1
                print(f"Processing file : {problem} - {imp} - {file_path}")
                # Check if the file exists
                if os.path.exists(file_path):                    
                    try:
                        data = data_loader.load_data(content_file = file_path, statements_file = description_path, test_cases_file = description_path)
                        test_passed, test_message, expected_outcome = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.CODE_EXECUTION)
                        
                        if test_passed:
                            print("PASS WRAPPED")
                            new_row.append("True")
                            
                            sum_cc, max_cc, max_rank = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.CC)
                            avg_loc = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.LOC)
                            
                            new_row.append(sum_cc)
                            new_row.append(max_cc)
                            new_row.append(max_rank)
                            new_row.append(avg_loc)

                            content = generate_code(LLM, prompt_generator_em, data)
                            
                            if content == None:
                                print("Generated None")
                                continue

                            output_path = LLM.model_name +"-"+ prompt_generator_em.prompting_type+"-em"
                            generated_file_path = os.path.join(sample_folder_path, output_path)
                            write_generated_to_file(generated_file_path, file_name, content)
                            generated_file_path = os.path.join(generated_file_path, file_name)

                            data = data_loader.load_data(content_file = generated_file_path, statements_file = description_path, test_cases_file = description_path)
                            test_passed, test_message, expected_outcome = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.CODE_EXECUTION)
                            data.set_test_result(outcome = test_message, expected = expected_outcome)

                            while ("rci" in prompt_generator_em.prompting_type) and (test_passed != True) and (attempt_count > 0):                                
                                print(f"ATTEMPT {attempt_count}")
                                attempt_count -= 1
                                content = generate_code(LLM, prompt_generator_em, data, attempt_count)
                                
                                if content == None:
                                    print("Generated None")
                                    continue

                                output_path = LLM.model_name +"-"+ prompt_generator_em.prompting_type+"-em"
                                generated_file_path = os.path.join(sample_folder_path, output_path)
                                write_generated_to_file(generated_file_path, file_name,content)
                                generated_file_path = os.path.join(generated_file_path, file_name)
                                
                                data = data_loader.load_data(content_file = generated_file_path, statements_file = description_path, test_cases_file = description_path)
                                test_passed, test_message, expected_outcome = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.CODE_EXECUTION)
                                data.set_test_result(outcome = test_message, expected = expected_outcome)
                            
                            output_path = LLM.model_name +"-"+ prompt_generator_em.prompting_type
                            output_path = os.path.join(parent_folder, output_path)
                            if not os.path.exists(output_path):
                                os.makedirs(output_path)
                            output_path = os.path.join(output_path, "attempts.txt")
                            save_rci_attempt(output_path, imp, attempt_count)

                            if test_passed:
                                print("PASS EXTRACT")
                                new_row.append("True")
                                sum_cc, max_cc, max_rank = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.CC)
                                avg_loc = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.LOC)
                                
                                new_row.append(sum_cc)
                                new_row.append(max_cc)
                                new_row.append(max_rank)
                                new_row.append(avg_loc)

                                content = generate_code(LLM, prompt_generator_rm, data)
                                
                                if content == None:
                                    print("Generated None")
                                    continue

                                output_path = LLM.model_name +"-"+ prompt_generator_em.prompting_type+"-rm"
                                generated_file_path = os.path.join(sample_folder_path, output_path)
                                write_generated_to_file(generated_file_path, file_name, content)
                                generated_file_path = os.path.join(generated_file_path, file_name)
                                
                                data = data_loader.load_data(content_file = generated_file_path, statements_file = description_path, test_cases_file = description_path)
                                test_passed, test_message, expected_outcome = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.CODE_EXECUTION)

                                attempt_count = 2
                                while ("rci" in prompt_generator_rm.prompting_type) and (test_passed != True) and (attempt_count > 0):                                
                                    print(f"ATTEMPT {attempt_count}")
                                    attempt_count -= 1

                                    content = generate_code(LLM, prompt_generator_rm, data, attempt_count)
                                
                                    if content == None:
                                        print("Generated None")
                                        continue

                                    output_path = LLM.model_name +"-"+ prompt_generator_em.prompting_type+"-rm"
                                    generated_file_path = os.path.join(sample_folder_path, output_path)
                                    write_generated_to_file(generated_file_path, file_name, content)
                                    generated_file_path = os.path.join(generated_file_path, file_name)
                                    
                                    data = data_loader.load_data(content_file = generated_file_path, statements_file = description_path, test_cases_file = description_path)
                                    test_passed, test_message, expected_outcome = evaluator.evaluate(input_data = data, evaluation_type = EvaluationType.CODE_EXECUTION)
                                    data.set_test_result(outcome = test_message, expected = expected_outcome)

                                if test_passed:
                                    print("PASS RENAME")
                                    new_row.append("True")
                                else:
                                    print("FAIL RENAME")
                                    new_row.append("False") 
                            else:
                                print("FAIL EXTRACT")
                                print(test_message)
                                new_row.append("False")
                                new_row.append(None)
                                new_row.append(None)
                                new_row.append(None)
                                new_row.append(None)
                                new_row.append(None)                                       
                        else:
                            print("FAIL WRAPPED")
                            new_row.append("False")
                            new_row.append(None)
                            new_row.append(None)
                            new_row.append(None)
                            new_row.append(None)
                            new_row.append(None)
                            new_row.append(None)
                            new_row.append(None)
                            new_row.append(None)
                            new_row.append(None)
                            new_row.append(None)
                            
                        df_submissions.loc[len(df_submissions)] = new_row
                        print(f"{count}/{len(problem_implementations)}")
                    except Exception as e:
                        print(f"Error : {e}")
                else:
                    print(f"File {file_name} not found in {sample_folder_path}")
                
                
        output_path = LLM.model_name +"-"+ prompt_generator_em.prompting_type
        output_path = os.path.join(parent_folder, output_path)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        output_path = os.path.join(output_path, "analysis.csv")
        save_analysis(df_submissions, output_path)
        

    # Calculate the end time and time taken
    end = time.time()
    length = end - start

    # Show the results : this can be altered however you like
    print("It took", length, "seconds!")

main()