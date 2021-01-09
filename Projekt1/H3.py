import numpy as np
from pylab import rcParams
import matplotlib.pyplot as plt
from tqdm import tqdm
from utilities import generate
from utilities import e_util
from utilities import get_mean_of_lists
from utilities import group_result_and_get_relative_error
import matplotlib.patches as mpatches
import numpy
from collections import deque
rcParams['figure.figsize'] = 15,5
agg_size = 100000

exponents = generate(-10.0, 50.0, 500000, 500000)


counting_from_def_results = []
counting_from_rec_results = []
expected_results = []

for i in tqdm(exponents):
    e = e_util(i, 50, True)
    r = e.compute_exp(method='rec', reverse=False)
    counting_from_rec_results.append(r)

for i in tqdm(exponents):
    e = e_util(i, 50, True)
    d = e.compute_exp(method='def', reverse=False)
    counting_from_def_results.append(d)

for i in exponents:
    e = e_util(i, 50, True)
    expected_results.append(e.compare_math())


relative_errors = group_result_and_get_relative_error(agg_size, expected_results, [counting_from_def_results, counting_from_rec_results])
exponents_array = get_mean_of_lists(np.split(np.array(exponents), agg_size))
diffArray = numpy.subtract(relative_errors[0], relative_errors[1])

#Gathering statistics
a = np.where(diffArray>0, 1, 0)
b = np.where(diffArray<0, 1, 0)
c = np.where(diffArray==0, 1, 0)
result = 0
for i in a:
    result= result + i
print ("x>0" + str(result))

result = 0
for i in b:
    result= result + i
print ("x<0" + str(result))

result = 0
for i in c:
    result= result + i
print ("x=0" + str(result))


colors = np.where(diffArray>0,'g',np.where(diffArray<0, 'r', 'white'))
plt.grid(color='black', linestyle='-', linewidth=0.1)
plt.axvline(linewidth=1.5, color='black')
plt.scatter(exponents_array, diffArray, s=1, c= colors)
p = 1*10**-10
plt.ylim(-p, p)
plt.yscale('symlog', linthreshy=10**-15)


plt.title(r'Różnica obliczania $e^x$ szeregiem Taylora, a obliczania na podstawie poprzedniego elementu')
plt.xlabel('Wykładnik')
plt.ylabel('Błąd względny')
green_patch = mpatches.Patch(color='green', label='Różnica dodatnia')
red_patch = mpatches.Patch(color='red', label='Różnica ujemna')
plt.legend(handles=[green_patch, red_patch])
plt.show()