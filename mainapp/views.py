from django.shortcuts import render
from django.http import JsonResponse
from .helperFunctions import getModel, getParametersFromQueryString

# Create your views here.

def index(request):
    response = {
        'message' : 'Hello AWS Lambda From GitHub Actions!!!'
    }
    return JsonResponse(response)

def sklearnLinearRegression(request):
    # http://127.0.0.1:8000/sklearn_LinearRegression/?GREScore=337&TOEFLScore=118&UniversityRating=4&SOP=4.5&LOR=4.5&CGPA=9.65&Research=1
    response = {
        'message' : 'An Unknown Error has occoured',
    }

    model = getModel('sklearn_LinearRegression')
    if not model:
        response['message'] = 'sklearn LinearRegression pickeled model was not found'
        return JsonResponse(response)

    parameters = ['GREScore', 'TOEFLScore', 'UniversityRating', 'SOP', 'LOR', 'CGPA', 'Research']
    inputParameters, validQueryString = getParametersFromQueryString(request, parameters)
    if not validQueryString:
        response['message'] = 'Invalid Input Query String'
        return JsonResponse(response)
    
    try:
        modelInput = [inputParameters[parameter] for parameter in parameters]
        chanceOfAdmit = model.predict([modelInput])
    except:
        response['message'] = 'Invalid Input Parameters'
        return JsonResponse(response)

    response['message'] = 'Successfully Predicted Chance Of Admit'
    response['chanceOfAdmit'] = chanceOfAdmit[0]
    response['inputParameters'] = inputParameters

    return JsonResponse(response)