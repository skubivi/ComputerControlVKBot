import cv2
import pyautogui

from secondary_functions import *


def play_music(text):
    pyautogui.PAUSE = 0.3

    pyautogui.click(1740, 1060)
    pyautogui.click(1740, 920)
    pyautogui.click(100, 1060)
    pyautogui.click(130, 1000)
    pyautogui.write('spotify')
    pyautogui.press('enter')
    if text == 'сначала':
        pyautogui.dragTo(910, 920)
        pyautogui.click()
    else:

        pyautogui.click(100, 100)
        pyautogui.click(100, 120)
        if check_language(text):
            pyautogui.hotkey('alt', 'shift')
            pyautogui.write(translate(text))
        else:
            pyautogui.write(text)
        pyautogui.dragTo(880, 370, 0.5)
        pyautogui.click()


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
        elif text.lower()[0:7] == 'включи ':
            play_music(text.lower()[7:])

    return dictionary
