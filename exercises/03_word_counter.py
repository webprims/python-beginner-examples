text = input("Enter a sentence: ").strip()

if not text:
    print("Word count: 0")
else:
    words = text.split()
    print("Word count:", len(words))
