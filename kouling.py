import re


def check(kouling):

    if len(kouling) < 8:
        print("请至少输入8位密码！")
        return False

    xiaoRegex = re.compile(r'[a-z]+')
    if xiaoRegex.findall(kouling) == []:
        print("请至少输入1个小写字母！")
        return False

    daRegex = re.compile(r'[A-Z]+')
    if daRegex.findall(kouling) == []:
        print("请至少输入1个大写字母！")
        return False

    numRegex = re.compile(r'\d+')
    if numRegex.findall(kouling) == []:
        print("请至少输入1个数字！")
        return False


if __name__=="__main__":
    mima = input(">>")
    check(mima)
