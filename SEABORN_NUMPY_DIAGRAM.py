import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random as r


def values_1to100(times):
    values = []
    for i in range(1, times+1):
        outcome = r.randint(1, 100)
        values.append(outcome)
    return values


def ecdf(x):
    n = len(x)
    x = np.sort(x)
    y = np.arange(1, n + 1 / n)

    return x, y


sns.set()

data = values_1to100(1000000)
number, percentage_of_number = ecdf(data)

plt.plot(number, percentage_of_number)

plt.xlabel('number')
plt.ylabel('percentage_of_number [ECDF]')

plt.show()