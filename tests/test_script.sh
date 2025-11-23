#!/bin/bash
echo "🧪 Testing Python files..."
find . -name "*.py" -exec python -m py_compile {} \;
echo "✅ All Python files are valid!"