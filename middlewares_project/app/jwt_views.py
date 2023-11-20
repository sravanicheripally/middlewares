# # myapp/views.py

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
# from .utils import create_jwt_token, verify_jwt_token
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login

# def login_view(request):
#     # Perform user authentication (customize this based on your needs)
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(username,"views..............")
#             user=authenticate(request,username=username,password=password)
#             # If authentication is successful, create a JWT token
#             if user.is_authenticated:
#                 login(request,user)
#                 jwt_token = create_jwt_token(user)
#                 print(jwt_token,"jwt token.................")
#                 return JsonResponse({'token': jwt_token})
#             else:
#                 return JsonResponse({'error': 'Authentication failed'}, status=401)
#     else:
#         form = AuthenticationForm()

#     return render(request, 'login.html', {'form': form})
#     user = request.user  # Replace this with your actual authentication logic

    
# @login_required
# def protected_view(request):
#     # Access the authenticated user
#     user = request.user
#     return JsonResponse({'message': f'Hello, {user.username}!'})


# myapp/views.py

from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .utils import create_tokens, verify_access_token, verify_refresh_token
from django.contrib.auth import authenticate, login,logout
from .utils import BLACKLISTED_TOKENS
def login_view(request):
    # Perform user authentication (customize this based on your needs)
    user = request.user  # Replace this with your actual authentication logic

    # If authentication is successful, create access and refresh tokens
    if user.is_authenticated:
        access_token, refresh_token = create_tokens(user)
        return JsonResponse({'access_token': access_token, 'refresh_token': refresh_token})
    else:
        return JsonResponse({'error': 'Authentication failed'}, status=401)

@login_required
def protected_view(request):
    # Access the authenticated user using the access token
    access_token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    user = verify_access_token(access_token)

    if user:
        return JsonResponse({'message': f'Hello, {user.username}!'})
    else:
        return JsonResponse({'error': 'Invalid access token'}, status=401)

def refresh_token_view(request):
    # Get the refresh token from the request
    refresh_token = request.POST.get('refresh_token')

    # Verify the refresh token
    user = verify_refresh_token(refresh_token)

    if user:
        # If refresh token is valid, create a new access token
        access_token, _ = create_tokens(user)
        return JsonResponse({'access_token': access_token})
    else:
        return JsonResponse({'error': 'Invalid refresh token'}, status=401)
    
def logout_view(request):
    # Get the access token from the request
    access_token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

    # Add the access token to the blacklist
    BLACKLISTED_TOKENS.add(access_token)

    return JsonResponse({'message': 'Logout successful'})
