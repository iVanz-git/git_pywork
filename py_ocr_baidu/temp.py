import os
import time
# from tkinter import image_names

# 这个第三者文件，用于定义两个py文件共同需求的文件名生成方法nameGenerate()，以确保两个py文件不会环形引用
# 自定义将日期转化为字符串，用于后续截图自动保存的命名规则中
# 每次按下截图键时(本人使用Snipaste.exe ，截图热键是 alt + shift + Q)，调用一次nameGenerate()函数，确保每次生成的文件名不同，从而保证所有截图都被保存到指定目录下("./image_and_txt_Cache_/")

# s2 = ""
def nameGenerate():
    # 生成当前的时间戳字符串：s1
    # 为解决文件名错过差异，取消 秒 的字符 @iVanZ; 2022-08-26 00:39:37 +0800
    s1 = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    # 原始写法如下，将 秒 加入文件后，容易产生bug：即文件在上一秒生成，执行打开功能时寻址路径却在下一秒，造成文件名不匹配，使得程序无法运行！ 详见截图 E:\pywork\py_ocr\py_prc_目前遗留的bug-20220826.png
    # s1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 过滤字符串，将原有时间戳字符串中的 ':', ' ' 全部替换，然后赋值给：s2
    s2 = s1.replace(' ', '_').replace(':', '-')
    # 以下两种相对路径方式都是可行的，实际imageName同时包括了路径变更以及上述时间戳字符串s2
    # imageName = "E:\\pywork\\py_ocr\\image_and_txt_Cache_\\" + s2 + 'screen_img.jpeg'
    path = os.getcwd()
    imageName = path+ "\\image_and_txt_Cache_\\" + s2
    return imageName


    