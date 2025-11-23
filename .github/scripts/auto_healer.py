#!/usr/bin/env python3
"""
Super Python Auto-Healer
Fixes common Python syntax errors automatically
"""

import os
import re
import sys
from pathlib import Path

class PythonAutoHealer:
    def __init__(self):
        self.fixes_applied = 0
        self.common_fixes = [
            # Function definitions
            (r'defx\s+', 'def '),
            
            # Print statements - multiple patterns
            (r'printx\s*\(', 'print('),  # print(with parentheses
            (r'printx\s+', 'print('),    # print(without parentheses
            (r'print\s+(".*?"|\'.*?\')', r'print(\1)'),  # print(without) parentheses
            (r'print\s+(\w+)', r'print(\1)'),  # print(variable) without parentheses
            
            # Return statements
            (r'returnx\s+', 'return '),
            
            # Class definitions
            (r'classx\s+', 'class '),
        ]
    
    def heal_file(self, file_path):
        """Apply fixes to a single Python file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            healed_content = original_content
            for pattern, replacement in self.common_fixes:
                healed_content = re.sub(pattern, replacement, healed_content)
            
            # Add missing closing parentheses for print(statements)
            lines = healed_content.split('\n')
            fixed_lines = []
            for line in lines:
                if 'print(' in line and not line.rstrip().endswith(')') and '#' not in line:
                    # Count quotes to see if we have a complete string
                    if line.count('"') % 2 == 0 and line.count("'") % 2 == 0:
                        line += ')'
                fixed_lines.append(line)
            
            healed_content = '\n'.join(fixed_lines)
            
            if healed_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(healed_content)
                self.fixes_applied += 1
                print(f"✅ Healed: {file_path}")
                return True
                
        except Exception as e:
            print(f"❌ Error healing {file_path}: {e}")
            return False
    
    def cleanup_test_files(self, directory='.'):
        """Remove test files created during testing"""
        test_patterns = [
            '*test*.py',
            '*broken*.py', 
            'temp_*.py',
            'test_*.py'
        ]
        
        files_removed = 0
        for pattern in test_patterns:
            for test_file in Path(directory).rglob(pattern):
                if test_file.name != 'test_basic.py':  # Keep your actual test file
                    try:
                        test_file.unlink()
                        print(f"🗑️ Removed: {test_file}")
                        files_removed += 1
                    except Exception as e:
                        print(f"❌ Error removing {test_file}: {e}")
        
        return files_removed
    
    def heal_directory(self, directory='.'):
        """Heal all Python files in directory"""
        python_files = list(Path(directory).rglob('*.py'))
        print(f"🔍 Found {len(python_files)} Python files")
        
        for py_file in python_files:
            self.heal_file(str(py_file))
        
        print(f"🎯 Applied {self.fixes_applied} fixes across {len(python_files)} files")
        
        # Optional: Cleanup test files
        cleanup = input("Do you want to cleanup test files? (y/n): ").lower().strip()
        if cleanup == 'y':
            removed = self.cleanup_test_files(directory)
            print(f"🗑️ Removed {removed} test files")
        
        return self.fixes_applied

if __name__ == '__main__':
    healer = PythonAutoHealer()
    fixes = healer.heal_directory()
    sys.exit(0 if fixes >= 0 else 1)
