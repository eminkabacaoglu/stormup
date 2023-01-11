from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404

from ideas.models import Idea



def index(request):
    ideas=Idea.objects.filter(is_active=True)
    return render(request,'index.html',{
        "ideas":ideas
    })
    
def dashboard(request):
    return render(request,'dashboard.html')

def ideas(request):
    ideas=Idea.objects.filter(is_active=True)
    return render(request,'ideas.html',{
        "ideas":ideas
    })

def details(request,id):
    idea = get_object_or_404(Idea, pk=id)
    # idea=Idea.objects.get(pk=id)
    return render(request,'idea-details.html',{
        "idea":idea,
        "persons" :idea.person.all(),
        "documents":idea.document_set.all(),
        "comments":idea.comments.all().order_by("-id"),
    })