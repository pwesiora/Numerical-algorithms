from utilities import generate
from utilities import e_util
from utilities import get_mean_of_lists
#from utilities import get_array_difference
from utilities import group_result_and_get_relative_error
import numpy
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
from tqdm import tqdm

limit = 4*10**-15
rcParams['figure.figsize'] = 15 ,5
agg_size = 100000


exponents = generate(-3.0, 5.0, 50000, 50000)

summing_from_start_results = []
summing_from_end_results = []
expected = []

for i in tqdm(exponents):
    e = e_util(i, 10**-18)
    v1 = e.compute_exp(method='def', reverse=False)
    summing_from_start_results.append(v1)

for i in tqdm(exponents):
    e = e_util(i, 10**-18)
    v2 = e.compute_exp(method='def', reverse=True)
    summing_from_end_results.append(v2)

for i in exponents:
    series = e_util(i)
    expected.append(series.compare_math())


exponents_grouped = get_mean_of_lists(np.split(numpy.array(exponents), agg_size))
relative_errors = group_result_and_get_relative_error(agg_size, expected, [summing_from_start_results, summing_from_end_results])
diffArray = numpy.subtract(relative_errors[0], relative_errors[1])
colors = np.where(diffArray>0,'g',np.where(diffArray<0, 'r', 'white'))
plt.scatter(exponents_grouped, (diffArray+diffArray), s=1, label='Sumowanie od początku', c=colors)

plt.ylim(-limit, limit)
plt.title(r'$e^x$ oblicznony szeregiem Taylora')
plt.xlabel('Wykładnik')
plt.ylabel('Różnica błędu względnego')
plt.grid(color='b', linestyle='-', linewidth=0.1)
plt.axhline(linewidth=1.5, color='black')
green_patch = mpatches.Patch(color='green', label='Różnica dodatnia')
red_patch = mpatches.Patch(color='red', label='Różnica ujemna')
plt.legend(handles=[green_patch, red_patch])
plt.show()