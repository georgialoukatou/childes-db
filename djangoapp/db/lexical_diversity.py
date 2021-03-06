# Copyright 2017 John Frens
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Adapted 3 April 2018 by Stephan Meylan: using more robust math and scipy libraries; works with Python 2


# removed punctuation -> null translator for compatibility with Python 2 (used string methods from Py 3 only)

import math
import scipy.special

import warnings
warnings.filterwarnings("error")

# MTLD internal implementation
def mtld_calc(word_array, ttr_threshold):
    current_ttr = 1.0
    token_count = 0
    type_count = 0
    types = set()
    factors = 0.0

    for token_obj in word_array:
        token = token_obj.gloss
        token = token.lower()  # trim punctuation, make lowercase
        token_count += 1
        if token not in types:
            type_count += 1
            types.add(token)
        current_ttr = type_count / token_count
        if current_ttr <= ttr_threshold:
            factors += 1
            token_count = 0
            type_count = 0
            types = set()
            current_ttr = 1.0

    excess = 1.0 - current_ttr
    excess_val = 1.0 - ttr_threshold
    factors += excess / excess_val
    if factors != 0:
        return len(word_array) / factors
    return -1


# MTLD implementation
def mtld(word_array, ttr_threshold=0.72):
    if isinstance(word_array, str):
        return 7777777
        #raise ValueError("Input should be a list of strings, rather than a string. Try using string.split()")
    if len(word_array) < 50:
        return None
    result = (mtld_calc(word_array, ttr_threshold) + mtld_calc(word_array[::-1], ttr_threshold)) / 2
    if math.isnan(result):
        return 0
    elif result:
        return round(result, 3)
    else:
        return result


# hypergeometric probability: the probability that an n-trial hypergeometric experiment results
#  in exactly x successes, when the population consists of N items, k of which are classified as successes.
#  (here, population = N, population_successes = k, sample = n, sample_successes = x)
#  h(x; N, n, k) = [ kCx ] * [ N-kCn-x ] / [ NCn ]
def hypergeometric(population, population_successes, sample, sample_successes):
    return (scipy.special.comb(population_successes, sample_successes) *
            scipy.special.comb(population - population_successes, sample - sample_successes)) / \
           scipy.special.comb(population, sample)

# x! = x(x-1)(x-2)...(1)
# def factorial(x):
#     if x <= 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
# # n choose r = n(n-1)(n-2)...(n-r+1)/(r!)
# def combination(n, r):
#     r_fact = factorial(r)
#     numerator = 1.0
#     num = n-r+1.0
#     while num < n+1.0:
#         numerator *= num
#         num += 1.0
#     return numerator / r_fact


# HD-D implementation
def hdd(word_array, sample_size=42.0):
    if isinstance(word_array, str):
        return 7777777
        #raise ValueError("Input should be a list of strings, rather than a string. Try using string.split()")
    if len(word_array) < 50:
        return None

    # Create a dictionary of counts for each type
    type_counts = {}
    for token_obj in word_array:
        token = token_obj.gloss
        token = token.lower()  # trim punctuation, make lowercase
        if token in type_counts:
            type_counts[token] += 1.0
        else:
            type_counts[token] = 1.0
    # Sum the contribution of each token - "If the sample size is 42, the mean contribution of any given
    #  type is 1/42 multiplied by the percentage of combinations in which the type would be found." (McCarthy & Jarvis 2010)
    hdd_value = 0.0
    for token_type in type_counts.keys():

        try:
            hgeo = hypergeometric(len(word_array), sample_size, type_counts[token_type], 0.0)
        except RuntimeWarning:
            return 0

        contribution = (1.0 - hgeo) / sample_size
        hdd_value += contribution

    if math.isnan(hdd_value):
        return 0
    elif hdd_value:
        return round(hdd_value, 3)
    else:
        return hdd_value
