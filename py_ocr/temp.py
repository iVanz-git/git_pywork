import time
# from tkinter import image_names

# 这个第三方文件，用于定义两个py文件共同需求的文件名生成方法nameGenerate()，以确保两个py文件不会环形引用
# 自定义将日期转化为字符串，用于后续截图自动保存的命名规则中
# 每次按下截图键时(本人使用Snipaste.exe ，截图热键是 alt + shift + Q)，调用一次nameGenerate()函数，确保每次生成的文件名不同，从而保证所有截图都被保存到指定目录下("./imageCache_/")


def nameGenerate():
    # 生成当前的时间戳字符串：s1
    s1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 遍历该并过滤字符串，将原有时间戳字符串中的':', ' ', '-'全部删除，赋值给：s2
    for i in s1:
        if i == ':' or i == ' ' or i == '-':
            s2 = s1.replace(i, '')
    # 以下两种相对路径方式都是可行的，实际imageName同时包括了路径变更以及上述时间戳字符串s2
    # imageName = "E:\\pywork\\py_ocr\\imageCache_\\" + s2 + 'screen_img.jpeg'
    imageName = "./imageCache_/" + s2 + 'screen_img.jpeg'
    return imageName

