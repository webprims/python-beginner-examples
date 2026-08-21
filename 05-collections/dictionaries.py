student = {
    "name": "Harpreet",
    "course": "Python",
    "city": "Amritsar",
}

print(student["name"])
student["level"] = "Beginner"

for key, value in student.items():
    print(f"{key}: {value}")
