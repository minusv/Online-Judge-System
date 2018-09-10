from django.shortcuts import render, redirect
from .forms import question_form, edit_question_form
from .models import question
from submission.models import status
from django.contrib.auth.decorators import login_required,user_passes_test


@login_required(login_url='/login')
@user_passes_test(lambda user: user.is_superuser,login_url='/login')
def judge_home(request):
    context={}
    judge_name = request.user
    context["name"]=judge_name
    return render(request,"judge/judge_home.html",context)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.is_superuser,login_url='/login')
def add_question(request):
    form=question_form(request.POST,request.FILES)
    context={'form':form,}
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('/judge')
    else:
        context['form'] = question_form()
    return render(request,'judge/add_question.html',context)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.is_superuser,login_url='/login')
def view_question(request):
    questions=question.objects.all()
    context={}
    context["questions"]=questions
    return render(request,'judge/view_question.html',context)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.is_superuser,login_url='/login')
def edit_question(request,pk):
    questionob = question.objects.get(pk=pk)
    if request.method=='POST':
        form=edit_question_form(instance=questionob,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/question/view')
    else:
        form=edit_question_form(instance=questionob)
    context={'form':form,}
    return render(request,'judge/edit_question.html',context)

@login_required(login_url='/login')
@user_passes_test(lambda user: user.is_superuser,login_url='/login')
def delete_question(request,pk):
    question.objects.filter(id=pk).delete()
    return redirect('/question/view')

@login_required(login_url='/login')
@user_passes_test(lambda user: user.is_superuser,login_url='/login')
def judge_status(request):
    context={}
    alldata=status.objects.all()
    context["alldata"]=alldata
    return render(request,"judge/judge_status.html",context)
