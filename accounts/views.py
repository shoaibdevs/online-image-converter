from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, password_validation
from django.contrib import messages
from django.contrib.auth.models import User
from tool.models import *

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        if email and password:
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Login Sucessfull')
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Invalid email or password!!!'})
        else:
            return render(request, 'login.html', {'error': 'Email and password is required.'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        print(email, password)
        if email and password and confirm_password:
            if password != confirm_password:
                print('not confirm')
                return render(request, 'register.html', {'error': 'Password and confirm password does not match.', 'email': email})
            elif User.objects.filter(username=email).exists():
                print('already')

                return render(request, 'register.html', {'error': 'Email already exists.','email': email})
            
            else:
                try:
                    password_validation.validate_password(password)
                except password_validation.ValidationError as e:
                    return render(request, 'register.html', {'error_2': e.messages, 'email': email})
                user = User.objects.create_user(username=email, password=password)
                login(request, user)
                messages.success(request, f'Login Sucessfull')
                return redirect('home')
        else:
            return render(request, 'register.html', {'error': 'Email and password is required.'})
    else:
        return render(request, 'register.html', {'email' : ''})


def logout_view(request):
    logout(request)
    request.session['lng_code'] = 'en'
    return redirect('home')

def set_language(request):
    """
    Set the language preference and redirect back to the previous page.
    """
    request_path = request.get_full_path()
    print(request_path)
    if request.method == 'POST':
        lang_code = request.POST.get('language')
        current_url = request.POST.get('currentUrl').lstrip('/')
        
        print(lang_code, current_url)
        if lang_code:
            request.session['lng_code'] = lang_code
        if len(current_url) == 3:
            return redirect('/'+lang_code)
        if current_url != '':
            check = ToolPageTranslation.objects.filter(
                url__url=current_url
            )
            if check.exists():
                print(check[0].tool_page_id)
                check_2 = ToolPageTranslation.objects.filter(
                    tool_page_id=check[0].tool_page_id,
                    language=lang_code
                )
                if check_2.exists():
                    print("exist",check_2[0].url)
                    return redirect(str(check_2[0].url))
            else:
                return redirect(str(current_url))

    # Redirect back to the previous page or a default page
    return redirect('/'+lang_code)