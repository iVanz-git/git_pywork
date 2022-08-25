import datetime
import time
import keyboard
from PIL import ImageGrab
from bd_aip import get_content
from temp import nameGenerate


'''
1.保存图片到本地
2.识别本地图片
'''


def screen():
    # 用当前截图软件的热键 alt + shift + Q
    keyboard.wait(hotkey='alt + shift + q')
    keyboard.wait(hotkey='enter')   
    # 休息0.5秒，确保剪贴板的截图是实时的
    time.sleep(0.5)
    # 读取剪切板的图片
    image = ImageGrab.grabclipboard()
    # 根据nameGenerate()方法，保存剪切板的图片，确保以下要求完成：
    #   1.生成图片名称
    #   2.确保图片保存在指定目录中
    image.save(nameGenerate())


# 死循环，确保可以一次运行程序，一直截图并识别截图中的文字
while True:
    screen()
    date = get_content()
    print(date)
    




