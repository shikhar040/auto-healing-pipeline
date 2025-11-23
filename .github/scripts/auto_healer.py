<<<<<<< HEAD
#!/usr/bin/env python3
"""
Enhanced Super Python Auto_Healer
Fixes common Python syntax errors automatically
"""
=======
name: Super Python Auto-Healer
>>>>>>> 83539739e9a55b8855fdec163e7b87b9d025b068

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  schedule:
    - cron: '0 6 * * *'  # Run daily at 6 AM UTC

<<<<<<< HEAD
class PythonAutoHealer:
    def __init__(self):
        self.fixes_applied = 0
        self.common_fixes = [
            # Basic fixes
            (r"defx\s+", "def "),
            (r"printx\s*\(", "print("),
            (r"printx\s+", "print("),
            (r"returnx\s+", "return "),
            (r"classx\s+", "class "),
            # Enhanced fixes
            (r"(def\s+\w+\(.*\))\s*$", r"\1:"),
            (r"(class\s+\w+)\s*$", r"\1:"),
            (r"(if|elif|else|for|while|with|try|except|finally)\s*$", r"\1:"),
            (r"if\s+(\w+)\s*=\s*(\w+):", r"if \1 == \2:"),
            (r"\b(\d+[a-zA-Z_]\w*)\b", r"var_\1"),
            (r"\b([a-zA-Z_]\w*)-([a-zA-Z_]\w*)\b", r"\1_\2"),
            (r"def\s+(\w+)\((\w+)\s+(\w+)\):", r"def \1(\2, \3):"),
            (r"(\w+\"\s*)(\d+)\)", r'\1, \2)'),  # Fixed escape sequence
            (r",\s*,", r","),
            (r"\{(\w+):", r'{"\1":'),
            (r",\s*(\w+):", r', "\1":'),
            (r'print\s+(".*?"|\'.*?\')', r"print(\1)"),
            (r"print\s+(\w+)", r"print(\1)"),
        ]

    def heal_file(self, file_path):
        """Apply fixes to a single Python file"""
        try:
            # Skip if it's this file to avoid self-modification loops
            if "auto_healer.py" in file_path:
                print(f"🔒 Skipping self: {file_path}")
                return False
                
            with open(file_path, "r", encoding="utf-8") as f:
                original_content = f.read()
            
            healed_content = original_content
            
            for pattern, replacement in self.common_fixes:
                healed_content = re.sub(pattern, replacement, healed_content)
            
            healed_content = self.fix_advanced_errors(healed_content)
            
            if healed_content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(healed_content)
                self.fixes_applied += 1
                print(f"✅ Healed: {file_path}")
                return True
            else:
                print(f"✅ No issues: {file_path}")
                return False
                
        except Exception as e:
            print(f"❌ Error healing {file_path}: {e}")
            return False

    def fix_advanced_errors(self, content):
        """Fix more complex syntax errors"""
        lines = content.split("\n")
        fixed_lines = []
        
        for i, line in enumerate(lines):
            fixed_line = line
            
            # Fix missing colons for control structures
            if re.match(r'^\s*(def|class|if|elif|for|while|with|try|except|finally)\s+.*', fixed_line) and not fixed_line.rstrip().endswith(':') and not fixed_line.strip().endswith('('):
                if not any(keyword in fixed_line for keyword in ['import', 'from', 'return']):
                    fixed_line = fixed_line.rstrip() + ':'
            
            # Fix unmatched quotes (simple cases)
            if fixed_line.count('"') % 2 != 0 and "'" not in fixed_line:
                fixed_line += '"'
            elif fixed_line.count("'") % 2 != 0 and '"' not in fixed_line:
                fixed_line += "'"
            
            # Fix unmatched parentheses
            open_paren = fixed_line.count("(")
            close_paren = fixed_line.count(")")
            if open_paren > close_paren:
                fixed_line += ")" * (open_paren - close_paren)
            
            # Fix unmatched brackets
            open_bracket = fixed_line.count("[")
            close_bracket = fixed_line.count("]")
            if open_bracket > close_bracket:
                fixed_line += "]" * (open_bracket - close_bracket)
            
            # Fix unmatched braces
            open_brace = fixed_line.count("{")
            close_brace = fixed_line.count("}")
            if open_brace > close_brace:
                fixed_line += "}" * (open_brace - close_brace)
            
            fixed_lines.append(fixed_line)
        
        return "\n".join(fixed_lines)

    def create_test_files_for_demo(self):
        """Create some test files with common errors to demonstrate healing"""
        test_files = {
            "test_broken.py": '''
def broken_function
    printx "hello world"
    returnx 42

class TestClass
    def method(self)
        print("test"

if x = 5
    print("x is 5")
''',
            "temp_example.py": '''
printx "temporary file"
returnx "test"
'''
        }
        
        for filename, content in test_files.items():
            with open(filename, "w") as f:
                f.write(content)
            print(f"📝 Created test file: {filename}")

    def cleanup_test_files(self, directory="."):
        """Remove temporary test files but keep important ones"""
        test_patterns = [
            "test_*.py",
            "temp_*.py", 
            "*test*.pyc",
            "*broken*.py",
            "*error*.py",
            "*example*.py",
        ]
        
        protected_files = ["test_basic.py", "app.py", "__init__.py", "conftest.py", "protected_test.py"]
        protected_dirs = ["src", "tests", ".github", "venv", "__pycache__"]
        
        files_removed = 0
        for pattern in test_patterns:
            for test_file in Path(directory).rglob(pattern):
                # Skip protected directories
                if any(protected_dir in str(test_file) for protected_dir in protected_dirs):
                    continue
                # Skip protected files
                if test_file.name in protected_files:
                    continue
                # Skip this file
                if "auto_healer.py" in str(test_file):
                    continue
                try:
                    test_file.unlink()
                    print(f"🗑️  Removed: {test_file}")
                    files_removed += 1
                except Exception as e:
                    print(f"⚠️  Could not remove {test_file}: {e}")
        
        return files_removed

    def heal_directory(self, directory="."):
        """Main function to heal all Python files"""
        print("🚀 Starting Auto-Healing Pipeline...")
        
        # Create demo files to show healing in action
        self.create_test_files_for_demo()
        
        python_files = list(Path(directory).rglob("*.py"))
        print(f"📁 Found {len(python_files)} Python files")
        
        for py_file in python_files:
            self.heal_file(str(py_file))
        
        print(f"🔧 Applied {self.fixes_applied} fixes across {len(python_files)} files")
        
        removed_count = self.cleanup_test_files(directory)
        print(f"🧹 Cleaned up {removed_count} temporary files")
        
        return self.fixes_applied

