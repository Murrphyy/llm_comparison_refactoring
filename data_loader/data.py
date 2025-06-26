class Data:
    """A class to store and retrieve content, statements, and test cases."""
    
    def __init__(self, content="", statements=None, test_cases=None, path = None):
        self.content = content
        self.statements = statements
        self.test_cases = test_cases
        self.path = path
        self.outcome = None
        self.expected = None

    def get_content(self):
        """Returns the stored content."""
        return self.content

    def set_content(self, code):
        self.content = code

    def get_statements(self):
        """Returns the stored statements."""
        return self.statements

    def get_test_cases(self):
        """Returns the stored test cases."""
        return self.test_cases

    def get_path(self):
        """Returns the stored content file path."""
        return self.path

    def set_test_result(self, outcome, expected):
        self.outcome = outcome
        self.expected = expected
    
    def get_test_results(self):
        return self.outcome, self.expected