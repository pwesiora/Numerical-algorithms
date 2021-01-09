import numpy as np
from pylab import rcParams
import matplotlib.pyplot as plt
from tqdm import tqdm
from utilities import generate
from utilities import e_util
from utilities import get_mean_of_lists
from utilities import group_result_and_get_relative_error
#from collections import deque


exponents = generate(-10.0, 50.0, 200000, 800000)
results1 = []
results2 = []
results3 = []
results4 = []
expected = []

for i in tqdm(exponents):
    e = e_util(i, 10, True)
    rp1 = e.compute_exp(method='rec', reverse=False)
    results1.append(rp1)

for i in tqdm(exponents):
    e = e_util(i, 20, True)
    rp2 = e.compute_exp(method='rec', reverse=False)
    results2.append(rp2)

for i in tqdm(exponents):
    e = e_util(i, 50, True)
    rp3 = e.compute_exp(method='rec', reverse=False)
    results3.append(rp3)

for i in tqdm(exponents):
    e = e_util(i, 500, True)
    rp4 = e.compute_exp(method='rec', reverse=False)
    results4.append(rp4)

for i in exponents:
    series = e_util(i)
    expected.append(series.compare_math())



agg_size = 100000
exponents_array = get_mean_of_lists(np.split(np.array(exponents), agg_size))
errors = group_result_and_get_relative_error(agg_size, expected, [results1, results2, results3, results4])
rcParams['figure.figsize'] = 15 ,5

plt.grid(color='black', linestyle='-', linewidth=0.1)
plt.axvline(linewidth=1.5, color='black') #adds thick red line @ x=0
#plt.axhline(linewidth=5.5, color='black')  #adds thick red line @ y=0)
plt.scatter(exponents_array, errors[0], s=1, label=f'N = {10}')
plt.scatter(exponents_array, errors[1], s=1, label=f'N = {20}')
plt.scatter(exponents_array, errors[2], s=1, label=f'N = {50}')
plt.scatter(exponents_array, errors[3], s=1, label=f'N = {500}')
plt.yscale('symlog', linthreshy=10**-16)
plt.ylim(0)
plt.title(r'$e^x$ oblicznony szeregiem Taylora o N składnikach')
plt.xlabel('Wykładnik')
plt.ylabel('Błąd względny')
plt.legend()
plt.show()