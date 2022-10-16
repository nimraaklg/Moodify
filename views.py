import os
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from dashboard.utils import getAccessToken, getClientId



def login(request):
    client_id = getClientId()
    redirect_uri = os.environ.get('SPOTIFY_REDIRECT_URI')
    auth_uri = 'https://accounts.spotify.com/authorize?client_id={}&redirect_uri={}&response_type={}'
    final_auth_uri = auth_uri.format(client_id,redirect_uri,'code')
    return redirect(final_auth_uri)


def callback(request):
    error = request.GET.get('error')
    code = request.GET.get('code')

    if(error != None):
        return HttpResponse("Oh no, {}".format(error))

    return HttpResponse(getAccessToken(code))

    #TODO: getAccessToken response returns access token of the logged in user, use this token to fetch data for the user and calcluate recommendations


def dashBoard(request):
    return HttpResponse("Hello, this is the dashboard.")