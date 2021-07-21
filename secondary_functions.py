import requests
import urllib.request
import json

from config import yandex_iam_token
from config import yandex_folder_id


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


def save_file(link):
    r = requests.get(link, allow_redirects=True)
    open('audio.ogg', "wb").write(r.content)


def speech_to_text():
    with open("audio.ogg", "rb") as f:
        data = f.read()

    params = "&".join([
        "topic=general",
        "folderId=%s" % yandex_folder_id,
        "lang=ru-RU"
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % yandex_iam_token)

    response_data = urllib.request.urlopen(url).read().decode('UTF-8')
    decoded_data = json.loads(response_data)

    if decoded_data.get("error_code") is None:
        return decoded_data.get("result")


def test():
    speech_to_text()


if __name__ == '__main__':
    test()
