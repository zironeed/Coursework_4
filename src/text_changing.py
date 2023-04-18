def text_change(text: str) -> str:
    """
    Удаление лишних символов
    :param text: Текст для форматирования
    :return: Отфармотированный текст
    """
    patterns = {
        1: ['<highlighttext>', ''],
        2: ['</highlighttext>', '']
    }

    if text is None:
        return f"Нет данных"
    elif text == "null":
        return f"Нет данных"
    else:
        for i in patterns:
            text = text.replace(patterns[i][0], patterns[i][1])

        return text.lower()

print(text_change("asdfjsldfjdlverjglkajlvfLKJGLSKDJFLSDKv"))
