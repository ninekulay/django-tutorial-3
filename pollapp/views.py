from django.shortcuts import render,redirect
from .models import Poll
from .forms import CreatePollForm
from django.http import HttpResponse

def home(request):
    polls = Poll.objects.all()
    context = {'polls' : polls}
    return render(request, 'poll/home.html',context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {'form' : form}
    return render(request, 'poll/create.html',context)

def vote(request,pk):
    poll = Poll.objects.get(id=pk)
    if request.method == "POST":
        select_option = request.POST['poll']
        if select_option == 'option_one':
            poll.option_one_count += 1
        elif select_option == 'option_two':
            poll.option_two_count += 1
        elif select_option == 'option_three':
            poll.option_three_count += 1
        else:
            return HttpResponse(400,'Please vote before submit')
        poll.save()
        return redirect('results',pk)
    context = {'poll' : poll}
    return render(request, 'poll/vote.html',context)

def results(request,pk):
    poll = Poll.objects.get(id=pk)
    total = poll.option_one_count + poll.option_two_count + poll.option_three_count
    context = {'poll' : poll , 'total' : total}
    return render(request, 'poll/results.html',context)
