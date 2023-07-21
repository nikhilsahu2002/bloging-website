from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.core.paginator import Paginator
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse

from Login.models import NewsArticle,Comment

def reg(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'Registration.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                user.save()
                # Redirect to the 'login' URL
                return redirect('/login/')
        else:
            return render(request, 'Registration.html', {'error': 'Password does not match!'})
    else:
        return render(request, 'Registration.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth_logout(request)
    return redirect('/Login/')

# def (request):
#     return render(request,"tables.html")

@login_required(login_url='/Login/')
def create_article(request):
    if request.method == 'POST':
        headline = request.POST.get('headline')
        description = request.POST.get('description')
        image_url = request.POST.get('image_url')
        image = request.FILES.get('image')
        date = request.POST.get('date')
        category = request.POST.get('category')

        article = NewsArticle(
            user=request.user,
            headline=headline,
            description=description,
            date=date,
            category=category
        )
        
        if image_url:
            article.image_url = image_url
        elif image:
            article.image = image

        article.save()
        return HttpResponse("Article is stored successfully.")

    return render(request, 'restricted.html')
@login_required(login_url='/Login/')
def table(request):
    # Get the articles created by the current user
    articles = NewsArticle.objects.filter(user=request.user)
    paginator = Paginator(articles, 10)  # Set the number of articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get the comments made by the current user
    comments = Comment.objects.filter(user=request.user)
    paginator1 = Paginator(comments, 10)  # Set the number of comments per page
    page_number1 = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number1)

    if request.method == 'POST':
        # Delete Article
        if 'delete_article' in request.POST:
            article_id = request.POST.get('delete_article')
            article = get_object_or_404(NewsArticle, id=article_id, user=request.user)
            article.delete()

        # Delete Comment
        if 'delete_comment' in request.POST:
            comment_id = request.POST.get('delete_comment')
            if comment_id:
                comment = get_object_or_404(Comment, id=comment_id, user=request.user)
                comment.delete()
            else:
                # Handle the case when the comment ID is missing or empty
                return redirect('table')

        # Redirect back to the same page after deleting
        return redirect('table')

    return render(request, 'tables.html', {'page_obj': page_obj, 'page_obj1': page_obj1})
# Restricted Views 
# def restricted_page(request):
#     return render(request, 'restricted.html')

@login_required(login_url='/Login/')
def Admin(request):
    return render(request,'index.html')

@login_required(login_url='/Login/')
def comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        Comment.objects.create(name=name, email=email, comment=comment)

        return HttpResponse("Comment submitted successfully!")

    return render(request, 'thali.html')

def hone(request):
    return render(request,"home.html")

def Food(req):
    context = NewsArticle.objects.filter(category ='food')
    return render(req,"food.html",{"context" : context})


def rest(req):
        context = NewsArticle.objects.filter(category='restaurant')
        return render(req,"restaurant.html",{"context" : context})

def about(req):
    return render(req,"about.html")

def drink(req):
    context = NewsArticle.objects.filter(category='drink')
    return render(req,"drinks.html",{'context': context})

def your_view(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    articles = [article]  # Wrap the single object in a list

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')

        # Create a new comment object
        comment = Comment(name=name, email=email, comment=comment_text)
        comment.save()

    return render(request, 'thali.html', {'articles': articles})