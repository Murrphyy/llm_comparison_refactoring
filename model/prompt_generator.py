import yaml
import os

class PromptGenerator:
    def __init__(self, config_path: str, mode: str):
        """
        Initializes the PromptGenerator by loading the YAML configuration.
        
        :param config_path: Path to the YAML configuration file.
        :param mode: extract_method or rename_method.
        """
        self.config = self.load_config(config_path)
        self.prompting_type = self.config.get("prompting_type", "zero_shot")  # Default to zero-shot
        self.rci_structure = self.config.get("rci", {})
        self.mode = mode
        if self.mode == "extract_method":
            self.generic_prompts = self.config.get("generic_prompts_extract_method", [])
            self.few_shot_examples = self.config.get("few_shot_examples_extract_method", [])
        elif self.mode == "rename_method":
            self.generic_prompts = self.config.get("generic_prompts_rename_method", [])
            self.few_shot_examples = self.config.get("few_shot_examples_rename_method", [])
        self.reset_generator()

    def reset_generator(self):
        self.initial_prompt = True
        self.message = []

    def load_config(self, config_path: str) -> dict:
        """Loads the YAML configuration file."""
        with open(config_path, "r") as file:
            return yaml.safe_load(file)

    def generate_prompt(self, data):
        if self.initial_prompt:
            self.initial_prompt = False
            if self.mode == "extract_method":
                if self.prompting_type == "few_shot":
                    return self.few_shot_prompt_em(data.get_content())
                elif (self.prompting_type == "zero_shot") or (self.prompting_type == "rci"):
                    return self.zero_shot_prompt_em(data.get_content())
                else:
                    print("WRONG PROMPT TYPE. CHECK prompts.yaml!")
                    return None
            elif self.mode == "rename_method":
                if self.prompting_type == "few_shot":
                    return self.few_shot_prompt_rm(data.get_content(), data.get_statements())
                elif (self.prompting_type == "zero_shot") or (self.prompting_type == "rci"):
                    return self.zero_shot_prompt_rm(data.get_content(), data.get_statements())
                else:
                    print("WRONG PROMPT TYPE. CHECK prompts.yaml!")
                    return None
            else:
                print("WRONG PROMPT GENERATOR MODE! OPTIONS : extract_method, rename_method") 
                return None            
        elif self.prompting_type == "rci":
            return self.rci_prompt(data)
        else:
            print("WRONG PROMPT TYPE. CHECK prompts.yaml!") 
            return None
        

    def zero_shot_prompt_em(self, user_input):
        """Returns the user input as a zero-shot prompt."""
        system_msg = self.generic_prompts.get("system")
        user_msg_part_one = self.generic_prompts.get("part1")
        user_msg_part_two = self.generic_prompts.get("part2")
        self.message = [
            { "role": "system", "content": system_msg },
            { "role": "user", "content": user_msg_part_one+"\n"+user_input +"\n "+user_msg_part_two }
        ]

        return self.message
    
    def zero_shot_prompt_rm(self, user_input, problem_definition):
        """Returns the user input as a zero-shot prompt."""
        system_msg = self.generic_prompts.get("system")
        user_msg_part_one = self.generic_prompts.get("part1")
        user_msg_part_two = self.generic_prompts.get("part2")
        self.message = [
            { "role": "system", "content": system_msg },
            { "role": "user", "content": user_msg_part_one+ "\n"+problem_definition +"\n "+user_msg_part_two+"\n"+user_input }
        ]

        return self.message

    def few_shot_prompt_em(self, user_input):
        """Constructs a few-shot prompt using examples from the YAML file."""
        system_msg = self.generic_prompts.get("system")
        user_msg_part_one = self.generic_prompts.get("part1")
        user_msg_part_two = self.generic_prompts.get("part2")

        self.message = [{ "role": "system", "content": system_msg }]

        for ex in self.few_shot_examples:
            self.message.append({ "role": "user", "content": user_msg_part_one+"\n"+ex['input'] +"\n "+user_msg_part_two })
            self.message.append({ "role": "assistant", "content": ex['output'] })

        self.message.append({ "role": "user", "content": user_msg_part_one+"\n"+user_input +"\n "+user_msg_part_two })
        
        return self.message
    
    def few_shot_prompt_rm(self, user_input, problem_definition):
        """Constructs a few-shot prompt for rename refactoring using examples from the YAML file."""
        system_msg = self.generic_prompts.get("system")
        user_msg_part_one = self.generic_prompts.get("part1")
        user_msg_part_two = self.generic_prompts.get("part2")

        self.message = [{ "role": "system", "content": system_msg }]

        for ex in self.few_shot_examples:
            self.message.append({ "role": "user", "content": user_msg_part_one+ "\n"+ex["problem_definition"] +"\n "+user_msg_part_two+"\n"+ex["input"] })
            self.message.append({ "role": "assistant", "content": ex['output'] })

        self.message.append({ "role": "user", "content": user_msg_part_one+ "\n"+problem_definition +"\n "+user_msg_part_two+"\n"+user_input })
        
        return self.message

    def rci_prompt(self, data):
        """Constructs an RCI (Role, Context, Instruction) prompt."""
        print("RCI ENTERED")
        code = data.get_content()
        output, expected = data.get_test_results()
        output = str(output)
        expected = str(expected)

        user_msg_rci_part_one = self.rci_structure.get("part1")
        user_msg_rci_part_two = self.rci_structure.get("part2")
        user_msg_rci_part_three = self.rci_structure.get("part3")

        self.message.append({ "role": "assistant", "content": code})
        self.message.append({ "role": "user", "content": user_msg_rci_part_one+" '"+expected+"' "+ user_msg_rci_part_two+" '"+output+"'. "+user_msg_rci_part_three })

        return self.message

# Example usage
if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    prompt_gen = PromptGenerator(dir_path+"/../prompts.yaml", mode="rename_method")
    print(prompt_gen.generate_prompt("CODE", "DEFINITION"))

    #if using rci
    print(prompt_gen.generate_prompt(("CODE_2","OUTPUT","EXPECTED")))