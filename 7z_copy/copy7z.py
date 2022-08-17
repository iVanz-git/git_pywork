
import os
import zipfile
import shutil

# def unzip_file(zip_file, target_file):
#     with zip_file.ZipFile(zip_file, "r") as zfile:
#         for file in zfile.namelist():
#             zfile.extract(file, target_file)

def find_7z(file_path, target, result):  # 寻找7z文件 
    files = os.listdir(file_path)          # 找到路径中的所有文件
    for f in files:
        npath = file_path + '/' + f        # 路径+文件名
        if os.path.isfile(npath):
            if os.path.splitext(npath)[1] == target:  # 匹配目标 .7z
                result.append(npath)
        if os.path.isdir(npath):
            if f[0] == '.':
                pass
            else:
                find_7z(npath, target, result)
    return result


def copy_file(result):              # 复制7z文件
    file_path2 = r"E:\BaiduYunDownload\042_7z"   # 复制到路径
    for file in result:
        print(str(file).split("/")[-1])  # 书名
        file2 = file_path2 + "/" + str(file).split("/")[-1]   # 路径+书名
        shutil.copy(file, file2)   # 复制文件


if __name__ == "__main__":
    file_path = r"E:\BaiduYunDownload\042"
    result = []
    find_7z(file_path, ".7z", result)
    copy_file(result)
