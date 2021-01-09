from multiprocessing.pool import Pool

import psutil as psutil
import xlsxwriter
from CustomTypes.MyMatrix import Matrix
from Gauss.GaussElimination import gauss
from Tests.tests import *

if __name__ == '__main__':
    matrix1 = Matrix.createFromList([[1.2, 2.6, -0.1, 1.5],
                                     [4.5, 9.8, -0.4, 5.7],
                                     [0.1, -0.1, -0.3, -3.5],
                                     [4.5, -5.2, 4.2, -3.4]])
    matrix2 = Matrix.createFromList([[13.15],
                                     [49.84],
                                     [-14.08],
                                     [-46.51]])

    size_of_matrix = 500
    avg_from = 15

    a = gauss(matrix1,matrix2,1)
    print(a)
	
    #workbook = xlsxwriter.Workbook('wyniki.xlsx')
    #worksheet = workbook.add_worksheet()

    #h1_h2(size_of_matrix, avg_from, 1)
    #h3()
    #q1(5, size_of_matrix, 5, avg_from)
    #q2(5, size_of_matrix, 5, avg_from)
    #e1()
    #test_1(size_of_matrix-480, 3, 0, 3)
    #test_1(size_of_matrix-480, 3, 1, 3)
    #test_1(size_of_matrix-480, 3, 2, 3)
    #workbook.close()
