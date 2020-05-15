from django.shortcuts import HttpResponse, render, redirect
# from django.http import HttpResponse
from django.template import loader
from .models import Contact
from django.contrib import messages
from .models import Post
from comment.models import UserCommet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


# def index(request):
#     return render (request, 'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<2 or len(phone)<10:
            messages.error(request, "Plese fill the form correctly")
        else:
            messages.success(request, "Your message has been sent sucessfully")
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, 'contact.html')
        
    
def healthcare(request):
    # return HttpResponse("Writer blogs")
    return render (request, 'healthcare.html')

def hippa(request):
    return HttpResponse("HIPPA")

def about(request):
    return render(request, 'about.html')

def home(request):
    post = Post.objects.all()
    comments = UserCommet.objects.filter(post=post)
    
    # post = Post.objects.filter(slug=slug).first()
    context = {'post': post, 'comments':comments}
    return render(request, 'home.html', context)
    # return HttpResponse("in home")

def search(request):
    query = request.GET['query']
    if len(query) > 80:
        allposts = Post.objects.none()

    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allposts = allPostsTitle | allPostsContent


    if allposts.count() == 0:
        messages.warning(request, "No Search result Found, please refine your query")
    params = {'allposts': allposts, 'query':query}
    return render(request, 'search.html', params) 

def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        

        # Checks for errorneous inpurts

        if not username.isalnum():
            messages.error(request, "Username should be alphanumeric")
            return redirect("Home page")


        if pass1 != pass2:
            messages.error(request, "passwords do not match")
            return redirect("Home page")
        

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.lasst_name = lname
        myuser.save()
        messages.success(request, "Your account has been sucessfully created")
        return redirect ("Home page")
    
    else:
        return HttpResponse("Not found")


def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            
            login(request, user)
            messages.success(request, "Sucessfully Logged In")
            
            return redirect("Home page")
        else:
            messages.error(request, "Invalid credentials, please try again!")
           
            return redirect("Home page")

    else:
        return HttpResponse("page not found")

def handlelogout(request):
    logout(request)
    messages.success(request, "sucessfully logged Out")
    return redirect ("Home page")
    return HttpResponse("logout")
