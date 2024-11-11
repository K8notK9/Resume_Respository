def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

file_name = (input("Enter a filename: "))
word_count = count_words(file_name)
print(f"Number of words in '{file_name}': {word_count}")
