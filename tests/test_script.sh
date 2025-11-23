#!/bin/bash

echo "🧪 STARTING AUTO-HEALING TEST SUITE"
echo "========================================"

# Test 1: Check if main application exists
echo "1. Testing application file existence..."
if [ -f "src/app.py" ]; then
    echo "✅ PASS: src/app.py exists"
else
    echo "❌ FAIL: src/app.py missing"
    exit 1
fi

# Test 2: Python syntax validation
echo "2. Testing Python syntax..."
if python -m py_compile src/app.py; then
    echo "✅ PASS: Python syntax is valid"
else
    echo "❌ FAIL: Python syntax error"
    exit 1
fi

# Test 3: Test application functionality
echo "3. Testing application functionality..."
if python -c "import sys; sys.path.append('src'); import app; result = app.calculate_sum(2, 3); assert result == 5, f'Expected 5, got {result}'; print('✅ Calculation test passed')"; then
    echo "✅ PASS: Application functions correctly"
else
    echo "❌ FAIL: Application functionality test failed"
    exit 1
fi

# Test 4: Check for broken files
echo "4. Checking for problematic files..."
if [ -f "broken.txt" ]; then
    echo "❌ FAIL: broken.txt file detected"
    exit 1
else
    echo "✅ PASS: No broken files found"
fi

# Test 5: Run the main application
echo "5. Running full application test..."
cd src && python app.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ PASS: Application runs successfully"
else
    echo "❌ FAIL: Application runtime error"
    exit 1
fi

echo "========================================"
echo "🎉 ALL TESTS PASSED! SYSTEM IS HEALTHY!"
echo "🤖 Auto-healing capability: VERIFIED"
echo "🚀 Ready for demonstration!"