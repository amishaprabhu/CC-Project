from flask import Flask,render_template,redirect,url_for,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# creating a classifier using sklearn
from sklearn.linear_model import LogisticRegression

application=Flask(__name__)
application.config['SECRET_KEY']='3483dd03f2cb409aba821cd2a27c64b3'

def calulate(lst):
	dataset = pd.read_csv('newdata.csv')
	# selecting the features and labels
	X = dataset.iloc[:, :-1].values
	Y = dataset.iloc[:, -1].values
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.2)
	clf = LogisticRegression(random_state=0, solver='lbfgs',max_iter=1000).fit(X_train,Y_train)
	# printing the acc
	clf.score(X_test, Y_test)
	# predicting for random value
	Y_pred=clf.predict([[lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6]]])
	return Y_pred[0]


@application.route('/test')
def home():
	return render_template('index.html')

@application.route('/')
def aboutus():
	return render_template('/aboutus.html')

@application.route('/result',methods=['GET','POST'])
def result():
	lst=[int(request.form['age']),int(request.form['gender']),int(request.form['stream']),int(request.form['internship'])
	,float(request.form['cgpa']),0,int(request.form['backlog'])]
	result=calulate(lst)
	if result==1:
		string="Congratulation! you can able to get the placement based on your academic data"
	else:
		string="Sorry to say but you need to improve yourself"

	return render_template('result.html',mssg=string)

if __name__ == '__main__':
	application.run(debug=True)
