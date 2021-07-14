from django.shortcuts import render
from django.http import JsonResponse
from .helperFunctions import getModel

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
    # http://127.0.0.1:8000/tensorflow_neuralNetworks/?GREScore=337&TOEFLScore=118&UniversityRating=4&SOP=4.5&LOR=4.5&CGPA=9.65&Research=1
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
    
    allUniRatings = [4.92, 4.7, 4.53, 4.13, 4.12, 4.02, 4.0, 3.95, 3.92, 3.91, 3.77, 3.72, 3.69, 3.64, 3.64, 3.61, 3.61, 3.54, 3.5, 3.46, 3.44, 3.42, 3.39, 3.38, 3.38, 3.35, 3.35, 3.26, 3.25, 3.21, 3.21, 3.19, 3.19, 3.19, 3.17, 3.14, 3.14, 3.14, 3.12, 3.12, 3.09, 3.09, 3.08, 3.06, 3.04, 3.04, 3.03, 3.02, 3.0, 2.99, 2.99, 2.98, 2.98, 2.96, 2.94, 2.94, 2.93, 2.92, 2.88, 2.85, 2.85, 2.84, 2.84, 2.83, 2.81, 2.81, 2.81, 2.8, 2.8, 2.8, 2.8, 2.79, 2.79, 2.77, 2.77, 2.76, 2.75, 2.75, 2.74, 2.74, 2.73, 2.73, 2.73, 2.72, 2.72, 2.71, 2.71, 2.71, 2.7, 2.69, 2.69, 2.69, 2.68, 2.67, 2.66, 2.66, 2.65, 2.65, 2.64]
    allUnis = []
    for UR in allUniRatings:
        inputParameters['UniversityRating'] = UR
        allUnis.append(dict(inputParameters))
    # print(allUnis)
    ch = []
    for p in allUnis:
        try:
            modelInput = [p[parameter] for parameter in parameters]
            modelInput = list(map(float, modelInput))
            chanceOfAdmit = model.predict([modelInput])
            ch.append(str(round(chanceOfAdmit[0][0], 2)))
        except:
            response['message'] = 'Invalid Input Parameters/Query String'
            return JsonResponse(response)

    response['message'] = 'Successfully Predicted Chance Of Admit'
    response['success'] = True
    response['chanceOfAdmit'] = ch

    return JsonResponse(response)