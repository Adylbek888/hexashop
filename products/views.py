from django.shortcuts import render
from .models import *


def mens(request):
    mens = Mens.objects.all()
    context = {
        "mens":mens
    }
    return render(request,'products/mens.html',context=context)

def womens(request):
    womens = Womens.objects.all()
    context = {
        "womens":womens
    }
    return render(request,'products/womens.html',context=context)

def kids(request):
    kids = Kids.objects.all()
    context = {
        "kids":kids
    }
    return render(request,'products/kids.html',context=context)

def accessories(request):
    accessories= Accessories.objects.all()
    context = {
        "accessories":accessories
    }
    return render(request,'products/accessories.html',context=context)

def single_product(request):
    return render(request,'products/single-product.html') 