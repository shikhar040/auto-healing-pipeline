import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import hello_world, calculate_sum

def test_hello_world():
    result = hello_world()
    assert result == "Hello, World!"

def test_calculate_sum():
    result = calculate_sum(2, 3)
    assert result == 5

if __name__ == "__main__":
    test_hello_world()
    test_calculate_sum()
    print("✅ All tests passed!")
