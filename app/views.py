
# Create your views here.


from .models import Choice, Question
from django.http import HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render, redirect 
from django.urls import reverse 
from django.views import generic
from .models import Choice, Question


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('app:index')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('app:coding')
	else:
		form = SignUpForm()
		return render(request, 'app/register.html', {'form':form})

	return render(request, 'app/register.html', {'form':form})


class CodingView(generic.ListView): 
    template_name = 'app/Coding_test.html' 
    context_object_name = 'latest_question_list'
    def get_queryset(self): 

        """Return the last five published questions.""" 
        return Question.objects.order_by('-pub_date')[:20]

class IndexView(generic.ListView): 
    template_name = 'app/index.html' 
    context_object_name = 'latest_question_list'
    def get_queryset(self): 

        """Return the last five published questions.""" 
        return Question.objects.order_by('-pub_date')[:10]
    

    
class DetailView(generic.DetailView): 
    model = Question 
    template_name = 'app/detail.html'


class ResultsView(generic.DetailView): 
    model = Question 
    template_name = 'app/results.html'


def vote(request, question_id): 
    question = get_object_or_404(Question, pk=question_id) 
    try: selected_choice = question.choice_set.get(pk=request.POST['choice']) 
    except (KeyError, Choice.DoesNotExist): 
        # Redisplay the question voting form. 
        return render(request, 'app/detail.html', { 'question': question, 'error_message': "You didn't select a choice.",
}) 
    else: 
        selected_choice.votes += 1 
        selected_choice.save() 
    # Always return an HttpResponseRedirect after successfully dealing 
    # with POST data. This prevents data from being posted twice if a # user hits the Back button. 
    return HttpResponseRedirect(reverse('app:results', args=(question.id,)))



# def choice(request, question_id):
#     model = choice
#     question = get_object_or_404(Question, pk=question_id)
#     choice_correct = question.choice_set.get(pk=request.POST['vote'])
#     context = {'choice_correct':choice_correct}
#         # Redisplay the question voting form. 
#     return render(request, 'app/result.html', context)                                                    