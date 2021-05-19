from cal_num import CalNum


if __name__ == "__main__":
    file_path = '中欧班列（满、二）运行情况表2021051516.xlsx'
    cal_num = CalNum(file_path)
    citys = ['满洲里','二连','绥芬河']
    for i in range(len(citys)):
        city = citys[i]
        cal_num.run_cal_num(city)
        cal_num.run_cal_num_(city)
