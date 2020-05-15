from django.shortcuts import render, HttpResponse, redirect
from Blog.models import Post
from django.contrib import messages

# Create your views here.


# def commenthome(request):
#     return HttpResponse("comment home")

def postComment(request):
    return HttpResponse("test")

    # if request.method=='POST':
    #     comment = request.POST.get("comment")
    #     user = request.user
    #     postSno = request.POST.get("postSno") 
    #     post = Post.objects.get(sno=postSno)


    #     comment = postComment(comment=comment, user=user, post=post)
    #     comment.save()
    #     messages.success(request, "your comment has been posted sucessfylly")
        
    #     return redirect("home page")
