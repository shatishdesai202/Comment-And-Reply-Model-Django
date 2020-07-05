from django.shortcuts import render, redirect
from .forms import commentForm
from .models import Comment


def index(request):
    comment = Comment.objects.filter(parent=None).order_by('-timestamp')
    form = commentForm()
    
    if request.method == "POST":
        form = commentForm(request.POST)
        user = request.user
        form.instance.comment_by = user

        parent = request.POST.get('parent')

        if parent:
            parentPost = Comment.objects.get(id=parent)
            form.instance.parent = parentPost 

        print(parent)

        
        if form.is_valid():
            form.save()
            context = {'form': form}

            return redirect('index')

    context = {'form':form,'comment':comment}
    return render(request, 'index.html', context)

def commentdelete(request,id):
    com = Comment.objects.get(id=id)
    com.delete()
    return redirect('index')


    