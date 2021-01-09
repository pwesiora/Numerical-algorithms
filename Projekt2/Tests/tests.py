from tqdm import tqdm
from CustomTypes.MyMatrix import Matrix
from Gauss.GaussElimination import gauss
import time
import xlsxwriter

def h1_h2(size, test_num, matrix_type):

    time_whole = time.time()
    avg_error = 0

    workbook = xlsxwriter.Workbook('h1_and_h2_results.xlsx')
    worksheet = workbook.add_worksheet()

    for i in tqdm(range(test_num)):
        matrix_a = Matrix.makeRandom(size, size, matrix_type)
        matrix_b = Matrix.makeRandom(size, 1, matrix_type)
        c = gauss(matrix_a, matrix_b, 0)
        avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / size);
    av_time = (time.time() - time_whole) / test_num
    avg_error = avg_error / test_num
    worksheet.write(0, 0, av_time)
    worksheet.write(3, 0, avg_error)

    avg_error = 0
    time_whole = time.time()
    for i in tqdm(range(test_num)):
        matrix_a = Matrix.makeRandom(size, size, matrix_type)
        matrix_b = Matrix.makeRandom(size, 1, matrix_type)
        c = gauss(matrix_a, matrix_b, 1)
        avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / size);
    av_time = (time.time() - time_whole) / test_num
    avg_error = avg_error / test_num
    worksheet.write(1, 0, av_time)
    worksheet.write(4, 0, avg_error)

    avg_error = 0
    time_whole = time.time()
    for i in tqdm(range(test_num)):
        matrix_a = Matrix.makeRandom(size, size, matrix_type)
        matrix_b = Matrix.makeRandom(size, 1, matrix_type)
        c = gauss(matrix_a, matrix_b, 2)
        avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / size);
    avg_error = avg_error / test_num
    av_time = (time.time() - time_whole) / test_num
    worksheet.write(2, 0, av_time)
    worksheet.write(5, 0, avg_error)
    workbook.close()

def h3():
    workbook = xlsxwriter.Workbook('h3_results.xlsx')
    worksheet = workbook.add_worksheet()

    avg_error = 0
    matrix_a = Matrix.makeRandom(5, 5, 3)
    matrix_b = Matrix.makeRandom(5, 1, 3)
    c = gauss(matrix_a, matrix_b, 1)
    avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / 5);
    if avg_error.__eq__("0/1"):
        x = 0
    worksheet.write(1, 0, x)
    print("5")

    avg_error = 0
    matrix_a = Matrix.makeRandom(10, 10, 3)
    matrix_b = Matrix.makeRandom(10, 1, 3)
    c = gauss(matrix_a, matrix_b, 1)
    avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / 10);
    if avg_error.__eq__("0/1"):
        x = 0
    worksheet.write(2, 0, x)
    print("10")

    avg_error = 0
    matrix_a = Matrix.makeRandom(15, 15, 3)
    matrix_b = Matrix.makeRandom(15, 1, 3)
    c = gauss(matrix_a, matrix_b, 1)
    avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / 15);
    if avg_error.__eq__("0/1"):
        x = 0
    worksheet.write(3, 0, x)
    print("15")

    avg_error = 0
    matrix_a = Matrix.makeRandom(20, 20, 3)
    matrix_b = Matrix.makeRandom(20, 1, 3)
    c = gauss(matrix_a, matrix_b, 1)
    avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / 20);
    if avg_error.__eq__("0/1"):
        x = 0
    worksheet.write(4, 0, x)
    print("20")

    avg_error = 0
    matrix_a = Matrix.makeRandom(25, 25, 3)
    matrix_b = Matrix.makeRandom(25, 1, 3)
    c = gauss(matrix_a, matrix_b, 1)
    avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / 25);
    if avg_error.__eq__("0/1"):
        x = 0
    worksheet.write(5, 0, x)
    print("25")

    avg_error = 0
    matrix_a = Matrix.makeRandom(30, 30, 3)
    matrix_b = Matrix.makeRandom(30, 1, 3)
    c = gauss(matrix_a, matrix_b, 1)
    avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / 30);
    print("30")
    if avg_error.__eq__("0/1"):
        x = 0

    workbook.close()

