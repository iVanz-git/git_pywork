import datetime
import time

import keyboard
from PIL import ImageGrab


'''
1.保存图片到本地
2.识别本地图片
'''
# 自定义将日期转化为字符串，用于后续截图自动保存的命名规则中
s1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
for i in s1:
    if i == ':' or i == ' ' or i == '-':
        s2 = s1.replace(i, '')


def screen():
    # 用截图软件的热键 alt + shift + Q
    keyboard.wait(hotkey='alt + shift + q')
    keyboard.wait(hotkey='enter')
    # 休息0.5秒，确保剪贴板的截图是实时的
    time.sleep(0.5)
    # 读取剪切板的图片
    image = ImageGrab.grabclipboard()
    # 保存剪切板的图片
    image.save('screen_img.jpeg')


screen()


