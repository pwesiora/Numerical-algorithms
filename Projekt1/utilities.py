import math
import numpy as np

class e_util:
    def __init__(self, x, precision=10 ** -16, use_nprecision=False):
        self.precision = precision
        self.x = x
        self.n = 0
        self.definition_list = []
        self.recursion_list = []
        self.build_in_result = None
        self.use_nprecision = use_nprecision


    def check_precision(self, elem, n):
        if self.use_nprecision == True:
            prec_func = N_precision
            return prec_func(elem, n, self.precision)
        else:
            prec_func = epsilon_precision
            return prec_func(elem, n, self.precision)


    def definition_method(self):
        if not self.definition_list:
            elem = 1
            n = 0
            while not self.check_precision(elem, n):
                self.definition_list.append(elem)
                n += 1
                elem = self.pow(self.x, n) / (math.factorial(n))

            self.n = n

        return self.definition_list

    def rec_method(self):
        if len(self.recursion_list) <= 1:
            elem = 1
            n = 0
            while not self.check_precision(elem, n):
                self.recursion_list.append(elem)
                n += 1
                elem *= self.x / n

            self.n = n
        return self.recursion_list

    def pow(self, x, n):
        result = 1
        for i in range(n):
            result *= x
        return result

    def compute_exp(self, method="def", reverse=False):
        if method == "def":
            series = self.definition_method()
        else:
            series = self.rec_method()
        if reverse:
            series.reverse()
        result = 0
        for s in series:
            result += s
        return result

    def compute_exp_with_n_first_elems(self, n=50, method='def'):
        if method == "def":
            series = self.definition_method()
        else:
            series = self.rec_method()
        result = 0
        for s in series[:n]:
            result += s
        return result

    def compare_math(self):
        if not self.build_in_result:
            self.build_in_result = math.exp(self.x)
        return self.build_in_result


def generate(min_number, max_number, number_of_negatives, number_of_positives):
    positive_increment = max_number / number_of_positives
    negative_increment = abs(min_number / number_of_negatives)

    e_powers = []

    for i in range(-number_of_negatives, 0):
        exponent = i * negative_increment
        e_powers.append(exponent)

    for i in range(number_of_positives):
        exponent = i * positive_increment
        e_powers.append(exponent)

    return e_powers

def get_mean_of_lists(arrays):
    return [np.mean(rg, dtype=np.float64) for rg in arrays]

def get_array_difference(array, array2):
    return np.subtract(array, array2)

def group_result_and_get_relative_error(parts, expected_results, results, use_expected = False):
    expected_results_grouped = [np.mean(i, dtype=np.float64) for i in np.split(np.array(expected_results), parts)]
    relative_errors = []
    for result in results:
        grouped_res = [np.mean(i, dtype=np.float64) for i in np.split(np.array(result), parts)]
        err = np.divide(np.abs(np.subtract(expected_results_grouped, grouped_res)), expected_results_grouped)
        relative_errors.append(err)

    return relative_errors

def epsilon_precision(elem, n, precision):
    return precision > abs(elem)


def N_precision(elem, n, precision):
    return n > precision

