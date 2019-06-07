import csv
import numpy as np
from sklearn.linear_model import LinearRegression

data = []

with open('estimator.csv', 'r') as csvFile:
    reader = csv.reader(csvFile,delimiter=";")
    for row in reader:
        attack = float(row[0])
        defense = float(row[1])
        player = float(row[2])
        weaknesscoeff = float(row[3])
        if weaknesscoeff != 1.:
            data.append([attack, defense, player])

csvFile.close()

data = np.array(data)
x = data[:, :2]#np.array([data[:, 1]]).transpose()#data[:, :2]#
y = data[:, 2]

model = LinearRegression(fit_intercept=False)
model.fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)


def estimator(attack, defense):
    return attack/413. + defense/83.-0.34

for i in range(len(data)):
    attack = data[i,0]
    defense = data[i,1]
    print(attack, defense, estimator(attack, defense), data[i,2])

