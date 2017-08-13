from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404
from .models import News
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def news_list(request):
    posts_list = News.objects.all().order_by('-date')
    paginator = Paginator(posts_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'news/home.html', {'posts': posts})



def post_detail(request, pk):
    post = get_object_or_404(News, pk=pk)
    share_string = quote_plus(post.title)
    return render(request, 'news/post_detail.html', {'post': post, 'share_string': share_string})

def contacts(request):
    return render(request, 'news/contacts.html')

def licey(request):
    return render(request, 'news/licey.html')