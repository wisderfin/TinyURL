def next_short(latest_short: str = '') -> str:
    if not latest_short:
        return 'A'  # Если строка пустая, начинаем с 'A'
    chars = list(latest_short)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    # Индекс последнего символа в алфавите
    max_index = len(alphabet) - 1
    # Итерируемся с конца строки
    for i in range(len(chars)-1, -1, -1):
        char = chars[i]
        # Получаем индекс текущего символа в алфавите
        index = alphabet.index(char)
        # Если текущий символ не является последним в алфавите
        if index < max_index:
            chars[i] = alphabet[index + 1]
            break
        else:
            chars[i] = alphabet[0]
            # Если символ был последним в алфавите, добавляем новый символ в конец строки
            if i == 0:
                chars.append(alphabet[0])
    return ''.join(chars)










