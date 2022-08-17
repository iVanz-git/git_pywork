import os
import shutil
import time

"""
# 准备目录的路径
"""
srcdir = r" X:\ "

for fname in os.listdir(srcdir):
    curr_path = f"{srcdir}/{fname}"
    print(curr_path)
    if os.listdir(curr_path):
        continue
    file_ext = fname.split(".")[-1]
    

