from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserProfileForm


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('videos:home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Log the user in
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to EcoDu!')
            return redirect('videos:home')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('videos:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Xush kelibsiz, {username}!')
            return redirect('videos:home')
        else:
            messages.error(request, 'Foydalanuvchi nomi yoki parol noto\'g\'ri.')
    
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    """User logout view"""
    logout(request)
    return redirect('videos:home')


@login_required
def profile(request):
    """User profile view"""
    from videos.models import VideoProgress
    from quizzes.models import QuizAttempt
    
    # Get user statistics
    videos_watched = VideoProgress.objects.filter(user=request.user, completed=True).count()
    quiz_attempts = QuizAttempt.objects.filter(user=request.user)
    quizzes_passed = quiz_attempts.filter(passed=True).count()
    
    # Recent activity
    recent_videos = VideoProgress.objects.filter(user=request.user).order_by('-watched_at')[:5]
    recent_quizzes = quiz_attempts.order_by('-completed_at')[:5]
    
    context = {
        'videos_watched': videos_watched,
        'quizzes_passed': quizzes_passed,
        'recent_videos': recent_videos,
        'recent_quizzes': recent_quizzes,
    }
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    """Edit user profile"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'users/edit_profile.html', {'form': form})
