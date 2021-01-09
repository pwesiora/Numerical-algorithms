import re

import pandas as pd
from tqdm import tqdm

rx_dict = {
    'id_prod': re.compile(r'Id:   (?P<id_prod>.*)'),
    'customer': re.compile(r'cutomer: (?P<customer>\b\S{14}\b).{10}(?P<rating>\d)')
}

def _parseLine(line):

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    return None, None


def parseFile(filepath, item_number):


    data = []
    data_c = []
    data_p = []
    data_r = []
    prod = 0
    licznik = 0
    pbar = tqdm(total=item_number)
    with open(filepath, 'r', encoding="utf8") as file_object:
        line = file_object.readline()
        while line:
            # print(line)
            # at each line check for a match with a regex
            key, match = _parseLine(line)

            # id_prod = -1
            # customer = -1
            # rating = -1
            # extract id_prod name
            if key == 'id_prod':
                id_prod = match.group('id_prod')
                if int(licznik) == item_number:
                    break

            if key == 'customer':
                customer = match.group('customer')
                data_c.append(customer)

            if key == 'customer':
                rating = match.group('rating')
                data_r.append(rating)
                data_p.append(id_prod)
                if id_prod != prod:
                    prod = id_prod
                    licznik = licznik + 1
                    pbar.update(1)

            line = file_object.readline()
            dict = {'id_customer': data_c, 'id_prod': data_p, 'rating': data_r}
            data = pd.DataFrame(dict)
            # data = data.sort_values(by=['id_customer'])
    pbar.close()
    return data

#Wymaga dane w pliku .csv (dataToParse)
#metoda parsing przeprowadza parsowanie za pomocą biblioteki Pandas zwracając dane i zapisując je do ratingsFile
def parseALS(dataToParse, minAmountOfRatings, ratingsFile):
    data_read = pd.read_csv(dataToParse, sep=';')
    ratings = pd.pivot_table(data_read, values=['rating'],
                             columns=['id_prod'], index=['id_customer'],
                             aggfunc='first', fill_value=0)
    ratings["sum_0"] = ratings.apply(lambda row: sum(row[0:ratings.shape[1]] == 0), axis=1)

    ratings = ratings.drop(ratings[ratings['sum_0'] >= ratings.shape[1] - minAmountOfRatings].index)
    ratings = ratings.drop("sum_0", axis=1)

    ratings = ratings.loc[:, (ratings != 0).any(axis=0)]
    ratings.to_csv(ratingsFile, sep=';', index=False, header=False)
    return ratings