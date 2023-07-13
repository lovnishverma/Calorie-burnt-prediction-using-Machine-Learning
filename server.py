from flask import *
import pandas as pd
import numpy as np
from  sklearn.linear_model import LinearRegression 


app = Flask(__name__) 

@app.route('/') 
def first(): 
  return render_template('index.html') 

@app.route('/r') # open the form for result prediction  
def second(): 
  return  render_template('calorie.html') 

@app.route('/hp', methods = ['POST'] ) 
def housepricepredict(): 
  location='Whitefield'
  sqft  = eval ( request.form.get ( "area") )
  bath  = eval ( request.form.get ( "bath") )
  bhk   = eval ( request.form.get ( "bhk") )
  # predict and save the output in result variable
  url   = "bhp.csv"
  df = pd.read_csv(url)
  X = df.drop(['price'],axis='columns')
  y = df["price"]
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  model.fit(X,y)
  loc_index = np.where(X.columns==location)[0][0]

  x = np.zeros(len(X.columns))
  x[0] = sqft
  x[1] = bath
  x[2] = bhk
  if loc_index >= 0:
      x[loc_index] = 1
        
  hp = model.predict([x])[0]
  return " House price predicted as (in lakhs ) "  + str(hp) 


if __name__ == '__main__': 
  app.run()