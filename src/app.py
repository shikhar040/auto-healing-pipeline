defx hello_world():
    print("Hello, World!")
    return "Hello, World!"

defx calculate_sum(a, b):
    result = a + b
    print(f"Calculation: {a} + {b} = {result}")
    return result

if __name__ == "__main__":
    hello_world()
    calculate_sum(5, 3)
