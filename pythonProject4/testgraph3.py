import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Mamdouh make sure that these are importing corectly as it wont run if you dont import the file from the correct location
import logistic_regressionforgraph as logic
from utils import MyUtils

#from code_misc.utils import MyUtils

#Mamdouh make sure that the file paths for these csv's are working correctly for where you place this file.
#however it may run just fine.
df_X_train = pd.read_csv('X_train.csv')
df_y_train = pd.read_csv('y_train.csv')
df_X_test = pd.read_csv('X_test.csv')
df_y_test = pd.read_csv('y_test.csv')

X_train = df_X_train.to_numpy()
X_test = df_X_test.to_numpy()
n_train = X_train.shape[0]

X_all = MyUtils.normalize_neg1_pos1(np.concatenate((X_train, X_test), axis=0))
X_train = X_all[:n_train]
X_test = X_all[n_train:]
y_train = df_y_train.to_numpy()
y_test = df_y_test.to_numpy()

train_error = np.array([])
test_error = np.array([])
runs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

#Mamdouh the way this works is that it runs once with default values and 3 times per variable that i change
#i would suggest putting in your own values besides what i have so it doesnt look copied
#also i didnt put this in a for loop to make it easier to edit

#When you run this it WILL take a while to run.
log = logic.LogisticRegression()
#Default
log.fit(X_train, y_train, lam=0, eta=0.01, iterations=1000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 1 results')
print(train_error)
print(test_error)

#degree  2, 3,
log.fit(X_train, y_train, lam=0, eta=0.01, iterations=1000, SGD=True, mini_batch_size=1, degree=2)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 2 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0, eta=0.01, iterations=1000, SGD=True, mini_batch_size=1, degree=3)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 3 results')
print(train_error)
print(test_error)


#lambda 0.1, 0.01, 0.001
log.fit(X_train, y_train, lam=0.1, eta=0.01, iterations=1000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 4 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0.01, eta=0.01, iterations=1000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 5 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0.001, eta=0.01, iterations=1000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 6 results')
print(train_error)
print(test_error)
#eta 0.1, 0.001, 0.0001
log.fit(X_train, y_train, lam = 0, eta = 0.1, iterations=1000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 7 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0, eta=0.001, iterations=1000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 8 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0, eta=0.0001, iterations=1000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 9 results')
print(train_error)
print(test_error)
#iterations 10000, 100000, 1000000
log.fit(X_train, y_train, lam=0, eta=0.01, iterations=10000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 10 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0, eta=0.01, iterations=100000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 11 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0, eta=0.01, iterations=1000000, SGD=True, mini_batch_size=1, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 12 results')
print(train_error)
print(test_error)

#mini batch size 2 3 4
log.fit(X_train, y_train, lam=0, eta=0.01, iterations=1000, SGD=True, mini_batch_size=2, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 13 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0, eta=0.01, iterations=1000, SGD=True, mini_batch_size=3, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 14 results')
print(train_error)
print(test_error)

log.fit(X_train, y_train, lam=0, eta=0.01, iterations=1000, SGD=True, mini_batch_size=4, degree=1)
train_error = np.append(train_error, (log.error(X_train, y_train)))
test_error = np.append(test_error, (log.error(X_test, y_test)))
print('run 15 results')
print(train_error)
print(test_error)

plt.scatter(runs, train_error, marker='.')
plt.xlabel('Runs')
plt.ylabel('MSE')

plt.scatter(runs, test_error, marker='.')
plt.xlabel('Runs')
plt.ylabel('MSE')
plt.show()
print('success')

