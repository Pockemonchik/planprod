from django.shortcuts import render, redirect, get_object_or_404;

def rate_otsenka(request):
    return render(request,'rate_otsenka.html');

def nach_kaf(request):
    return render(request,'nach_kaf.html');

def sotr_umr(request):
    return render(request,'sotr_umr.html');