from flask import *
import pandas as pd
import numpy as np
from  sklearn.linear_model import LinearRegression 


app = Flask(__name__) 

@app.route('/') 
def index(): 
  return render_template('index.html') 

@app.route('/r') # open the form for result prediction  
def predict(): 
  return  render_template('calorie') 

@app.route('/cp', methods = ['POST'] ) 
def caloriesburntpredict(): 
  location='Whitefield'
  Age  = eval ( request.form.get ( "Age") )
  Heart_Rate  = eval ( request.form.get ( "Heart_Rate") )
  Body_Temp   = eval ( request.form.get ( "Body_Temp") )
  # predict and save the output in result variable
  url   = "cbp.csv"
  df = pd.read_csv(url)
  X = df.drop(['ID','Calories'],axis='columns')
  Y = df["Calories"]
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  model.fit(X,Y)
  loc_index = np.where(X.columns==location)[0][0]

  x = np.zeros(len(X.columns))
  x[0] = Age
  x[1] = Duration
  x[2] = Heart_Rate
  x[3] = Body_Temp
  if loc_index >= 0:
      x[loc_index] = 1
        
  hp = model.predict([x])[0]
  return " Calories Burnt "  + str(hp) 


if __name__ == '__main__': 
  app.run()