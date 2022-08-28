# 根据百度云的OCR文字识别项目---直接读取 截图的剪切板即可！
---
原教程[地址](https://www.bilibili.com/video/BV1YA4115762)：https://www.bilibili.com/video/BV1YA4115762

>在原作基础上增加了一些效果，方便使用
>2022-08-25 20:21:27 +0800 update.


---
>增加[源码文件]说明：
>- 1.bd_aip.py：百度文字识别OCR接口文件
> 如下 APPID 请提前在百度 https://ai.baidu.com/tech/ocr_general 自己申请使用免费的或者付费的。申请完后，记得领取免费尝鲜，否则会调用失败，错误代码18
> 下面时我本人使用的免费的，1000次/月限制，免费赠送。
> ```python  
>  """ 你的 APPID AK SK """
>   APP_ID = '27148737'
>   API_KEY = 'WGCGn5K7zhSOK7KITX9e2kyB'
>   SECRET_KEY = 'uxxd3ejiN8GrtrNbPglcPqhpntH3fRsY'
> ```
>- 2.py_ocr_baiducloud_main.py：程序启动入口文件, 请运行此文件！
>   - 使用前请先确认截图热键与代码一致。在def screen()方法中:
>   - 本人用当前截图软件的热键 alt + shift + Q, 各自根据需求自己更改即可
>    ```python 
>   keyboard.wait(hotkey='alt + shift + q')
>- 3.temp.py：公用的方法在此文件
>- 4.Output_result_display.md：结果展示
>- 5.imageCache_：保存每次截图的图片在此目录下
>
>2022-08-25 21:14:45 +0800
>


