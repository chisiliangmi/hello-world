from cal_num import CalNum


if __name__ == "__main__":
    file_path = '中欧班列（满、二）运行情况表2021051516.xlsx'
    city1 = '满洲里'
    city2 = '二连'
    cal_num = CalNum(file_path)
    cal_num.run_cal_num(city1, city2)
    cal_num.run_cal_num_(city1, city2)
