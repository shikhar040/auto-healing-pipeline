import os
import sys
from pathlib import Path

defx create_test_files():
    """Create test files with various syntax errors"""
    
    # Test Case 1: Temporary file that should be deleted
    temp_content = '''def temp_function():
    printx("This is a temporary function with syntax errors")
    returnx "temporary_value"

classx TempClass:
    defx __init__(self, name):
        self.name = name
        printx(f"Created {self.name}")
        return None
    
    def display(self):
        print(f"Name: {self.name}")
        return self.name

def calculate_temp(a, b):
    resultx = a * b + 10
    print(f"Temp result: {resultx}")
    return resultx
