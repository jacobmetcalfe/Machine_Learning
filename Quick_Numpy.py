# Machine Learning - A Machine carrying out a task by itself
# Taking out specific features instead of raw data is called feature engineering
# Python can off load into C or Fortran extensions
# Numpy provides support of highly optimized multidimensional arrays
# SciPy uses those arrays to provide a set of fast numerical recipes
# Matplotlib is convent and feature rich library to plot high quality graphs
# import very little of numpy similar to namespace
# [3,2] = 3 rows, 2 columns

import numpy as np

a = np.array(([0, 1, 2, 3, 4, 5]))
print('Starting array')
print(a)
# prints number of dimensions of the array
print('A has this many dimensions')
print(a.ndim)
# prints number of elements per dimension of array
print('A is this shape')
print(a.shape)

# transform array into a two dimensional matrix
# prints array in 3x2 form making it multidimensional
b = a.reshape((3, 2))
print('b reshaped to a is')
print(b)
# number of dimensions
print('b has this many dimensions now')
print(b.ndim)
# prints the shape of b
print('b is this shape')
print(b.shape)
# changes value of row 2 column 1 to 77 of both a and b
b[1][0] = 77
print('This is the new b, row 2 column 0 is now 77')
print(b)
print('a is now 77 as well due to making an exact copy')
print(a)
# reshaping c
print('reshaping c')
c = a.reshape(3, 2).copy()
print(c)
# changing value of c
print('change first value of c to 99')
c[0][0] = 99
print(c)
print('however, since we made a copy instead it does not change the value of a')
print(a)
# c and a are now totally independent copies
d = np.array([1, 2, 3, 4, 5])
print(d)
# doubles all values in the array
print('Doubled all values of the array')
print(d * 2)
print('Squared all the values of the array')
print(d ** 2)
# multiplying your array
print('If you take your actual array and multiple it by two it gives puts two of the same array into one')
doubledArray = [1, 2, 3, 4, 5] * 2
print(doubledArray)

# indexing
print('this is array a')
print(a)
print('gives the index 2, 3, and, 4 of the array')
print(a[np.array([2, 3, 4])])
print('Conditional tests will print the array in boolean form')
print('Will print false when index in a is not greater than 4')
print(a > 4)
print('Will trim the array down to only values that are greater than 4')
print(a[a > 4])
print('This makes any index that is great than 4 equal to 4')
a[a > 4] = 4
print(a)
print('Clips values at both ends of an interval with one function call')
print(a.clip(0, 4))

# Handling non existing values
c = np.array([1, 2, np.NAN, 3, 4])
print('Can do non existing values as well')
print(c)
print('How to find all non existing values in an array')
print(np.isnan(c))
print('How to find all existing values of the array')
print(c[~np.isnan(c)])
print('Find the mean of all of the existing numbers in array c')
print(np.mean(c[~np.isnan(c)]))

# Comparing the runtime
print('Timing numpy compared to regular lists')
import timeit

normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))',
                              number=10000)
naive_np_sec = timeit.timeit(
    'sum(na*na)',
    setup="import numpy as np; na=np.arange(1000)",
    number=10000)
good_np_sec = timeit.timeit(
    'na.dot(na)',
    setup="import numpy as np; na=np.arange(1000)",
    number=10000)
print("Normal Python: %f sec" % normal_py_sec)
print("Naive NumPy: %f sec" % naive_np_sec)
print("Good NumPy: %f sec" % good_np_sec)
print('the results prove that numpy lists are 3.5x faster than regular ones')
print('This comes at a price, numpy arrays can only hold one data type where regular python lists can hold multiple '
      'data types')
a = np.array([1, 2, 3])
print('prints data type of array')
print(a.dtype)