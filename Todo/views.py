from django.shortcuts import render,redirect, get_object_or_404
from .forms import RegisterForm,Postform,Updateform
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Task
import inflect
# Create your views here.
@login_required(login_url='/login')
def home(request):
    tasks= Task.objects.filter(author=request.user)
    if request.method == 'POST':
        task= request.POST.get('task')
        task= get_object_or_404(Task,id=task)
        task.delete()
    count = len(tasks)
    word = inflect.engine()
    num = word.number_to_words(count)
    return render(request,'Todo/home.html',{'tasks':tasks,'count':num})

def sign_up(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/')
        else:
             print(form.error_messages)
    else:
        form = RegisterForm()
    return render(request,'registration/sign_up.html', {'form':form})

@login_required(login_url='/login')
def addTask(request):
    form= Postform()
    if request.method =='POST':
        form = Postform(request.POST)
        if form.is_valid():
           task= form.save(commit=False)
           task.author=request.user
           if request.FILES.get('image'):
                task.image=request.FILES.get('image')
           task.save()
           return redirect('/')
    return render(request, 'Todo/create.html', {'form':form})
def updateTask(request,pk):
    form= Updateform()
    if request.method =='POST':
        form = Updateform(request.POST)
        if form.is_valid():
           task = get_object_or_404(Task,pk=pk)
           if form.cleaned_data.get('done'):
             task.delete()
           else:
            task.text= form.cleaned_data.get('text')
            task.description= form.cleaned_data.get('description')  
            task.author=request.user
            if request.FILES.get('image'):
                task.image=request.FILES.get('image')
            task.save()
        return redirect('/')
    if request.method == 'GET':
        task = get_object_or_404(Task,pk=pk)
        newt= {
            'image': task.image,
    'text': task.text,
    'description': task.description,
    'done':task.done,
        }
        form = Updateform(newt)
    return render(request, 'Todo/update.html', {'form':form,'task':task})