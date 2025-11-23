#!/bin/bash

echo "🧪 STARTING TEST SUITE"
echo "======================"

# Test 1: Check if main application exists
echo "1. Testing application file..."
if [ -f "src/app.py" ]; then
    echo "✅ PASS: src/app.py exists"
else
    echo "❌ FAIL: src/app.py missing"
    exit 1
fi

# Test 2: Python syntax validation
echo "2. Testing Python syntax..."
if python -m py_compile src/app.py; then
    echo "✅ PASS: Python syntax valid"
else
    echo "❌ FAIL: Python syntax error"
    exit 1
fi

# Test 3: Application functionality
echo "3. Testing application functionality..."
cd src
python -c "import app; app.hello_world()"
cd ..

# Test 4: Check for broken files
echo "4. Checking for problematic files..."
if [ -f "broken.txt" ]; then
    echo "❌ FAIL: broken.txt detected"
    exit 1
else
    echo "✅ PASS: No broken files"
fi

echo "======================"
echo "🎉 ALL TESTS PASSED!"
echo "🚀 System is HEALTHY!"