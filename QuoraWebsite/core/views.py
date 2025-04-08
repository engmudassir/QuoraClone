from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterForm, QuestionForm, AnswerForm
from .models import Question, Answer, Like
from django.contrib import messages
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        print(form,"DDDDDDDDDDDDDDDD")
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user,"AAAAAAAAAAA")
            login(request, user)
            return redirect('home')
        else:
            print(user,"BBBBBBBB")
            messages.error(request, 'Invalid username or password.')  # 👈 Add this
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Home Page - View Questions and Post New Question
@login_required
def home_view(request):
    questions = Question.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm() 
    return render(request, 'home.html', {'questions': questions, 'form': form})

# Question Detail View - Post Answer and View Answers
@login_required
def question_detail_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all().order_by('-created_at')

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('question_detail', question_id=question_id)
    else:
        form = AnswerForm()

    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

# Like Answer
@login_required
def like_answer_view(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    already_liked = Like.objects.filter(user=request.user, answer=answer)
    if not already_liked.exists():
        Like.objects.create(user=request.user, answer=answer)
    return redirect('question_detail', question_id=answer.question.id)




def user_list(request):
    users = User.objects.all()
    print(users,"VVVVVVVVVVVVVVVVVVVVVVVVV")
    return render(request, 'user_list.html', {'users': users})