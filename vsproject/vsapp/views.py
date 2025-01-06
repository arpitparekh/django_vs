from django.shortcuts import render
from .models import Product,Blog
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

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
def showContact(request):
  return render(request, 'contact.html')
def showAbout(request):
  return render(request, 'about.html')

def showCrud(request):

  if request.method=='POST':
    name = request.POST['name']
    price = request.POST['price']
    quantity = request.POST['quantity']
    description = request.POST['description']

    # store data in database
    product = Product(name=name, price=price, quantity=quantity, description=description)
    product.save()
    # from django.shortcuts import redirect
    return redirect('crud')   # refresh the page

  list = Product.objects.all()
  # get all the product from the table


  return render(request, 'crud.html',{'list':list})

def showBlog(request):
  blogList = Blog.objects.all()
  print(blogList)
  return render(request, 'blog.html',{'blogList':blogList})

def showRegister(request):
  if request.method=='POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      return redirect('register')
  else:
    form = UserCreationForm()
  return render(request, 'register.html',{'form':form})
