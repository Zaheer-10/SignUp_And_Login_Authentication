from django.shortcuts import render, redirect
from .models import user_data, about
from django.contrib import messages
from django.contrib.auth import authenticate
from django.db.models import Q
# from django.db.models import filter

# Create your views here.
# .....................................................SIGNUP......................................................................


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        pass1 = request.POST['password2']
        email = request.POST['email']

        if password == pass1:
            new_user = user_data(
                username=username, email=email, password=password)
            new_user.save()  # store into the DB
            return redirect('login')

        else:
            messages.info(request, 'Password Must Match')
            return redirect('reg')

    else:
        return render(request, 'signup.html')


# .....................................................LOGIN..........................................................................

def user_login(request):
    if 'username' in request.session:
        result = about.objects.all()
        return render(request, 'home.html', {"home": result})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)

        if user is not None:
            request.session['username'] = username

            context = {
                'users': user_data.objects.all(),
                'user': username
            }
            return render(request, 'admin_panel.html', context)

        else:
            if user_data.objects.filter(username=username, password=password).exists():
                request.session['username'] = username
                result = {
                    'home': about.objects.all(),
                    'user': username
                }
                return render(request, 'home.html', result)

            else:
                messages.info(request, 'Invalid credentials')
                return redirect('login')

    else:
        return render(request, 'login.html')

# .....................................................HOME.........................................................................


def home_page(request, user):
    if 'username' in request.session:
        result = {
            'home': about.objects.all(),
            'user': user
        }
        return render(request, 'home.html', result)
    else:
        return redirect('login')


# .....................................................UPLOAD-FILES..................................................................

def upload(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        image = request.FILES['image']
        new_user = about(name=name, desc=desc, image=image)
        new_user.save()
        return render(request, 'upload.html')
    else:
        return render(request, 'upload.html')

# .....................................................ADMIN-PANEL....................................................................


def admin_panel(request):
    if request.user.is_authenticated:
        context = {
            'users': user_data.objects.all()
        }
        return render(request, 'admin_panel.html', context)
    elif 'username' in request.session:

        context = {
            'users': user_data.objects.all()
        }
        return render(request, 'admin_panel.html', context)
    else:
        return redirect('login')

# .....................................................ADMIN-PANEL-DELETE-USER....................................................................


def delete_user(request, id):
    user_del = user_data.objects.get(id=id)
    user_del.delete()

    context = {
        'users': user_data.objects.all()
    }
    return render(request, 'admin_panel.html', context)


# .....................................................ADMIN-PANEL-EDIT-USER....................................................................


def edit_user(request, id):
    context = {
        'users': user_data.objects.get(id=id)
    }
    return render(request, 'update_user.html', context)


# .....................................................ADMIN-PANEL-UPDATE-USER....................................................................


def update_user(request, id):
    if request.method == 'POST':
        ex1 = user_data.objects.filter(id=id).update(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'])
        context = {
            'users': user_data.objects.all()
        }
        return render(request, 'admin_panel.html', context)
    return redirect('admin_panel')

# .....................................................ADMIN-PANEL-ADD-USER....................................................................


def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        pass1 = request.POST['password2']
        email = request.POST['email']

        if password == pass1:
            new_user = user_data(
                username=username, email=email, password=password)
            new_user.save()
            messages.info(request, 'New User Added')
            return redirect('add_user')

        else:
            messages.info(request, 'Password Must Match')
            return redirect('add_user')

    else:
        return render(request, 'add_user.html')

# .....................................................LOGOUT....................................................................


def LogoutPage(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')

# .....................................................search....................................................................

# def searchposts(request):
#     if request.method == 'GET':
#         query= request.GET.get('q')

#         submitbutton= request.GET.get('submit')

#         if query is not None:
#             lookups= Q(username=query) | Q(email=query)

#             results= user_data.objects.filter(lookups).distinct()

#             context={'results': results,
#                      'submitbutton': submitbutton}

#             return render(request, 'search.html', context)

#         else:
#             return render(request, 'search.html')

#     else:
#         return render(request, 'search.html')


def search_user(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        multiple_query = Q(Q(username__icontains=searched)
                           | Q(email__icontains=searched))
        users = user_data.objects.filter(multiple_query)
        context = {
            'users': users
        }
    return render(request, 'admin_panel.html', context)

    # .....................*....................*..........................*......................
