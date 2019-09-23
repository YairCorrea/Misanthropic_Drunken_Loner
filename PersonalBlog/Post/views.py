from django.shortcuts import render
from django.http import HttpResponse
from Post.models import Post
from django.template import loader
def index(request):
    return render(request,'Home/index.html')
def OnePost(request,Post_id):
    post = Post.objects.filter(id=Post_id).first()
    template = loader.get_template('Post/OnePost.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))
