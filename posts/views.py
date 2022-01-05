from django.shortcuts import render, get_object_or_404
from .models import post
# Create your views here.
def postz(request):
    posts = post.objects.order_by('-date')[:1]
    second = post.objects.order_by('-date')[1:2]
    third = post.objects.order_by('-date')[2:3]
    trend1 = post.objects.order_by('pk')[:2]
    trend2 = post.objects.order_by('pk')[2:4]
    trend3 = post.objects.order_by('pk')[4:6]
    newly = post.objects.order_by('-pk')[0:5]
    last = post.objects.order_by('date')
    return render(request,'posts/viewmore.html',{'posts':posts,'second':second,'third':third,'trend1':trend1,'trend2':trend2,'trend3':trend3,'newly':newly,'last':last})
def details(request,post_id):
    posty = get_object_or_404(post,pk = post_id)
    return render(request,'posts/details.html',{'posty':posty})