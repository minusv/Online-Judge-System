import os,uuid
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from judge.models import question
from .models import status
from .forms import Submit_Program
from submission import judge

def get_result(ob):
    subid=ob.id
    quescode=ob.quesid
    timelimit=question.objects.get(quescode=quescode).timelimit
    ip_file_path=question.objects.get(quescode=quescode).ip_file.path
    expopf_path=question.objects.get(quescode=quescode).op_file.path
    source_code_path=ob.source_code.path
    op_file_path=ob.op_file.path
    error_file_path=ob.error_file.path
    [result,time]=judge.run_prog(ip_file_path,expopf_path,source_code_path,error_file_path,op_file_path,float(timelimit))
    ob.result=result
    ob.time=time
    ob.save()

@login_required(login_url='/login')
def contestant_home(request):
    context={}
    name = request.user
    context["name"]=name
    return render(request,"submission/contestant_home.html",context)

@login_required(login_url='/login')
def submit_code(request):
    form = Submit_Program(request.POST, request.FILES)
    context={'form':form,}
    if request.method =="POST":
        if form.is_valid():
            s=form.save(commit=False)
            s.username=str(request.user)
            s.time=0.0
            s.save()
            get_result(s)
            return redirect("/contest/status")
    else:
        context['form']=Submit_Program()
    return render(request,'submission/submit_code.html',context)

@login_required(login_url='/login')
def view_status(request):
    context={}
    username=str(request.user)
    alldata=status.objects.filter(username=username)
    context["alldata"]=alldata
    return render(request,"submission/view_status.html",context)