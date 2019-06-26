import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import scipy
import numpy
import mpl_toolkits.mplot3d.axes3d as p3

data = []

with open('estimator.csv', 'r') as csvFile:
    reader = csv.reader(csvFile,delimiter=";")
    for row in reader:
        attack = float(row[0])
        defense = float(row[1])
        player = float(row[2])
        weaknesscoeff = float(row[3])
        if weaknesscoeff == 1.:
            data.append([attack, defense, player])

csvFile.close()
data = np.array(data)


# One dimension
x = np.array([data[:, 1]]).transpose()
y = data[:, 2]

model = LinearRegression(fit_intercept=False)
model.fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('slope:', model.coef_)

plt.plot(x,y, '+')
plt.plot(x,1/80.*x)
plt.show()

# Two dimensions
x = data[:, :2]
y = data[:, 2]

model = LinearRegression(fit_intercept=False)
model.fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

fig=plt.figure()
ax = p3.Axes3D(fig)
ax.scatter(data[:,0], data[:,1], data[:,2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.add_axes(ax)

Y=numpy.linspace(0,300,3)
X,Y=numpy.meshgrid(Y,Y)
Z=Y/585. + X/88.- 0.34
surf=plt.gca(projection='3d').plot_surface(X,Y,Z.T,rstride=1,cstride=1, linewidth=0,antialiased=False)
plt.show()

x1 = data[:, 0]
x2 = data[:, 1]
plt.plot(x2,y, '+r')
plt.plot(x2,x1/585. + x2/88.,'+g')
plt.show()



def estimator(attack, defense):
    return attack/585. + defense/88.

for i in range(len(data)):
    attack = data[i,0]
    defense = data[i,1]
    print(attack, defense, estimator(attack, defense), data[i,2])

