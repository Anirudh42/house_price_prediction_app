from flask import Flask, render_template, request, redirect, url_for
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

with open("./ml_model/linear_reg_model.model","rb") as f:
    model = pickle.load(f)
def process_data(data):
    curr_data = pd.DataFrame(data,columns=['LotArea','BldgType','RoofMatl','TotalBsmtSF'])
    curr_data['BldgType'] = curr_data['BldgType'].astype('category').cat.codes
    curr_data['RoofMatl'] = curr_data['RoofMatl'].astype('category').cat.codes
    return curr_data

app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def welcome():
    if request.method=='POST':
        #Get the username from form
        return #Change or redirect your URL to /predict
    else:
        return render_template("index.html")

@app.route("/predict/<usr>",methods=['GET','POST'])
def predict(usr):
    user = usr
    if request.method=='POST':
        #Fetch all data from HTML form
        #Process data
        #Use mode to predict
        return render_template("predict.html",content=user,prediction="House Price = $ " + str(round(price[0],2)))
    else:
        return render_template("predict.html",content=user)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)