import numpy as np
import matplotlib.pyplot as plt


class GeneralClassifiers(object):
	def __init__(self):
		pass

	def add_data(self,X,Y,num_classes,reg,epochs,alpha,mini_batch_size): 
		#These X and Y are the training sets
		#Dimensions of X are as m x n
		self.X_train = X
		self.Y_train = Y
		self.m = X_train.shape[0]
		self.n = X_train.shape[1]
		self.k = num_classes
		self.reg = reg
		self.epochs = epochs
		self.alpha = alpha
		self.mini_batch_size = mini_batch_size
		StandardizeTrain()
		return

	def InitializePars():
		pass	

	def UpdateReg(self,reg):
		self.reg = reg	
		return 

	def UpdateEpochs(self,epochs):
		self.epochs = epochs
		return

	def UpdateAlpha(self,alpha):
		self.alpha = alpha	
		return

	def UpdataMiniBatchSize(self,mini_batch_size):
		self.mini_batch_size = mini_batch_size

	def StandardizeTrain():
		mean = np.mean(X_train,axis=0)
		X_train = X_train - mean
		var = np.car(X_train,axis=0)
		X_train = X_train/var
		return

	def StandardizeTrain():
		mean = np.mean(X_test,axis=0)
		X_test = X_test - mean
		var = np.car(X_test,axis=0)
		X_test = X_test/var
		return

	def CostFunc():
		pass

	def Gradient():
		pass

	def GradientDescent(start,end):
		pass
			
	def	give_prediction(self,X): 
		#These X and Y are the test sets
		#Returns a prediction of what corresponding X to each element of X the label should be
		self.X_test = X
		StandardizeTest()
		return predict()

	def predict():
		temp = np.dot(X_test,np.transpose(pars))
		return np.argmax(temp,axis=1)	

	def give_prediction_and_accuracy(self,X,Y):	
		#These X and Y are the test sets
		#Returns a prediction of what corresponding X to each element of X the label should be and also
		#analysis of the prediction with respect to true Y
		self.X_test = X
		self.Y_test = Y
		StandardizeTest()
		Y_predict = predict()
		accuracy = find_error(Y_predict)
		return {'prediction' : Y_predict,'accuracy' : accuracy}

	def find_error(prediction):
		return np.count_nonzero(prediction==Y_test)			