import pyautogui
import python_imagesearch.imagesearch as imgsearch
import time
# from pynput import mouse
# from pynput.mouse import Controller, Button
import win32api, win32con
# import ctypes


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def bin_clicker():

    pos = imgsearch.imagesearch_region_loop("img/max-bin.png", 0.001, 0, 0, 1000, 800)
    click(pos[0], pos[1])
    pos = imgsearch.imagesearch_region_loop("img/buy-bin.png", 0.001, 0, 0, 1000, 800)


def veve_clicker_comics():
    pos = imgsearch.imagesearch_region_loop("img/buy-button.png", 0.001, 0, 0, 300, 500, 0.8)
    print(time.time())
    click(pos[0], pos[1])
    print(time.time())
    time.sleep(1)
    # pos = imgsearch.imagesearch_loop("img/buy.png", 0.01)
    # while True:
    #     time.sleep(0.3)
    #     click(pos[0], pos[1])
    #     pos = imgsearch.imagesearch_loop("img/buy.png", 0.01)


def veve_clicker_collectible():
    pos = imgsearch.imagesearch_region_loop("img/buy-collectible.png", 0.05, 0, 0, 550, 1000, 0.9)
    click(pos[0], pos[1])
    time.sleep(1)
    pos = imgsearch.imagesearch_loop("img/buy.png", 0.01)
    while True:
        time.sleep(0.3)
        click(pos[0], pos[1])
        pos = imgsearch.imagesearch_loop("img/buy.png", 0.01)


if __name__ == '__main__':
    print("Bot is active!")
    time.sleep(2)
    print(time.time())
    veve_clicker_comics()


