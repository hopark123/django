import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import History
from .utils import Utils

# Create your views here.
utils = Utils()

def main(request):
    form = History()
    return render(request, 'ex02/index.html', {
        'history': utils.open_log(),
        'form': form
    })

def post(request):

    if request.method == 'POST':
        post = History(request.POST)
        if post.is_valid():
            utils.write_log(request.POST.get('content'))
        return HttpResponseRedirect('/ex02')
