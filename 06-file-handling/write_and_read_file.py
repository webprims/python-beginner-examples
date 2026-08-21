filename = "student_notes.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write("Python practice makes concepts clearer.\n")
    file.write("Build small projects and keep experimenting.\n")

with open(filename, "r", encoding="utf-8") as file:
    print(file.read())
