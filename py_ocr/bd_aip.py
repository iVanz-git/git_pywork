# @Time : 2022-08-24 23:42:52 +0800
# @Author : iVan

from aip import AipOcr
from temp import nameGenerate

# 下面全是百度的API

""" 你的 APPID AK SK """
APP_ID = '27148737'
API_KEY = 'WGCGn5K7zhSOK7KITX9e2kyB'
SECRET_KEY = 'uxxd3ejiN8GrtrNbPglcPqhpntH3fRsY'


client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取文件 """
def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()

# 将如下操作包装为get_content()方法，方便其他文件调用
def get_content():
    image = get_file_content(nameGenerate())

    # 调用通用文字识别（标准版）
    date = client.basicGeneral(image)
    image_content = ""
    # 调整输出格式
    for words in date['words_result']:
        # print(words['words'])
        image_content += words['words'] + "\n"
    return image_content
