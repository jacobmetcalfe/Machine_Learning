import scipy as sp
import matplotlib.pyplot as plt

# hypothetical web start-up company When do we have to request additional servers in the cloud to serve all the
# incoming requests successfully without paying for unused ones

# Reading in the data
# Says get from the text and the delimiter means that the data will be a tab away
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")

# Gets first ten pieces of data so we know it's grabbing something
print(data[:10])

# Prints what we need to limit the data into
print(data.shape)
print('The data is 743 rows and 2 columns')

print('\n Cleaning the Data')
# Pre processing and cleaning the data
# we will separate this into two vectors

# First Vector = Hours (Every row of the first column)
x = data[:, 0]

# Second Vector = web hits (Every row of the second column)
y = data[:, 1]

print('This is how many values of web hits are nan')
print(sp.sum(sp.isnan(y)))
print('We are missing 8/743 entries, so we can remove them')

# Sp.isnan returns an array of Booleans indicating whether an entry is a number or not
# We are negating those numbers so that it is the array minus the values in column 2 that are nan
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

# Visualizing our data
# Plots points with size = 10
plt.scatter(x, y, s=10)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hour")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)

# Drawing a grid
plt.grid(True, linestyle='-', color='.75')

# Choosing the right model and learning algorithm
print('Steps to choose the right model and learning algorithm')
print('-------------------------------------------------------')
print('1. Find the real model behind the noisy data points')
print('2, Following this, use the model to extrapolate into the future to find the point in time where our '
      'infrastructure has to be extended')


# Before building
# Simple theoretical approximations of complex reality
# There is going to be approximation error
def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


# Starting with a simple straight line Putting this line, in the  into the chart so that it results in the smallest
# approximation error polyfit() does exactly that. Given data x and y and the desired order of the polynomial (
# Straight line has an order of 1), it finds the model function that minimizes the error function defined earlier
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

# Polyfit() returns the parameters of the fitted model function, fp1
# By setting full = True we get extra information
print("Model parameters: %s" % fp1)
print('So your equation is 2.59619213x + 989.02487106')
print('Error of Approximation')
print(residuals)

# poly1d() is then used to create a model function from the model parameters
f1 = sp.poly1d(fp1)
print(error(f1, x, y))

# x values
fx = sp.linspace(0, x[-1], 1000)  # generate X-values for plotting
plt.plot(fx, f1(fx), linewidth=4, c='green')
plt.legend(["d=%i" % f1.order, "Number of Hits / Time"], loc="upper left")
plt.show()

# Although the graph doesn't look bad, it's not great
# How bad actually is the error 317,389,767.34?
# Number doesn't mean much, however we can compare it to other graphs and find the lower error
