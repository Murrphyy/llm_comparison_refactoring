from data_loader.data import Data
from bs4 import BeautifulSoup

class DataLoader:

    def _load_code(self, filename):
        """Reads a file and returns its content as a string."""
        try:
            with open(filename, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
            return None

    def _load_statements(self, filename):
        """Reads an HTML file and returns statements"""
        try:
            with open(filename, 'r') as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')

            problem_statement_section = soup.find('h3', string='Problem Statement').find_next('p')
            problem_statement = ''

            while problem_statement_section:
                problem_statement += problem_statement_section.get_text(separator=' ') + '\n'
                problem_statement_section = problem_statement_section.find_next_sibling('p')
            
            return problem_statement.strip()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
            return None

    def _load_test_cases(self, filename):
        """Reads an HTML file and returns the test cases"""
        try:
            with open(filename, 'r') as file:
                html_content = file.read()

            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find all sample input and output sections
            inputs = soup.find_all(string=lambda text: "Sample Input" in text)
            outputs = soup.find_all(string=lambda text: "Sample Output" in text)

            # Extract the text directly following the input/output labels
            sample_inputs = [inp.find_next('pre').get_text(strip=True) for inp in inputs]
            sample_outputs = [out.find_next('pre').get_text(strip=True) for out in outputs]

            # Combine inputs and outputs into pairs
            samples = list(zip(sample_inputs, sample_outputs))
            return samples
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: File '{filename}' is not a valid JSON.")
            return None
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
            return None

    def load_data(self, content_file, statements_file, test_cases_file):
        """Loads content, statements, and test cases from files and creates a Data instance."""
        content = self._load_code(content_file)
        statements = self._load_statements(statements_file)
        test_cases = self._load_test_cases(test_cases_file)

        if statements == None or test_cases == None or content == None:
            return None

        data_instance = Data(content, statements, test_cases, content_file)
        return data_instance
