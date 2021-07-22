import cv2
import pyautogui

from secondary_functions import *


def play_music(text):
    pyautogui.PAUSE = 0.3
    if (text.lower()[0:9] == 'следующий') or (text.lower()[0:9] == 'следущий'):
        pyautogui.press('nexttrack')
    elif text.lower()[0:10] == 'предыдущий':
        pyautogui.press('prevtrack')
        pyautogui.press('prevtrack')
    elif text.lower() == 'сначала':
        pyautogui.press('prevtrack')
    else:
        pyautogui.click(1740, 1060)
        pyautogui.click(1740, 920)
        pyautogui.click(100, 1060)
        pyautogui.click(130, 1000)
        pyautogui.write('spotify')
        pyautogui.press('enter')
        pyautogui.click(100, 100)
        pyautogui.click(100, 120)
        if check_language(text):
            pyautogui.hotkey('alt', 'shift')
            pyautogui.write(translate(text))
        else:
            pyautogui.write(text)
        pyautogui.dragTo(880, 370, 0.5)
        pyautogui.click()
    dictionary = {
        'text': 'Включил ' + text,
        'type': 'text'
    }
    return dictionary


def volume_up(n):
    n = n // 2
    for i in range(n):
        pyautogui.press('volumeup')
    return {
        'type': 'text',
        'text': 'Увеличил громкость на ' + str(n * 2) + ' процентов'
    }


def volume_down(n):
    n = n // 2
    for i in range(n):
        pyautogui.press('volumedown')
    return {
        'type': 'text',
        'text': 'Уменьшил громкость на ' + str(n * 2) + ' процентов'
    }


def mute():
    pyautogui.hotkey('volumemute')
    return {
        'type': 'text',
        'text': 'Выключил звук/Включил звук'
    }


def pause():
    pyautogui.press('playpause')
    return {
        'type': 'text',
        'text': 'Поставил на паузу/Продолжил'
    }


def make_screenshot():
    dictionary = {}
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.jpg')
    dictionary['attachment'] = 'screenshot.jpg'
    dictionary['type'] = 'screenshot'
    dictionary['text'] = 'Скриншот'
    return dictionary


def make_webcam_photo():
    dictionary = {}
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('web_camera.jpg', frame)
    dictionary['attachment'] = 'web_camera.jpg'
    dictionary['type'] = 'web_camera'
    dictionary['text'] = 'Захват фото с вебкамеры'
    return dictionary


def control_pc(text):
    dictionary = {}
    if text:
        if text.lower().replace(' ', '') == 'сделайскриншот' or \
                text.lower().replace(' ', '') == 'сделайскрин' or \
                text.lower().replace(' ', '') == 'скрин' or \
                text.lower().replace(' ', '') == 'скриншот':
            dictionary = make_screenshot()
        elif text.lower().replace(' ', '') == 'вебка' or \
                text.lower().replace(' ', '') == 'вебкамера':
            dictionary = make_webcam_photo()
        elif text.lower().replace(' ', '') == 'поставьнапаузу' or \
                text.lower()[0:12] == 'воспроизведи' or \
                text.lower()[0:8] == 'продолжи':
            dictionary = pause()
        elif text.lower().replace(' ', '') == 'выключизвук' or \
                text.lower().replace(' ', '') == 'включизвук':
            dictionary = mute()
        elif text.lower()[0:7] == 'включи ':
            dictionary = play_music(text.lower()[7:])
        elif text.lower().replace(' ', '')[0:18] == 'увеличьгромкостьна':
            dictionary = volume_up(int(text.lower().replace(' ', '')[18:20]))
        elif text.lower().replace(' ', '')[0:18] == 'уменьшигромкостьна':
            dictionary = volume_down(int(text.lower().replace(' ', '')[18:20]))

    return dictionary


def test():
    print(pyautogui.KEYBOARD_KEYS)


if __name__ == '__main__':
    test()
