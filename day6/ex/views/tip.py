from django.contrib.auth import authenticate, logout
from django.shortcuts import  redirect, render
import random
from ..forms import TipForm
from ..models import TipModel

def createtip(request):
    if request.method=='POST':
        form = TipForm(request.POST)
        if request.POST.get('up') or request.POST.get('down'):
            tip = TipModel.objects.get(pk=request.POST.get('up') or request.POST.get('down'))
            if request.POST.get('up'):
                tip.upvote(request.user)
            else:
                tip.downvote(request.user)
        if request.POST.get('delete') :
            TipModel.objects.get(pk=request.POST.get('delete')).delete()
        tmpform = TipForm(request.POST)
        if tmpform.is_valid:
            content=request.POST.get('content')
            if content is not None:
                tip = TipModel(content=request.POST.get('content'), author=request.user)
                tip.save()
    tips = TipModel.objects.all()
    return render(request, 'base.html', {'tips': tips, 'form': form})