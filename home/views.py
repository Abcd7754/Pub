from django.shortcuts import render,HttpResponse
from home.models import Tasks
# Create your views here.
def home(request):
    return render(request,"Index.html")
   # return HttpResponse("This ")
def AssignTasks(request):
    if request.method=="POST":
        TaskTitle=request.POST['TaskTitle']
        TaskDescription=request.POST['TaskDescription']
        print(TaskTitle,TaskDescription)
        ins = Tasks(TaskTitle=TaskTitle,TaskDescription=TaskDescription)
        ins.save()
        print("the data has been written to DB")
    return render(request,"AssignTasks.html")
def ViewTasks_Tabular(request):
    allTasks= Tasks.objects.all()
    context= {'tasks' : allTasks}
    return render(request,"ViewTasks_Tabular.html", context)
def ViewTasks(request):
    allTasks= Tasks.objects.all()
    context= {'tasks' : allTasks}
    return render(request,"ViewTasks.html", context)
def ViewTaskDescription(request,slug1):
    #To capture first element of list
    Task=Tasks.objects.filter(TaskTitle=slug1).first()
    context={'Task':Task}
    return render(request,"ViewTaskDescription.html", context)
    #return HttpResponse(f"You are viewing {slug1}")
    return 