########## >>>>>> Mamdouh Zayed


# Implementation of the linear regression with L2 regularization.
# It supports the closed-form method and the gradient-descent based method.


import numpy as np
import math
import sys

sys.path.append("..")

from utils import MyUtils


class LinearRegression:
    def __init__(self):
        self.w = None  # The (d+1) x 1 numpy array weight matrix
        self.degree = 1

    def fit(self, X, y, CF=True, lam=0, eta=0.01, epochs=1000, degree=1):
        """ Find the fitting weight vector and save it in self.w.

            parameters:
                X: n x d matrix of samples, n samples, each has d features, excluding the bias feature
                y: n x 1 matrix of lables
                CF: True - use the closed-form method. False - use the gradient descent based method
                lam: the ridge regression parameter for regularization
                eta: the learning rate used in gradient descent
                epochs: the maximum epochs used in gradient descent
                degree: the degree of the Z-space
        """
        self.degree = degree
        X = MyUtils.z_transform(X, degree=self.degree)

        if CF:
            self._fit_cf(X, y, lam)
        else:
            self._fit_gd(X, y, lam, eta, epochs)

    def _fit_cf(self, X, y, lam=0):
        """ Compute the weight vector using the clsoed-form method.
            Save the result in self.w

            X: n x d matrix, n samples, each has d features, excluding the bias feature
            y: n x 1 matrix of labels. Each element is the label of each sample.
        """

        ## Delete the `pass` statement below.
        ## Enter your code here that implements the closed-form method for
        ## linear regression
        ##X = np.c_[np.ones((X.shape[0], 1)), X]
        ##I = np.identity(X.shape[1])
        ##I[0, 0] = 0
        ##self.w = np.linalg.pinv(X.T @ X + lam * I)@ (X.T)@(y)
        ##d = X.shape[1]
        n, d = X.shape
        X = np.insert(X, 0, 1, axis=1)
        self.w = (np.linalg.pinv(X.T @ X + lam * np.identity(d + 1))) @ (X.T @ y)

    def _fit_gd(self, X, y, lam=0, eta=0.01, epochs=1000):
        ''' Compute the weight vector using the gradient desecent based method.
            Save the result in self.w

            X: n x d matrix, n samples, each has d features, excluding the bias feature
            y: n x 1 matrix of labels. Each element is the label of each sample.
        '''
        ## Enter your code here that implements the gradient descent based method
        ## for linear regression
        ##def regularized_linear_regression(X, y, lambda_value, eta, max_iterations):
        np.random.seed()
        n, d = X.shape
        self.w = np.array([[0], ] * (d + 1))
        self.w = np.random.rand(d + 1, 1)
        self.w = (self.w * 2 - 1) / math.sqrt(d)
        X = np.insert(X, 0, 1, axis=1)
        a = X.T @ X + lam * np.identity(d + 1)
        a = np.identity(d + 1) - a * 2 * eta / n
        b = X.T @ y * 2 * eta / n
        while (epochs > 0):
            self.w = a @ self.w + b
            epochs -= 1
        ##self.MSE.append(self._error(X,y))

    def predict(self, X):
        ''' parameter:
                X: n x d matrix, the n samples, each has d features, excluding the bias feature
            return:
                n x 1 matrix, each matrix element is the regression value of each sample
        '''

        ## Delete the `pass` statement below.

        ## Enter your code here that produces the label vector for the given samples saved
        ## in the matrix X. Make sure your predication is calculated at the same Z
        ## space where you trained your model. Make sure X has been normalized via the same
        ## normalization used by the training process.
        X = MyUtils.z_transform(X, self.degree)
        X = np.insert(X, 0, 1, axis=1)
        ##y_pred = self.predict(X)

        return X @ self.w

    def error(self, X, y):
        ''' parameters:
                X: n x d matrix of future samples
                y: n x 1 matrix of labels
            return:
                the MSE for this test set (X,y) using the trained model
        '''

        ## Delete the `pass` statement below.

        ## Enter your code here that calculates the MSE between your predicted
        ## label vector and the given label vector y, for the sample set saved in matraix X
        ## Make sure your predication is calculated at the same Z space where you trained your model.
        ## Make sure X has been normalized via the same normalization used by the training process.
        X = MyUtils.z_transform(X, degree=self.degree)
        X = np.insert(X, 0, 1, axis=1)

        temp = X @ self.w - y
        n, d = X.shape

        return np.sum((temp * temp) / n)
        # X = MyUtils.z_transform(X, self.degree)
        # X = np.insert(X, 0, 1, axis=1)
        # y_pred = np.dot(X,self.degree)
        # return np.mean((y_pred - y) ** 2)
        ##X = MyUtils.z_transform(X, degree=self.degree)
        ##X = np.insert(X, 0, 1, axis=0)
        ##return self.w.T @ X


