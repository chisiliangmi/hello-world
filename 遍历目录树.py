import os

for folderName, subfolders, filenames in os.walk('D:\\Python\\python_work\\benbanfa'):
    print('当前文件夹是： ' + folderName)

    for subfolder in subfolders:
        print(folderName + '中有子文件夹： ' + subfolder)
    for filename in filenames:
        print(folderName + '中有文件： ' + filename)

    print('\n')
