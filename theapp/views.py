from django.shortcuts import render

# Create your views here.
def main(requests):
    return render(requests, 'main.html')
def intro(requests):
    return render(requests, 'intro.html')
def photos(requests):
    return render(requests, 'photos.html')
def new(requests):
    return render(requests, 'new.html')