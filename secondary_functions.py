def check_language(text):
    asci = ord(text[0:1])
    if asci > 1000:
        return True
    return False


def translate(text):
    dictionary = {
        'й': 'q',
        'ц': 'w',
        'у': 'e',
        'к': 'r',
        'е': 't',
        'н': 'y',
        'г': 'u',
        'ш': 'i',
        'щ': 'o',
        'з': 'p',
        'х': '[',
        'ъ': ']',
        'ф': 'a',
        'ы': 's',
        'в': 'd',
        'а': 'f',
        'п': 'g',
        'р': 'h',
        'о': 'j',
        'л': 'k',
        'д': 'l',
        'ж': ';',
        'э': '\'',
        'я': 'z',
        'ч': 'x',
        'с': 'c',
        'м': 'v',
        'и': 'b',
        'т': 'n',
        'ь': 'm',
        'б': ',',
        'ю': '.',
    }
    new_text = ''
    for i in range(len(text)):
        if text[i] in dictionary:
            new_text = new_text + dictionary[text[i]]
        else:
            new_text = new_text + text[i]
    return new_text


def test():
    print(translate('ныф'))


if __name__ == '__main__':
    test()
