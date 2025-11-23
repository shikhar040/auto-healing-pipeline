#!/usr/bin/env python3
"""
Enhanced Super Python Auto-Healer
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
            # Original fixes
            (r'defx\s+', 'def '),
            (r'printx\s*\(', 'print('),
            (r'printx\s+', 'print('),
            (r'returnx\s+', 'return '),
            (r'classx\s+', 'class '),
            
            # NEW FIXES for complex errors:
            
            # 1. Missing colons after function/class/if/except
            (r'(def\s+\w+\(.*\))\s*$', r'\1:'),  # Function missing colon
            (r'(class\s+\w+)\s*$', r'\1:'),       # Class missing colon
            (r'(if|elif|else|for|while|with|try|except|finally)\s*$', r'\1:'),  # Control flow missing colon
            
            # 2. Fix assignment in conditions
            (r'if\s+(\w+)\s*=\s*(\w+):', r'if \1 == \2:'),  # = instead of ==
            
            # 3. Fix variable names starting with numbers
            (r'\b(\d+[a-zA-Z_]\w*)\b', r'var_\1'),  # 2var -> var_2var
            
            # 4. Fix hyphens in variable names
            (r'\b([a-zA-Z_]\w*)-([a-zA-Z_]\w*)\b', r'\1_\2'),  # my-var -> my_var
            
            # 5. Fix missing commas in parameters
            (r'def\s+(\w+)\((\w+)\s+(\w+)\):', r'def \1(\2, \3):'),  # (name age) -> (name, age)
            (r'(\w+\)\s*"\s*(\d+)\)', r'\1", \2)'),  # ("Alice" 25) -> ("Alice", 25)
            
            # 6. Fix double commas in lists
            (r',\s*,', r','),  # [1, 2,, 3] -> [1, 2, 3]
            
            # 7. Add missing quotes for dictionary keys
            (r'\{(\w+):', r'{"\1":'),  # {key: -> {"key":
            (r',\s*(\w+):', r', "\1":'),  # , key: -> , "key":
            
            # 8. Fix missing closing parentheses in function definitions
            (r'def\s+\w+\([^)]*$', lambda x: x.group() + ')'),  # def func(a -> def func(a)
            
            # 9. Fix print without parentheses for strings
            (r'print\s+(".*?"|\'.*?\')', r'print(\1)'),
            (r'print\s+(\w+)', r'print(\1)'),
        ]
    
    def heal_file(self, file_path):
        """Apply fixes to a single Python file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            healed_content = original_content
            
            # Apply regex fixes
            for pattern, replacement in self.common_fixes:
                healed_content = re.sub(pattern, replacement, healed_content)
            
            # Advanced fixes that need line-by-line processing
            healed_content = self.fix_advanced_errors(healed_content)
            
            if healed_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(healed_content)
                self.fixes_applied += 1
                print(f"✅ Healed: {file_path}")
                return True
                
        except Exception as e:
            print(f"❌ Error healing {file_path}: {e}")
            return False
    
    def fix_advanced_errors(self, content):
        """Fix more complex syntax errors"""
        lines = content.split('\n')
        fixed_lines = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Fix missing closing quotes
            if line.count('"') % 2 != 0 and "'''" not in line and '"""' not in line:
                line += '"'
            
            # Fix missing closing brackets/parentheses
            if line.count('(') > line.count(')'):
                line += ')'
            if line.count('[') > line.count(']'):
                line += ']'
            if line.count('{') > line.count('}'):
                line += '}'
            
            # Fix inconsistent indentation (basic)
            if '    ' in line and '  ' in line:  # Mixed tabs and spaces
                line = line.replace('  ', '    ')  # Convert to 4 spaces
            
            fixed_lines.append(line)
            i += 1
        
        return '\n'.join(fixed_lines)
    
    def cleanup_test_files(self, directory='.'):
        """Remove test files created during testing"""
        test_patterns = [
            '*test*.py',
            '*broken*.py', 
            'temp_*.py',
            'test_*.py',
            '*example*.py',
            '*error*.py'
        ]
        
        # Files to NEVER remove (your important application files)
        protected_files = [
            'test_basic.py', 'conftest.py', '__init__.py',
            'app.py', 'main_app.py', 'settings.py', 'helpers.py'
        ]
        
        # Directories to NEVER touch
        protected_dirs = ['src', 'config', 'utils', 'tests']
        
        files_removed = 0
        for pattern in test_patterns:
            for test_file in Path(directory).rglob(pattern):
                # Skip protected directories
                if any(protected_dir in test_file.parts for protected_dir in protected_dirs):
                    continue
                    
                # Skip protected files
                if test_file.name not in protected_files:
                    try:
                        test_file.unlink()
                        print(f"🗑️ Removed: {test_file}")
                        files_removed += 1
                    except Exception as e:
                        print(f"❌ Error removing {test_file}: {e}")
        
        return files_removed
    
    def heal_directory(self, directory='.', auto_cleanup=False):
        """Heal all Python files in directory"""
        python_files = list(Path(directory).rglob('*.py'))
        print(f"🔍 Found {len(python_files)} Python files")
        
        for py_file in python_files:
            self.heal_file(str(py_file))
        
        print(f"🎯 Applied {self.fixes_applied} fixes across {len(python_files)} files")
        
        # Cleanup logic
        if auto_cleanup:
            removed = self.cleanup_test_files(directory)
            print(f"🗑️ Auto-removed {removed} test files")
        else:
            try:
                cleanup = input("Do you want to cleanup test files? (y/n): ").lower().strip()
                if cleanup == 'y':
                    removed = self.cleanup_test_files(directory)
                    print(f"🗑️ Removed {removed} test files")
            except EOFError:
                print("ℹ️  Running in CI environment - skipping interactive cleanup")
        
        return self.fixes_applied

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Python Auto-Healer')
    parser.add_argument('--auto-cleanup', action='store_true', 
                       help='Automatically cleanup test files without prompt')
    
    args = parser.parse_args()
    
    healer = PythonAutoHealer()
    fixes = healer.heal_directory(auto_cleanup=args.auto_cleanup)
    sys.exit(0 if fixes >= 0 else 1)
