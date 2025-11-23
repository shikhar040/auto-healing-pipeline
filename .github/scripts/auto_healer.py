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
            (r'defx\s+(\w+)\s*\(', r'def \1('),
            (r'function\s+(\w+)\s*\(', r'def \1('),
            
            # Print statements
            (r'printx\s*\(', 'print('),
            (r'print\s+(".*?"|\'.*?\')', r'print(\1)'),
            (r'print\s+(\w+)', r'print(\1)'),
            
            # Return statements
            (r'returnx\s+', 'return '),
            
            # Missing colons
            (r'(def|class|if|elif|else|for|while|with|try|except)\s*\(.*\)\s*\n\s*', r'\1:\n    '),
            
            # Class definitions
            (r'class\s+(\w+)\s*\(', r'class \1('),
        ]
    
    def heal_file(self, file_path):
        """Apply fixes to a single Python file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            healed_content = original_content
            for pattern, replacement in self.common_fixes:
                healed_content = re.sub(pattern, replacement, healed_content)
            
            if healed_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(healed_content)
                self.fixes_applied += 1
                print(f"✅ Healed: {file_path}")
                return True
                
        except Exception as e:
            print(f"❌ Error healing {file_path}: {e}")
            return False
    
    def heal_directory(self, directory='.'):
        """Heal all Python files in directory"""
        python_files = list(Path(directory).rglob('*.py'))
        print(f"🔍 Found {len(python_files)} Python files")
        
        for py_file in python_files:
            self.heal_file(str(py_file))
        
        print(f"🎯 Applied {self.fixes_applied} fixes across {len(python_files)} files")
        return self.fixes_applied

if __name__ == '__main__':
    healer = PythonAutoHealer()
    fixes = healer.heal_directory()
    sys.exit(0 if fixes >= 0 else 1)
