from django.shortcuts import render

def index_view(request):

    return render(request, 'index.html')

def madara(request):

    return render(request, 'madara.html')

def kakashi(request):
    return render (request, 'kakashi.html')

def shikamaru(request):

    return  render(request, 'shikamaru.html')




