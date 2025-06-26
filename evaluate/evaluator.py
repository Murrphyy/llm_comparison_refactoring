import ast
import time
import subprocess
from evaluate.evaluation import EvaluationType
import sys
from radon.complexity import cc_visit, cc_rank
from radon.raw import analyze

class Evaluator:

    def evaluate(self, input_data, evaluation_type):
        """
        Evaluates the input data based on the selected evaluation method.

        :param input_data: The data to be evaluated.
        :return: Evaluation result.
        """
        if evaluation_type == EvaluationType.CODE_EXECUTION:
            return self._test_code(input_data)
        elif evaluation_type == EvaluationType.CC:
            return self._analyze_cyclomatic_complexity(input_data)
        elif evaluation_type == EvaluationType.LOC:
            return self._calculate_avg_loc_per_method(input_data)
        else:
            print("Unknown evaluation type.") 
            return None

    def _test_code(self,data):
        test_cases = data.get_test_cases()
        for sample_input, expected_output in test_cases:
            # Run the Python file as a subprocess
            try:
                process = subprocess.run(
                    [sys.executable, data.get_path()],  # Run the Python interpreter with the file
                    input=sample_input,          # Provide the sample input
                    text=True,                   # Treat input/output as text
                    capture_output=True,         # Capture the output
                    timeout=10                    # Set a timeout for safety
                )

                # Get the output and compare with the expected output
                actual_output = process.stdout.strip()

                if actual_output != expected_output:
                    return False, actual_output, expected_output

            except subprocess.TimeoutExpired:
                return False, "Timeout error! It did not finish in time.", expected_output
            except Exception as e:
                return False, "TRY CATCH ERROR IN EVALUATOR : "+str(e), expected_output

        return True, None, None

    def _analyze_cyclomatic_complexity(self,data):
        # Compute cyclomatic complexity using radon
        code = data.get_content()
        results = cc_visit(code)
        if not results:
            return None,None,None

        sum_cc = 0
        max_cc = 0
        max_rank = 'A'
        for item in results:
            sum_cc += item.complexity
            if(max_cc < item.complexity):
                max_cc = item.complexity
            if(max_rank < cc_rank(item.complexity)):
                max_rank = cc_rank(item.complexity)
            
        return sum_cc, max_cc, max_rank

    def _calculate_avg_loc_per_method(self,data):
        code = data.get_content()
        tree = ast.parse(code)
        
        method_locs = []

        # Traverse the AST to find function definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Calculate lines of code for the method
                start_line = node.lineno
                end_line = max(child.lineno for child in ast.walk(node) if hasattr(child, 'lineno'))
                loc = end_line - start_line + 1
                method_locs.append(loc)

        # Calculate average LOC per method
        if method_locs:
            avg_loc = sum(method_locs) / len(method_locs)
            return avg_loc
        return None

