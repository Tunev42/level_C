def caesar_decrypt(text, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    result = []
    for char in text.lower():
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = (pos - shift) % 33
            result.append(alphabet[new_pos])
        else:
            result.append(char)

    return ''.join(result)


def column_decrypt(text, key):
    if not text or key == 1:
        return text
    text_no_spaces = text.replace(' ', '')
    cols = key
    rows = len(text_no_spaces) // cols
    if len(text_no_spaces) % cols != 0:
        rows += 1
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for col in range(cols):
        for row in range(rows):
            if idx < len(text_no_spaces):
                matrix[row][col] = text_no_spaces[idx]
                idx += 1
    decrypted = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]:
                decrypted.append(matrix[row][col])
    return ''.join(decrypted)


def decrypt_message(encrypted_text, caesar_shift, column_key):
    column_decrypted = column_decrypt(encrypted_text, column_key)
    final_text = caesar_decrypt(column_decrypted, caesar_shift)
    return final_text, column_decrypted


def main():
    encrypted_text = input("Введите зашифрованный текст: ").lower()

    try:
        caesar_shift = int(input("Введите сдвиг для шифра Цезаря: "))
        column_key = int(input("Введите ключ для перестановки по столбцам: "))
    except ValueError:
        print("Ошибка: ключи должны быть числами!")
        return
    decrypted, intermediate = decrypt_message(encrypted_text, caesar_shift, column_key)
    print(f"Зашифрованный текст: {encrypted_text}")
    print(f"После перестановки: {intermediate}")
    print(f"Расшифрованный текст: {decrypted}")


if __name__ == "__main__":
    main()