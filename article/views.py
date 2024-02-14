from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import article,comments
from django.contrib.auth.decorators import login_required
def index(request):
    context={
        "numbers":[1,2,3,4,5,6,7,8,9]
    }
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
def dashboard(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=article.objects.filter(title__contains=keyword)
        return render(request,"dashboard.html",{"articles":articles})    
    if request.user.is_authenticated:
       articles=article.objects.filter(author=request.user)
    else:
       articles=[] 
    return render(request,"dashboard.html",{"articles":articles})
@login_required(login_url="user:login")
def addArticle(request):    
    if request.method=="POST":
        form=ArticleForm(request.POST,request.FILES)
        article=form.save(commit=False)
        article.author=request.user
        article.save()       
        messages.success(request,"Başarıyla Kaydedildi")
        return redirect("dashboard")
    else:  
        form=ArticleForm()
        return render(request,"addArticle.html",{"form":form}) 
@login_required(login_url="user:login")  
def update(request,id):
    Article=get_object_or_404(article,id=id)
    form=ArticleForm(request.POST,request.FILES,instance=Article)
    if request.method=="POST":
      if form.is_valid():
        article1=form.save(commit=False)
        article1.author=request.user
        article1.save()
        messages.success(request,"İşlem Başarılı")         
        return redirect("dashboard")
    form=ArticleForm(instance=Article)
    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")  
def delete(request,id):
    Article=get_object_or_404(article,id=id)
    Article.delete()
    messages.success(request,"İşlem Başarılı")
    return redirect("dashboard")    
def details(request,id):
    pass  
def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles=article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = article.objects.all()
    comments1 = comments.objects.all()

    if request.method == "POST":
        comment_author = request.POST["comment_author"]
        comment_content = request.POST["comment_content"]
        article_id = request.POST["article_id"]

        comments1 = comments(
        comment_author=comment_author,
        comment_content=comment_content,
        article_id=article_id,
    )
        comments1.save()
        return redirect("/article/articles")

    return render(request, "articles.html", {"articles": articles, "comments": comments1})


    

     