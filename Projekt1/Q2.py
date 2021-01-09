import numpy as np
from pylab import rcParams
import matplotlib.pyplot as plt
from tqdm import tqdm
from utilities import generate
from utilities import e_util
from utilities import get_mean_of_lists

exponents = generate(-10.0, 50.0, 3000, 7000)

PRECISION = 10**-6

number_of_elements = []

for i in tqdm(exponents):
    e = e_util(i, PRECISION)
    e.compute_exp(method='rec')
    number_of_elements.append(e.n)

rcParams['figure.figsize'] = 15 ,5
agg_size = 1000

number_of_elements_grouped = get_mean_of_lists(np.split(np.array(number_of_elements), agg_size))
exponents_array = get_mean_of_lists(np.split(np.array(exponents), agg_size))

plt.grid(color='black', linestyle='-', linewidth=0.1)
plt.axvline(linewidth=1.5, color='black')
plt.scatter(exponents_array, number_of_elements_grouped, s=1, label='Liczba składników')
plt.yscale('symlog')
plt.title(r'$e^x$ oblicznony z precyzją ' + r'$10^{-6}$')
plt.xlabel('Wykładnik')
plt.legend()
plt.show()