def q1(starting_size, end_size, step, test_num):

    SizeList = []
    ErrorList1 = []
    ErrorList2 = []
    ErrorList3 = []
    avg_error = 0
    avg_error2 = 0
    avg_error3 = 0

    workbook = xlsxwriter.Workbook('q111_results.xlsx')
    worksheet = workbook.add_worksheet()

    for i in tqdm(range(starting_size, end_size, step)):
        for j in range(test_num):
            matrix_a = Matrix.makeRandom(i, i, 2)
            matrix_b = Matrix.makeRandom(i, 1, 2)
            matrix_a2 = matrix_a
            matrix_b2 = matrix_b
            matrix_a3 = matrix_a
            matrix_b3 = matrix_b
            c = gauss(matrix_a, matrix_b, 0)
            c2 = gauss(matrix_a2, matrix_b2, 1)
            c3 = gauss(matrix_a3, matrix_b3, 2)
            avg_error = (matrix_b.__abssub__(matrix_a.__mul__(c)) / i)
            avg_error2 = (matrix_b2.__abssub__(matrix_a2.__mul__(c2)) / i)
            avg_error3 = (matrix_b3.__abssub__(matrix_a3.__mul__(c3)) / i)

        avg_error = avg_error / test_num
        avg_error2 = avg_error2 / test_num
        avg_error3 = avg_error3 / test_num
        SizeList.append(i)
        ErrorList1.append(avg_error)
        ErrorList2.append(avg_error2)
        ErrorList3.append(avg_error3)


    avg_error = 0
        # for i in tqdm(range(sizemin, sizemax, 10)):
        #     for j in range(5):
        #         matrix_a = Matrix.makeRandom(i, i, 1)
        #         matrix_b = Matrix.makeRandom(i, 1, 1)
        #         c = gauss(matrix_a, matrix_b, 2)
        #         avg_error = (matrix_b.__abssub__(matrix_a.__mul__(c)) / i);
        #     avg_error = avg_error / 10
        #     SizeList.append(i)
        #     ErrorList2.append(avg_error)
        #     # print(i)

    worksheet.write_row(11, 0, SizeList)
    worksheet.write_row(12, 0, ErrorList1)
    worksheet.write_row(13, 0, ErrorList2)
    worksheet.write_row(14, 0, ErrorList3)
    workbook.close()


def q2(starting_size, end_size, step, test_num):
    SizeList = []
    SizeList2 = []
    TimeList1 = []
    TimeList2 = []
    TimeList3 = []

    workbook = xlsxwriter.Workbook('q222_results.xlsx')
    worksheet = workbook.add_worksheet()
    # for i in range(starting_size, end_size, step):
    #     time_whole = time.time()
    #     for j in range(test_num):
    #         matrix_a = Matrix.makeRandom(i, i, 1)
    #         matrix_b = Matrix.makeRandom(i, 1, 1)
    #         c = gauss(matrix_a, matrix_b, 1)
    #     av_time = (time.time() - time_whole) / test_num
    #     SizeList.append(i)
    #     TimeList1.append(av_time)
    #     print(i)

    for i in range(starting_size, end_size, step):
        time_whole = time.time()
        for j in range(test_num):
            matrix_a = Matrix.makeRandom(i, i, 2)
            matrix_b = Matrix.makeRandom(i, 1, 2)
            c = gauss(matrix_a, matrix_b, 1)
        av_time = (time.time() - time_whole) / test_num
        TimeList2.append(av_time)
        print(i)

    # for i in range(2, 20):
    #     time_whole = time.time()
    #     for j in range(10):
    #         matrix_a = Matrix.makeRandom(i, i, 3)
    #         matrix_b = Matrix.makeRandom(i, 1, 3)
    #         c = gauss(matrix_a, matrix_b, 1)
    #     av_time = (time.time() - time_whole) / 10
    #     SizeList2.append(i)
    #     TimeList3.append(av_time)
    #     print(i)

    worksheet.write_row(17, 0, SizeList)
    worksheet.write_row(18, 0, TimeList1)
    worksheet.write_row(19, 0, SizeList)
    worksheet.write_row(20, 0, TimeList2)
    worksheet.write_row(21, 0, SizeList2)
    worksheet.write_row(22, 0, TimeList3)
    workbook.close()


