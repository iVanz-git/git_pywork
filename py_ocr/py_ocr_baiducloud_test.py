import time
import keyboard
import os
from PIL import ImageGrab
from bd_aip import get_content
from temp import nameGenerate


'''
1.保存图片到本地
2.识别本地图片
'''

# 主要功能为，截图并保存的主方法screen()
# 另外添加一个返回值，返回的 是 调用该函数的时间戳 的 基础字符串baseName，该字符串由nameGenerate()方法生成，为确保同一次截图时的 图片 和 文本文档 文件名字相同，必须尽量少调用该nameGenerate()函数，确保不会产生因多次调用函数时间差导致的 基础字符串 不同。
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
    baseName = nameGenerate()
    image.save(baseName + '_screen_img.jpeg')
    return baseName
    

# 定义方法，用来把生成的字符串写入txt文件，并且打开该文件
# 增加返回值，返回值为 字符串，表明生成的文本文档的路径
def fileTextGen():
    file_Txt = open(baseName + '_screen_img.txt', mode='w', encoding='utf-8')
    file_Txt.write(get_content())
    file_Txt.close()
    return "识别后的文本文档已经生成,位于\n" + baseName + '_screen_img.txt\n'
    

    
# 启动程序时为死循环，确保可以一次运行程序，一直截图并识别截图中的文字
while True:
    # screen() 方法设计了一个返回值，就是前面根据时间戳生成字符串的函数nameGenerate()，确保这个函数尽量只调用一次，否则会出现时间差导致文件名字差异，使得同一次识别时的的 图片文件.jpeg 与 写入文档文件.txt 名字不统一，造成无法执行写入操作
    # 这里的screen()方法返回值传递给 baseName 作为后续使用
    # 此处非常重要！！！@iVanZ;2022-08-26 00:09:09 +0800
    baseName = screen()
    date = get_content()
    # 此处两个效果，1.执行了fileTextGen()方法，2.将完成执行后的返回值 “生成文本文档的路径” 作为字符串信息显示在控制台
    print(fileTextGen())
    # 将识别后的结果 先打印在控制台上
    print("识别内容如下:\n" + date)
    # 打开文本识别后,生成的文本文档
    os.startfile(baseName + '_screen_img.txt')
    # 打开文本识别后,生成的图片
    os.startfile(baseName + '_screen_img.jpeg')




