def collatz(number):
    if number % 2 == 0:
        print("{}//2: {}".format(number, number // 2))
        return number // 2
    else :
        print("3*{}+1: {}".format(number, 3 * number + 1))
        return 3 * number + 1


print("请输入一个整数：")
try:
    number = int(input())
    while number != 1:
        number = collatz(number)
        continue
except ValueError:
    print("输入必须为一个整数")
