import os
import sys
from pathlib import Path

def create_test_files():
    """Create test files with various syntax errors"""
    
    # Test Case 1: Temporary file that should be deleted
    temp_content = '''defx temp_function():
    printx "This is a temporary function with syntax errors"
    returnx "temporary_value"

classx TempClass:
    defx __init__(self, name):
        self.name = name
        printx f"Created {self.name}"
        returnx None
    
    defx display(self):
        printx f"Name: {self.name}"
        returnx self.name

defx calculate_temp(a, b):
    resultx = a * b + 10
    printx f"Temp result: {resultx}"
    returnx resultx