def e1():
    matrix_a = Matrix.makeRandom(500, 500, 1)  # float
    matrix_b = Matrix.makeRandom(500, 1, 1)
    time_whole = time.time()
    c = gauss(matrix_a, matrix_b, 0)
    av_time10 = (time.time() - time_whole)
    time_whole = time.time()
    c = gauss(matrix_a, matrix_b, 1)
    av_time11 = (time.time() - time_whole)
    time_whole = time.time()
    c = gauss(matrix_a, matrix_b, 2)
    av_time12 = (time.time() - time_whole)
    print("done")

    workbook = xlsxwriter.Workbook('e1_results.xlsx')
    worksheet = workbook.add_worksheet()

    matrix_a = Matrix.makeRandom(500, 500, 2)  # double
    matrix_b = Matrix.makeRandom(500, 1, 2)
    time_whole = time.time()
    c = gauss(matrix_a, matrix_b, 0)
    av_time20 = (time.time() - time_whole)
    time_whole = time.time()
    c = gauss(matrix_a, matrix_b, 1)
    av_time21 = (time.time() - time_whole)
    time_whole = time.time()
    c = gauss(matrix_a, matrix_b, 2)
    av_time22 = (time.time() - time_whole)
    print("done")

    worksheet.write(24, 0, av_time10)
    worksheet.write(25, 0, av_time11)
    worksheet.write(26, 0, av_time12)
    worksheet.write(27, 0, av_time20)
    worksheet.write(28, 0, av_time21)
    worksheet.write(29, 0, av_time22)
    workbook.close()


def test_1(size, test_num, gauss_type, matrix_type):
    time_whole = time.time()
    avg_error = 0
    workbook = xlsxwriter.Workbook('t'+str(matrix_type)+'_results.xlsx')
    worksheet = workbook.add_worksheet()
    if gauss_type not in (0, 1, 2):
        print("Bad gauss version.\nAvailable gauss versions: 0, 1, 2\n")
    if matrix_type not in (0, 1, 2, 3):
        print("Bad matrix type.\nAvailable matrix types: 0, 1, 2, 3")
    if matrix_type == 0:
        print("Data type: default")
    elif matrix_type == 1:
        print("Data type: double")
    elif matrix_type == 2:
        print("Data type: float")
    elif matrix_type == 3:
        print("Data type: MyFraction type")
    for i in range(test_num):
        matrix_a = Matrix.makeRandom(size, size, matrix_type)
        matrix_b = Matrix.makeRandom(size, 1, matrix_type)
        c = gauss(matrix_a, matrix_b, gauss_type)
        if matrix_type != 4:
            avg_error = avg_error + (matrix_b.__abssub__(matrix_a.__mul__(c)) / size);
    avg_time = (time.time() - time_whole) / test_num
    if matrix_type != 4:
        avg_error = avg_error / test_num
    if gauss_type == 0:
        print("Gauss without pivot")
    elif gauss_type == 1:
        print("Gauss with partial pivot")
    elif gauss_type == 2:
        print("Gauss with full pivot")
    print("Whole: %s seconds" % (time.time() - time_whole))
    print("Average time: %s seconds" % avg_time)
    if matrix_type != 4:
        print("Average error: ", avg_error)
    if matrix_type == 4:
        print("Average error: 0")
    print("\n")
    workbook.close()

def test1Create(version):
    test_1(300, 30, version, 1)

