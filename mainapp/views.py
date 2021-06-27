from django.shortcuts import render
from django.http import JsonResponse
# from .helperFunctions import getModel

# Create your views here.

def index(request):
    response = {
        'message' : 'Hello AWS Lambda From GitHub Actions!!!'
    }
    return JsonResponse(response)

# def sklearnLinearRegression(request):
#     # http://127.0.0.1:8000/sklearn_LinearRegression/?GREScore=337&TOEFLScore=118&UniversityRating=4&SOP=4.5&LOR=4.5&CGPA=9.65&Research=1
#     response = {
#         'message' : 'An Unknown Error has occoured',
#         'success' : False
#     }

#     model = getModel('sklearn_LinearRegression')
#     if not model:
#         response['message'] = 'sklearn LinearRegression pickeled model was not found'
#         return JsonResponse(response)

#     parameters = ['GREScore', 'TOEFLScore', 'UniversityRating', 'SOP', 'LOR', 'CGPA', 'Research']
#     inputParameters = { parameter : request.GET.get(f'{parameter}') for parameter in parameters}
#     response['inputParameters'] = inputParameters
    
#     try:
#         modelInput = [inputParameters[parameter] for parameter in parameters]
#         chanceOfAdmit = model.predict([modelInput])
#     except:
#         response['message'] = 'Invalid Input Parameters/Query String'
#         return JsonResponse(response)

#     response['message'] = 'Successfully Predicted Chance Of Admit'
#     response['success'] = True
#     response['chanceOfAdmit'] = chanceOfAdmit[0]

#     return JsonResponse(response)

def tensorflowNeuralNetworks(request):
    # http://127.0.0.1:8000/tensorflow_neuralNetwork/?GREScore=337&TOEFLScore=118&UniversityRating=4&SOP=4.5&LOR=4.5&CGPA=9.65&Research=1
    response = {
        'message' : 'An Unknown Error has occoured',
        'success' : False
    }

    model = getModel('tensorflow_neuralNetworks')
    if not model:
        response['message'] = 'tensorflow Neural Network pickeled model was not found'
        return JsonResponse(response)

    parameters = ['GREScore', 'TOEFLScore', 'UniversityRating', 'SOP', 'LOR', 'CGPA', 'Research']
    inputParameters = { parameter : request.GET.get(f'{parameter}') for parameter in parameters}
    response['inputParameters'] = inputParameters
    
    try:
        modelInput = [inputParameters[parameter] for parameter in parameters]
        modelInput = list(map(float, modelInput))
        print('Hello')
        print(modelInput)
        chanceOfAdmit = model.predict([modelInput])
        print(chanceOfAdmit)
        print(chanceOfAdmit[0][0])
    except:
        response['message'] = 'Invalid Input Parameters/Query String'
        return JsonResponse(response)

    response['message'] = 'Successfully Predicted Chance Of Admit'
    response['success'] = True
    response['chanceOfAdmit'] = str(round(chanceOfAdmit[0][0], 2))

    return JsonResponse(response)