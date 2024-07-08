while True:
    text = input('Text to Clean: ')

    print(text.upper())
    print(text.lower())
    print(text.title())

    text_clean = text.strip()

    print(f'---{text}---')
    print(f'---{text_clean}---')

