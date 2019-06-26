import csv
import numpy as np
import matplotlib.pyplot as plt
import scipy
import numpy

data = []

with open('cooldown.csv', 'r') as csvFile:
    reader = csv.reader(csvFile,delimiter=";")
    for row in reader:
        distance = float(row[0])
        time = float(row[1])
        data.append([distance, time])

csvFile.close()

data = np.array(data)
x = data[:, 0] # distance
y = data[:, 1] # time
z = x/(y/60.)

plt.plot(x,y, '+')
plt.show()

res = scipy.optimize.curve_fit(lambda t,a,b: a*t**b,  x,  y)

a = res[0][0]
b = res[0][1]
plt.plot(x,y, '+')
plt.plot(x,a*x**(b))
plt.show()

def cooldown(distance):
    return round(2.35*distance**0.536,2)

print("distance P13-4T:", cooldown(13))
print("distance P13-P9:", cooldown(7))
