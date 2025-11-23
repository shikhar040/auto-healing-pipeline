print("Testing Python script...")
try:
    with open("broken.txt", "r") as f:
        content = f.read()
        print("File content:", repr(content))
    print("SUCCESS: File read successfully!")
except Exception as e:
    print("ERROR:", e)
    exit(1)
