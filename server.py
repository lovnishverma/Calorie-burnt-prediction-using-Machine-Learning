from flask import *
import pandas as pd
from  sklearn.linear_model import LinearRegression 



app = Flask(__name__) 

@app.route('/') 
def index(): 
  return render_template('index.html') 

@app.route('/r') # open the form for result prediction  
def predict(): 
  return  render_template('calorie.html') 

@app.route('/cp', methods = ['POST'] ) 
def caloriesburntpredict(): 
  # get input from user via form
  Age  = eval ( request.form.get ( "Age") )
  Duration=eval(request.form.get("Duration"))
  Heart_Rate  = eval ( request.form.get ( "Heart_Rate") )
  Body_Temp   = eval ( request.form.get ( "Body_Temp") )
  # predict and save the output in result variable
  url   = "cbp.csv"
  df = pd.read_csv(url)
  X = df.drop(['ID','Calories'],axis='columns')
  Y = df["Calories"]
  model = LinearRegression()
  model.fit(X,Y)
  arr=model.predict([[Age,Duration,Heart_Rate,Body_Temp]])
  return  render_template("calorie.html", data=arr[0]) 

if __name__ == '__main__': 
  app.run()