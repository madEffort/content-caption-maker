from django.shortcuts import render
from rest_framework.views import View

class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "home.html")