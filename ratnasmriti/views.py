from django.shortcuts import render
from app.models import *
from django.shortcuts import render, get_object_or_404

def HOME(request):
    category = Main_Category.objects.all().order_by('-id')
    popular = Post.objects.filter(section='Popular',status=1).order_by('-id')[0:4]
    recommended = Post.objects.filter(section='Recommended',status=1).order_by('-id')[0:4]


    context = {
        'category': category,
        'popular': popular,
        'recommended': recommended,
        # 'sub_category': sub_category,
    }
    return render(request, 'index.html',context)

def PRODUCT(request,id):
    main_category = get_object_or_404(Main_Category, id=id)
    sub_categories = Sub_Category.objects.filter(main_category=main_category)
    cmb = Main_Category.objects.all()
    recommended = Post.objects.filter(section='Recommended',status=1).order_by('-id')[0:4]

    context = {
        'main_category': main_category,
        'sub_categories': sub_categories,
        'cmb': cmb,
        'recommended' : recommended,
    }
    return render(request, 'product.html',context)

def  ABOUT(request):

    return render(request,'about.html')

def DESCRIPTION(request,id):
    sub_category = Sub_Category.objects.filter(id=id)
    context = {
        'sub_category': sub_category,
    }
    return render(request,'description.html',context)

def CATEGORY(request,id):
    popular = get_object_or_404(Post,id=id)
    # sub_categories = Post.objects.filter(section='Popular',status=1)
    context = {
        'popular': popular,
        # 'sub_categories': sub_categories,
    }
    return render (request,'category.html',context)

def ABOUTUS(request):
    return render(request,'aboutus.html')

def BLOG(request):
    blog = Blog.objects.all().order_by('-id')
    context = {
        'blog': blog,
        }
    
    return render(request,'blog.html',context)

def BLOGDETAILS(request):
    return render(request,'blogdetails.html')