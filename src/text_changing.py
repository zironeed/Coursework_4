def format_text(text: str) -> str:
    """
    Удаление ненужных букв в полях
    :param text: Строка для форматирования
    :return: Отформатированная строка
    """
    patterns = {
        1: ['<highlighttext>', ''],
        2: ['</highlighttext>', '']
    }

    if text == "null":
        return f"Данных нет"
    elif text is None:
        return f"Данных нет"
    else:
        for i in patterns:
            text = text.replace(patterns[i][0], patterns[i][1])
        return text
