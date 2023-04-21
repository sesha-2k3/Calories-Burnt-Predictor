import joblib # For loading model pickle file
import numpy as np # For array conversion
import pandas as pd # For dataframe conversion
from sklearn.preprocessing import StandardScaler as sc # For normalising the input

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI() # Instance of FastAPI class

# Mount static folder files to /static route
app.mount("/static",StaticFiles(directory="static"),name="static")

# Loads the Machine Learning model
model = joblib.load("models/Calories_Predictor_RF_.pkl")


# Sets the templates folder for the app
templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def home_index(request: Request):
	"""
    Function to render `index.html` at route '/' as a get request
    __Args__:
    - request (Request): request in path operation that will return a template
    __Returns__:
    - TemplateResponse: render `result.html`
    """
	return templates.TemplateResponse("index.html",{"request":request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
	request: Request,
    Age: int = Form(...),
    BMI: float = Form(...),
    Duration: float = Form(...),
    Heart_rate: float = Form(...),
    Body_Temp: float = Form(...),
    Gender_male: str = Form(...)):
	"""
    Function to predict Calories Burned
    and shows the result by rendering `index.html` at route `/predict`

    __Args__:
    - __request__: request in path operation that will return a template
    - __Age__: age of the person ,
    - __BMI__: body mass index of the person,
    -__Duration__: activity duration of the person,
    -__Heart_rate__: heart rate of the person,
    -__Body_Temp__: body temperature of the person,
    - __Gender_male__: sex of the person,
    
    __Returns:__
    - __TemplateResponse__: render `result.html`
    """

	sex = 1 if sex.lower() == "male" else 0


	# Convert list to pandas dataframe

	input_list = [Age, BMI, Duration, Heart_rate, Body_Temp, Gender_male]

	final_values = sc.transform(np.array(input_list).reshape(1,-1))
	
    # norm_final_values = sc.transform(final_values)

	output = model.predict(final_values) # Predicts using the model

	prediction = round(output[0],2)
	
	return templates.TemplateResponse("index.html",context={"request":request,"prediction":prediction})



