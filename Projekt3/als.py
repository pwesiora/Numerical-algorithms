import time
import tabel as tb
import numpy as np
import pandas as pd
import xlsxwriter
from tqdm import tqdm
from ParserAndUtilities import parsers
from ParserAndUtilities import utility
from CustomTypes.MyMatrix import Matrix
from Gauss.gauss import gauss
from ParserAndUtilities.utility import validateData


def als(d, reg, test_num, dataFile, result_save, resultFile, resultMatrixFile, ratingsFile, differenceFile):
    time_whole = time.time()
    sum1 = 0
    sum2 = 0
    sum3 = 0
    result = []
    print("ALS method parsing:")
    ratings = parsers.parseALS(dataFile, 2, ratingsFile)
    print("Total time: %s seconds" % (time.time() - time_whole))

    matrixA = Matrix.fromList(ratings.values)
    if resultFile == 'resultMale.csv' or resultFile == 'resultSrednie.csv':
        resultsValidated = validateData(matrixA)
    # print(resultVerify)
    customers_count = matrixA.retrunSizeX()
    products_count = matrixA.getRankN()
    print("customers amount: ", customers_count)
    print("products amount:", products_count)
    P = np.random.rand(d, products_count)
    U = np.random.rand(d, customers_count)
    index_list = []

    for a in tqdm(range(test_num)):
        index_list.append(a)
        for u in range(customers_count):
            I_u = np.flatnonzero(matrixA[u])
            P_I_u = P[:, I_u]
            P_I_u_T = P_I_u.T
            E = np.eye(d)
            A_u = np.matmul(P_I_u, P_I_u_T) + reg * E
            for i in I_u:
                P[:, i].reshape(d, 1)
            V_u = np.zeros(d).T
            for i in I_u:
                V_u += matrixA[u][i] * P[:, i]
            matrixA_u = Matrix._makeMatrix(np.ndarray.tolist(A_u))
            V_u = V_u.reshape(-1, 1)
            matrixV_u = Matrix._makeMatrix(np.ndarray.tolist(V_u))
            solution = gauss(matrixA_u, matrixV_u, 1)
            pom = Matrix._makeMatrix(np.ndarray.tolist(U))
            pom.setColumn(solution, u)
            U = np.asarray(pom.returnMatrix())
        for p in range(products_count):
            I_p = np.flatnonzero(matrixA[:, p])
            U_I_p = U[:, I_p]
            U_I_p_T = U_I_p.T
            E = np.eye(d)
            B_u = np.matmul(U_I_p, U_I_p_T) + reg * E
            for i in I_p:
                U[:, i].reshape(d, 1)
            W_p = np.zeros(d)
            for i in I_p:
                W_p += matrixA[i, p] * U[:, i]
            matrixB_u = Matrix._makeMatrix(np.ndarray.tolist(B_u))
            W_p = W_p.reshape(-1, 1)
            matrixW_p = Matrix._makeMatrix(np.ndarray.tolist(W_p))
            solution = gauss(matrixB_u, matrixW_p, 1)
            pom = Matrix._makeMatrix(np.ndarray.tolist(P))
            pom.setColumn(solution, p)
            P = np.asarray(pom.returnMatrix())
        matrixU = Matrix._makeMatrix(np.ndarray.tolist(U))
        matrixP = Matrix._makeMatrix(np.ndarray.tolist(P))

        U_T = U.T
        for u in range(matrixA.getRankM()):
            for p in range(matrixA.getRankN()):
                if matrixA[u][p] != 0:
                    sum1 += pow(matrixA[u][p] - (np.dot(U_T[u, :], P[:, p])), 2)
        for u in range(U.shape[1]):
            sum2 += pow(np.linalg.norm(matrixU.getColumn(u)), 2)
        for p in range(P.shape[1]):
            sum3 += pow(np.linalg.norm(matrixP.getColumn(p)), 2)
        target = sum1 + reg * (sum2 + sum3)

        result.append(target)

    if result_save == 0:
        df = pd.DataFrame(data={"index": index_list, "target function": result})
        df.to_csv(resultFile, sep=';', index=False)
    elif result_save == 1:
        matrixU = Matrix._makeMatrix(np.ndarray.tolist(U.T))
        matrixP = Matrix._makeMatrix(np.ndarray.tolist(P))
        RData = matrixU * matrixP
        workbook = xlsxwriter.Workbook(resultMatrixFile)
        worksheet = workbook.add_worksheet()
        row = 0
        for col, data in enumerate(RData):
            worksheet.write_column(row, col, data)
        workbook.close()
    elif result_save == 2:
        df = pd.DataFrame(data={"index": index_list, "target function": result})
        df.to_csv(resultFile, sep=';', index=False)
        matrixU = Matrix._makeMatrix(np.ndarray.tolist(U.T))
        matrixP = Matrix._makeMatrix(np.ndarray.tolist(P))
        RData = matrixU * matrixP
        workbook = xlsxwriter.Workbook(resultMatrixFile)
        worksheet = workbook.add_worksheet()
        row = 0
        for col, data in enumerate(RData):
            worksheet.write_column(row, col, data)
        workbook.close()
        wyniki = []
        print()
        if resultFile == 'resultMale.csv' or resultFile == 'resultSrednie.csv':
            for l in range(len(resultsValidated)):
                wyniki.append(abs(abs(RData.returnItem(resultsValidated[l].__getitem__(0), resultsValidated[l].__getitem__(1))) - abs(resultsValidated[l].__getitem__(2))))
                # print(RData.returnItem(resultsValidated[l].__getitem__(0), resultsValidated[l].__getitem__(1)))
                # print(resultsValidated[l].__getitem__(2))
                # print()
            print(wyniki)


