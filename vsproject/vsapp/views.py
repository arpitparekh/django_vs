from django.shortcuts import render

# Create your views here.
def showIntro(request):
  return render(request, 'intro.html')
