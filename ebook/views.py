from pdb import post_mortem
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SignUpForm, UploadBookForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from . models import EBooksModel
from django.http import HttpResponse
from django.contrib.auth.models import User



# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created Sucessfully')
            fm.save()
            return redirect('user_login')
    else:
        fm = SignUpForm()        
    return render(request,'registration/signup.html',{'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            fm = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': fm})
    else:
        return redirect('/')


def user_logout(request):
    logout(request)
    return redirect("user_login")        




def book_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UploadBookForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')

        else:
            form = UploadBookForm()
            context = {'form':form} 
        return render(request,'ebook/upload_book.html',context)

    else:
        return redirect('/user_login/')

def book_list(request):
    books = EBooksModel.objects.all()
    return render(request,'ebook/book_list.html',{'books':books, "user":request.user})


def delete_book(request, id):
    if request.method == "POST":
        book = EBooksModel.objects.get(pk = id)
        print(request.user)
        if request.user.username == book.author:    
            book.delete()
        elif request.user.is_superuser:
            book.delete()
        else:
            HttpResponse("you have not delete permission")
        return redirect('/')

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    user_books = EBooksModel.objects.filter(author=username)#.all(uploaded_by=username)
    print("user_books", user_books)
    return render(request, 'registration/user_profile.html', {"user":user, "user_books": user_books})



def search(request):        
    search =  request.GET['search']    
    books = EBooksModel.objects.filter(titlee__icontains=search)
    return render(request,"ebook/search.html",{"books":books})    


        



