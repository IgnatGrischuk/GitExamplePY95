def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            char_code = ord(char) + shift
            if char_code > ord('Z'):
                char_code -= 26
            result += chr(char_code) if is_upper else chr(char_code).lower()
        else:
            result += char
    return result


def encrypt_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    encrypted_lines = [caesar_cipher(line, i + 1) for i, line in
                       enumerate(lines)]

    with open('TaskSeven2.txt', 'w') as output_file:
        output_file.writelines(encrypted_lines)


encrypt_file('TaskSeven.txt')
