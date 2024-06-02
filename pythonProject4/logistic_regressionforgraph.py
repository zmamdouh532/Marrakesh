########## >>>>>> Put your full name and 6-digit EWU ID here.
import math
# Implementation of the logistic regression with L2 regularization and supports stachastic gradient descent


import sys

import numpy as np

from utils import MyUtils
sys.path.append("..")


class LogisticRegression:
    def __init__(self):

        self.w = None
        self.degree = 1



    def fit(self, X, y, lam = 0, eta = 0.01, iterations = 1000, SGD = False, mini_batch_size = 1, degree = 1):
        """ Save the passed-in degree of the Z space in `self.degree`.
            Compute the fitting weight vector and save it `in self.w`.

            Parameters:
                X: n x d matrix of samples; every sample has d features, excluding the bias feature.
                y: n x 1 vector of lables. Every label is +1 or -1.
                lam: the L2 parameter for regularization
                eta: the learning rate used in gradient descent
                iterations: the number of iterations used in GD/SGD. Each iteration is one epoch if batch GD is used.
                SGD: True - use SGD; False: use batch GD
                mini_batch_size: the size of each mini batch size, if SGD is True.
                degree: the degree of the Z space
        """

        # remove the pass statement and fill in the code.

        self.degree = degree
        X = MyUtils.z_transform(X, degree=self.degree)

        n, d = X.shape
        X = np.insert(X, 0, 1, axis=1)
        #np.random.seed()
        self.w = np.zeros((d+1, 1))



        #Stochastic Gradient Descent
        if (SGD):
            num_of_batches = math.ceil(n / mini_batch_size)
            for i in range(iterations):
                batch_num = i % num_of_batches
                start = batch_num * mini_batch_size
                end = (batch_num + 1) * mini_batch_size
                X_prime = X[start : end]
                Y_prime = y[start : end]
                n_prime, d_prime = X_prime.shape

                s = Y_prime * (X_prime @ self.w)
                temp = 1 - 2 * lam * eta/n_prime
                self.w = temp * self.w + (eta / n_prime) * (X_prime.T @ (Y_prime * LogisticRegression._v_sigmoid(-s)))
        #Normal Gradient Descent
        else:
            while iterations > 0:
                s = y * (X @ self.w)
                self.w = (1.0 - (2.0 * lam*eta)/n) * self.w + (eta/n * (X.T @ (y * LogisticRegression._v_sigmoid(-s))))
                iterations -= 1



    def predict(self, X):
        """ parameters:
                X: n x d matrix; n samples; each has d features, excluding the bias feature.
            return:
                n x 1 matrix: each row is the probability of each sample being positive.
        """


        X = MyUtils.z_transform(X, degree=self.degree)
        X = np.insert(X, 0, 1, axis=1)
        n, d = X.shape

        pred = X @ self.w




        return LogisticRegression._v_sigmoid(pred)


    def error(self, X, y):
        """ parameters:
                X: n x d matrix; n samples; each has d features, excluding the bias feature.
                y: n x 1 matrix; each row is a labels of +1 or -1.
            return:
                The number of misclassified samples.
                Every sample whose sigmoid value > 0.5 is given a +1 label; otherwise, a -1 label.
        """


        X = MyUtils.z_transform(X, degree=self.degree)
        X = np.insert(X, 0, 1, axis=1)
        #a = X @ self.w
        #np.sign((np.sign(a)-0.1)) !=y
        pred = np.sign(X @ self.w)
        pred = np.sign(pred- 0.1)
        MSE = np.sum(pred !=y)
        return MSE


    def _v_sigmoid(s):
        """
            vectorized sigmoid function

            s: n x 1 matrix. Each element is real number represents a signal.
            return: n x 1 matrix. Each element is the sigmoid function value of the corresponding signal.
        """
            

        #return Z
        vs = np.vectorize(LogisticRegression._sigmoid)
        return vs(s)
    
    
        
    def _sigmoid(s):
        """ s: a real number
            return: the sigmoid function value of the input signal s
            :rtype: object
        """

        # remove the pass statement and fill in the code.


        return 1.0 / (1.0 + math.exp(s * (-1.0)))

    
