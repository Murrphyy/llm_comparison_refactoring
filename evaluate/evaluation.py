from enum import Enum

class EvaluationType(Enum):
    """Enumeration of different evaluation types."""
    
    CODE_EXECUTION = "code_execution"  # test cases to validate the functionality
    LOC = "line_of_code"  # number of loc
    CC = "cyclomatic_complexity" 

    