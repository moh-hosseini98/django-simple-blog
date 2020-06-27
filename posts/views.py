from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.db.models import Count,Q
from .models import Post,PostView
from .forms import CommentForm

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset':queryset
    }    


    return render(request,'posts/search_result.htm',context)

def get_category_count():

    queryset = Post.objects.values('category__title').annotate(Count('category__title'))

    return queryset


def home(request):

    latest = Post.objects.order_by('-timestamp')[0:3]

    context = {
        
        'latest':latest,
    }

    return render(request,'posts/index.htm',context)

def blog(request):

    category_count = get_category_count()
    print(category_count)

    post_list = Post.objects.all()
    
    most_recent = Post.objects.order_by('-timestamp')[:3]
    
    
    context = {
        'post_list':post_list,
        'most_recent':most_recent,
        'category_count':category_count,
        
        
    }

    return render(request,'posts/blog.htm',context)

def post(request,id):



    post = get_object_or_404(Post,id=id)
    if request.user.is_authenticated:

    
        PostView.objects.get_or_create(user = request.user,post=post)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse('detail',kwargs={
                'id':post.id

            }))



    context = {
        'post':post,
        'form':form,
    }



    return render(request,'posts/detail.htm',context)    
