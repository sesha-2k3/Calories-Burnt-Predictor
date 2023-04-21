# Calories Burnt Predictor
Calories Predictor web-app is an online web application used to predict the anmount of calories that are burned by a person performing a certain physical activity based on the given input. Created using python's scikit-learn, Fastapi, numpy and joblib packages.

![python 3.11.0](https://img.shields.io/badge/Python-blue.svg)
![html](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
<img alt="CSS" src="https://img.shields.io/badge/CSS%20-%231572B6.svg?logo=css3&logoColor=white">
![numpy](https://img.shields.io/badge/Numpy-777BB4?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/Scikit_learn-0078D4?logo=scikit-learn&logoColor=white)
![fastapi](https://img.shields.io/badge/Fastapi-109989?logo=FASTAPI&logoColor=white)
![jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?logo=Jupyter&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)



## Dataset Description

The dataset consist of several predictor (independent) variables and one target (dependent) variable, Calories. Independent variables include the Age, BMI, Sex, Duration, Heart Rate, Body Temperature.

The data contains the following columns:

| Feature Name               | Feature Description                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| Age                        | Age (years)                                                                                         |
| BMI                        | Body mass index (weight in kg/(height in m)^2)                                                      |
| Sex                        | Class variable for Gender (male or female)                                                          |
| Duration                   | Duration of the activity                                                                            |
| Heart Rate                 | Heart Rate of the person                                                                            |
| Body Temperature           | Body temperature of the person                                                                      |
| Calories                   | Amount of calories burned by the person                                                             |

## Installation

Open Anaconda prompt and create new environment

```
conda create -n your_env_name python = (any_version_number > 3.11.0)
```

Then Activate the newly created environment

```
conda activate your_env_name
```

Clone the repository using `git`

```
git clone gh repo clone sesha-2k3/Calories-Burnt-Predictor
```

Change to the cloned directory

```
cd <directory_name>
```

To install all requirement packages for the app

```
pip install -r requirements.txt
```

Then, Run the app

```
uvicorn main:app --reload
```

## 📷 Screenshots

### Website

![app interface](markdown/website.png)


