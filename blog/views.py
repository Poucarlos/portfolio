from django.shortcuts import render , get_object_or_404
from . models import blog
# Create your views here.
#get_object_or_404 this gets any specific page if not it will give a file not foiund page
def allblogs(request):
	blogs=blog.objects
	return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail(request,blog_id):
	blog_detail=get_object_or_404(blog,pk=blog_id)
	return render(request,'blog/detail.html',{'blog':blog_detail})

