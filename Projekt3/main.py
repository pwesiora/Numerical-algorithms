#Autor: Piotr Węsiora
#13.01.2020

from ParserAndUtilities.parsers import parseFile
from als import als

if __name__ == '__main__':


    # Metody testowe zwracają wyniki do następujących plików (nazwy narzucone odgórnie):
    #   - pliki result.csv z wynikami funkcji celu po każdej iteracji ALS
    #   - pliki restltMatrix.xlsx z wynikowymi macierzami R = P*U (RData)
    #   - pliki ratings wykorzystywane

    def testRunAlsS(d, lambdaALS, testNum):
        dataFile = 'PSmall.csv'
        als(d, lambdaALS, testNum, dataFile, 2, 'resultS.csv', 'matrixR_S.xlsx', 'ratingsS.csv', 'differenceS.xlsx')

    def testRunAlsM(d, lambdaALS, testNum):
        dataFile = 'PMedium.csv'
        als(d, lambdaALS, testNum, dataFile, 2, 'resultMedium.csv', 'matrixR_Medium.xlsx', 'ratingsMedium.csv',
            'differenceS.xlsx')


    def testRunAlsB(d, lambdaALS, testNum):
        dataFile = 'PBig.csv'
        als(d, lambdaALS, testNum, dataFile, 2, 'resultBig.csv', 'matrixR_Big.xlsx', 'ratingsBig.csv',
            'differenceBig.xlsx')

    def testMultipleLambD(testNum, max_lambda, max_d):
        dataFile = 'PSmall.csv'
        for reg in (0.1, max_lambda, 0.1):
            for d in range(2, max_d, 1):
                result1 = "res1_cmp" + str(d) + str(int(reg)) + ".csv"
                result2 = "res2_cmp" + str(d) + str(int(reg)) + ".xlsx"
                als(d, reg, testNum, dataFile, 2, result1, result2, 'ratingsM.csv',
                    'differenceM.xlsx')

    # parsed = parseFile('amazon-meta.txt', 100)
    # parsed.to_csv('PSmall.csv', sep=';', index=False)
    # parsed = parseFile('amazon-meta.txt', 1000)
    # parsed.to_csv('PMedium.csv', sep=';', index=False)
    # parsed = parseFile('amazon-meta.txt', 10000)
    # parsed.to_csv('PBig.csv', sep=';', index=False)

    # testRunAlsS/M/B(d, lambdaALS, testNum)
    # d, lambdaALS - parametry z pseudokodu ALS
    # testNum - ilość obrotów pętli algorytmu ALS

    testRunAlsS(2, 0.1, 300)
    testRunAlsM(3, 0.01, 100)
    testRunAlsB(3, 0.01, 20)
    testMultipleLambD(10, 0.2, 3)

