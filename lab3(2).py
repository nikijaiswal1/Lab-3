with open("example.txt", "w") as f:
    f.write("Hello, this is a test file.\nWelcome to file handling in Python.")

with open("example.txt", "r") as f:
    # Read the first 5 characters
    part1 = f.read(5)
    print("First 5 characters:", part1)

    f.seek(0)
    full_content = f.read()
    print("Full content after seek(0):\n", full_content)

    f.seek(18)
    
    part2 = f.read()
    print("Content from position 18:\n", part2)
