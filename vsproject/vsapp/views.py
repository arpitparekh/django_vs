from django.shortcuts import render

# Create your views here.
def showIntro(request):

  data = {
    'title': 'Intro',
    'message': 'This is a message from the view',
  }

  return render(request, 'intro.html',data)

# def showIntro(reuqest):
# return render(reuqest, 'intro.html')

# def showDashboard(request):
#   return render(request, 'dashboard.html')

def showHome(request):
  return render(request, 'home.html')
