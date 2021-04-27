![CI/CD](https://github.com/winstonpais/admitpredictor_backend/workflows/Django%20CI%20CD/badge.svg)
[![codecov](https://codecov.io/gh/winstonpais/admitpredictor_backend/branch/main/graph/badge.svg)](https://codecov.io/gh/winstonpais/admitpredictor_backend)

# admitpredictor_backend
Backend for the Admit Predictor Project.  
This is a Django Project that provides a REST API.   
Deployed at https://bhqqqb8355.execute-api.ap-south-1.amazonaws.com/dev with AWS API GateWay and AWS Lambda

## Environments

### Django Environment
The environment required for the django project the requirements for this environment exist in the requirements.txt file in the root of the repository.  
  
### Environment for developing ML models
The environment for building ML models is in the devRequiements.txt in the Ml_models folder.  

## Installation
To create a virtual environment using venv
```
python -m venv <Path to Environment>
```
To activate this environment for windows
```
venv\Scripts\activate.bat
```
Install the environment Requirements
```
pip install -r requirements.txt
```

## Development
All the features to be developed in seperate branches off the ddevelopment branch.    

Command to create a new brach off development
```
git checkout -b <New Branch Name> development
```

## Running the Tests
To run this Project enter the command
```
python manage.py test
```

## Running the project
To run this Project enter the command
```
python manage.py runserver
```

the development server should start at http://127.0.0.1:8000/
