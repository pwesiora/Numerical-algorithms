def validateProduct(ratings,i,j):
    numerator = 0
    for m in range(ratings.getRankM()):
        # print(ratings.returnItem(m,j))
        if ratings.returnItem(m,j) != 0 and m != i:
            numerator = numerator + 1
            # print("M= ",m,"J= ",j,"N = ",numerator,"I = ", i)
    return numerator

def validateData(ratings):
    Data = []
    for i in range(ratings.getRankM()):
        for j in range(ratings.getRankN()):
            if ratings.returnItem(i, j) != 0:
                if validateProduct(ratings,i,j) != 0:
                    Data.append([i, j, ratings.returnItem(i, j)])
                    ratings.__setitemY__(i, j, 0)
                break
    return Data