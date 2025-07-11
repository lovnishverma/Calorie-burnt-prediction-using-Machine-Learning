from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/')
def index():
    # This function renders the index.html template when the root URL is accessed.
    return render_template('index.html')

@app.route('/r')
def predict():
    # This function renders the calorie.html template when the '/r' URL is accessed.
    # It opens the form for result prediction.
    return render_template('calorie.html')

@app.route('/cp', methods=['POST'])
def caloriesburntpredict():
    # This function is called when the form in calorie.html is submitted.
    # It receives the input from the user via the form.

    # Get input values from the form and convert them to appropriate data types.
    Age = eval(request.form.get("Age"))
    Duration = eval(request.form.get("Duration"))
    Heart_Rate = eval(request.form.get("Heart_Rate"))
    Body_Temp = eval(request.form.get("Body_Temp"))

    # Load the CSV file containing the data needed for the prediction.
    url = "cbp.csv"
    df = pd.read_csv(url)
    X = df.drop(['ID', 'Calories'], axis='columns')
    Y = df["Calories"]

    # Create a LinearRegression model and fit it to the data.
    model = LinearRegression()
    model.fit(X, Y)

    # Predict the result for the input values and store it in the 'arr' variable.
    arr = model.predict([[Age, Duration, Heart_Rate, Body_Temp]])

    # Render the calorie.html template with the predicted result.
    return render_template("calorie.html", data=arr[0])

if __name__ == '__main__':
    # This block of code runs the Flask application when the script is executed.
    app.run()
