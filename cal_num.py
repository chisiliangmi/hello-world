import openpyxl
import re


class CalNum:
    def __init__(self, file_path):
        self.wb = openpyxl.load_workbook(file_path)
        self.sheet_names = self.wb.get_sheet_names()

    def run_cal_num(self, city1, city2):
        # 使用正则表达式以匹配工作表名字
        regex = ['.*去', '.*回', '\\W', '^X8.*']
        global symbol
        symbol = []
        for i in range(len(self.sheet_names)):
            for j in range(len(regex)):
                Regex = re.compile(regex[j])
                reg = Regex.search(self.sheet_names[i])
                if reg and j == 0:
                    symbol_1 = i
                    global num_leave_city1, num_leave_city2
                    num_leave_city1, num_leave_city2 = self.zhida_leave(
                        symbol_1, city1, city2)
                    print("出境 %s 技术直达： %d" % (city1, num_leave_city1))
                    print("出境 %s 技术直达： %d" % (city2, num_leave_city2))
                    print('\n')
                elif reg and j == 1:
                    symbol_2 = i
                    global num_back_city1, num_back_city2
                    num_back_city1, num_back_city2 = self.zhida_back(
                        symbol_2, city1, city2)
                    print("回程 %s 技术直达： %d" % (city1, num_back_city1))
                    print("回程 %s 技术直达： %d" % (city2, num_back_city2))
                    print('\n')
                elif reg and j == 2:
                    symbol.append(0)
                elif reg and j == 3:
                    symbol.append(i)

    # 技术直达车次
    # 计算去程
    def zhida_leave(self, symbol_1, city1, city2):
        # 要操作的表
        sheet = self.wb[self.sheet_names[symbol_1]]
        num_leave_city1_ = 0
        num_leave_city2_ = 0
        for row in range(5, sheet.max_row + 1):
            # 确定列车到达
            if sheet['Y' + str(row)].value == city1 and sheet[
                    'Z' + str(row)].value is not None:
                num_leave_city1_ += 1
            elif sheet['Y' + str(row)].value == city2 and sheet[
                    'D' + str(row)].value is not None:
                num_leave_city2_ += 1

        return num_leave_city1_, num_leave_city2_

    # 计算回程
    def zhida_back(self, symbol_2, city1, city2):
        sheet = self.wb[self.sheet_names[symbol_2]]
        num_back_city1_ = 0
        num_back_city2_ = 0
        for row in range(5, sheet.max_row + 1):
            # 确定列车出发
            if sheet['C' + str(row)].value == str(city1) and sheet[
                    'D' + str(row)].value is not None:
                num_back_city1_ += 1
            elif sheet['C' + str(row)].value == str(city2) and sheet[
                    'D' + str(row)].value is not None:
                num_back_city2_ += 1
        return num_back_city1_, num_back_city2_

    def run_cal_num_(self, city1, city2):
        sym = []
        for i in range(len(symbol)):
            if symbol[i] == 0:
                sym.append(i)
                continue

        sym1 = symbol[:sym[0]]
        sym2 = symbol[sym[0] + 1:sym[1]]
        sym3 = symbol[sym[1] + 1:sym[2]]
        sym4 = symbol[sym[2] + 1:]

        number_leave_city1 = 0
        for i in range(len(sym1)):
            sheet = self.wb[self.sheet_names[sym1[i]]]
            number_leave_city = CalNum.train_leave(sheet, city1)
            number_leave_city1 += number_leave_city

        print("出境 %s 班列： %d" % (city1, number_leave_city1))

        number_leave_city2 = 0
        for i in range(len(sym2)):
            sheet = self.wb[self.sheet_names[sym2[i]]]
            number_leave_city = CalNum.train_leave(sheet, city2)
            number_leave_city2 += number_leave_city

        print("出境 %s 班列： %d" % (city2, number_leave_city2))
        print('\n')

        number_back_city1 = 0
        for i in range(len(sym3)):
            sheet = self.wb[self.sheet_names[sym3[i]]]
            number_back_city = CalNum.train_back(sheet, city1)
            number_back_city1 += number_back_city

        print("回程 %s 班列： %d" % (city1, number_back_city1))

        number_back_city2 = 0
        for i in range(len(sym4)):
            sheet = self.wb[self.sheet_names[sym4[i]]]
            number_back_city = CalNum.train_back(sheet, city2)
            number_back_city2 += number_back_city

        print("回程 %s 班列： %d" % (city2, number_back_city2))
        print('\n')

    # 计算一个工作表的班列车次
    # 计算去程
    def train_leave(sheet, city):
        number_leave_city = 0
        for row in range(10, 60):
            if sheet['S3'].value == city and sheet[
                    'B' + str(row)].value is not None:
                number_leave_city += 1

        return number_leave_city

    # 计算回程
    def train_back(sheet, city):
        number_back_city = 0
        for row in range(10, 60):
            if sheet['C3'].value == city and sheet[
                    'B' + str(row)].value is not None:
                number_back_city += 1

        return number_back_city