def main():
    healer = PythonAutoHealer()
    try:
        fixes_applied = healer.heal_directory()
        print(f"🎉 Auto-healing completed successfully!")
        print(f"📊 Summary: {fixes_applied} files healed")
        return 0
    except Exception as e:
        print(f"💥 Auto-healing failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
=======
jobs:
  auto-heal:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      with:
        token: ${{ secrets.GITHUB_TOKEN }}

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Run Auto-Healer
      run: |
        echo "🔍 Starting Super Python Auto-Healer..."
        python .github/scripts/auto_healer.py --auto-cleanup

    - name: Install dependencies
      run: |
        echo "📦 Installing dependencies..."
        if [ -f requirements.txt ]; then
          pip install -r requirements.txt
        fi

    - name: Test application
      run: |
        echo "🚀 Testing Python application..."
        # Test syntax of all Python files
        find . -name "*.py" -exec python -m py_compile {} \;
        
        # Run main application
        if [ -f "src/app.py" ]; then
          python src/app.py
        fi
        
        # Run tests
        if [ -f "tests/test_basic.py" ]; then
          python tests/test_basic.py
        fi

    - name: Commit and push fixes
      run: |
        echo "📝 Checking for changes to commit..."
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        
        # Check if there are changes to commit
        git add .
        if ! git diff --staged --quiet; then
          git commit -m "🤖 Auto-heal: Fixed Python syntax errors"
          git push
          echo "✅ Changes committed and pushed"
        else
          echo "✅ No changes to commit"
        fi

    - name: Generate report
      run: |
        echo "📊 Generating final report..."
        echo "### 🛠️ Auto-Healing Report" >> $GITHUB_STEP_SUMMARY
        echo "" >> $GITHUB_STEP_SUMMARY
        echo "**Status:** ✅ Success" >> $GITHUB_STEP_SUMMARY
        echo "**Python Version:** $(python --version)" >> $GITHUB_STEP_SUMMARY
        echo "**Workflow:** Auto-healing completed" >> $GITHUB_STEP_SUMMARY
        echo "" >> $GITHUB_STEP_SUMMARY
        echo "---" >> $GITHUB_STEP_SUMMARY
        echo "Job completed at: $(date)" >> $GITHUB_STEP_SUMMARY
>>>>>>> 83539739e9a55b8855fdec163e7b87b9d025b068
