from django.shortcuts import render

# Create your views here.
def showIntro(request):

  data = {
    'title': 'Intro',
    'message': 'This is a message from the view',
  }
  
  return render(request, 'intro.html',data)
