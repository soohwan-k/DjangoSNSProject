from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        return render(request, "DjangoSNSProject/main.html")

    def post(self, request):
        return render(request, "DjangoSNSProject/main.html")
