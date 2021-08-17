import requests
import requests.auth
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = "app/profile.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        print(request)
        print(request.session.keys)
        access_token = request.session['oidc_access_token']

        url = 'http://localhost:8000/drf/testmodels/'

        headers = {
            'Authorization': 'Bearer {0}'.format(access_token)
        }

        respons = requests.get(url, headers=headers)
        print(respons)
        return super().get(request, *args, **kwargs)