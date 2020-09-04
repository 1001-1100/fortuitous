from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
import random
import requests

class IntegerSequence(APIView):
    def post(self, request, format=None):
        integerSequences = []
        for i in range(int(request['n'])):
            integerSequence = random.sample(range(int(request['min']),int(request['max'])), int(request['length']))
            integerSequences.append(integerSequence)
        return Response(integerSequences)
