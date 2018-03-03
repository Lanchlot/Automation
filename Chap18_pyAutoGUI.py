import pyautogui
import time
pyautogui.PAUSE = 1
pyautogui.FailSafe = True


# <--------获取屏幕参数---------pyautogui.size()>
def get_screen_size():
    width, height = pyautogui.size()
    print(width, height)


# <---------控制鼠标------------moveTo(), moveRel(), position()， dragTo(), dragRel()>
def mouse_move():
    for i in range(0, 10):
        pyautogui.moveTo(100, 100, duration=3, pause=0)
        pyautogui.moveTo(200, 200, duration=1, pause=0)
        pyautogui.moveTo(300, 400, duration=2, pause=0)
        pyautogui.moveTo(700, 600, duration=3, pause=0)
    for i in range(0, 10):
        pyautogui.moveRel(10, 10, duration=0.5)     # 相对当前位置偏移量
        pyautogui.moveRel(-10, -10, duration=0.5)


def get_mouse_location():
    while True:
        x, y = pyautogui.position()
        if x == 0:          # 鼠标移动到屏幕最左边退出循环
            break
        else:
            print('{},{}'.format(x, y))
        time.sleep(0.5)


def mouse_click():
    for i in range(1, 3):
        pyautogui.moveTo(928, 751, duration=2)
        pyautogui.click(928, 751, button='left')    # left, right, middle
        time.sleep(2)
        pyautogui.moveTo(1260, 6, duration=2)
        pyautogui.click(1260, 9, button='left')
        # pyautogui.click(500, 500)         # 左键单击
        # pyautogui.doubleClick(500, 500)   # 左键双击
        # pyautogui.rightClick(500, 500)    # 右键双击
        # pyautogui.middleClick(500，500)    # 滚轮双击


def mouse_drag():
    """拖动发生在鼠标的当前位置"""
    # pyautogui.dragTo(500, 500, duration=1)
    # pyautogui.dragRel(10, 10, duration=1)
    pass


def mouse_scroll():
    """滚动发生在鼠标的当前位置"""
    pyautogui.scroll(300)
    pass


# <---------控制屏幕------------>
def get_screen_shot():
    pass


def analyze_screen_shot():
    pass


# <---------控制键盘------------typewrite(), press(), keyDown(), keyUp()>
def keyboard_type():
    time.sleep(5)       # 休眠5秒，用于打开记事本
    pyautogui.typewrite('Hello  World!', 0.2)      # 打印每个字符后暂停0.2秒,防止反应过慢的应用来不及处理输入的字符


def keyboard_press():
    for item in pyautogui.KEYBOARD_KEYS:
        print(item)
    # pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
    # pyautogui.keyDown('shift')
    # pyautogui.press('4')
    # pyautogui.keyUp('shift')


def hot_key():
    # pyautogui.hotkey('ctrl', 'c')
    # pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'alt', 'delete')


# <----------主程序------------->
if __name__ == '__main__':
    pass
