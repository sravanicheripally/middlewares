from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from app.views import login_view
from django.shortcuts import render, HttpResponseRedirect
# # class SimpleMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         # Code to be executed for each request before
# #         # the view (and later middleware) are called.
# #         print("This is a custom middleware!")

# #         response = self.get_response(request)

# #         # Code to be executed for each request/response after
# #         # the view is called.

# #         return response


# # class SecondSimpleMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         # Code to be executed for each request before
# #         # the view (and later middleware) are called.
# #         print("This is a second custom middleware!")

# #         response = self.get_response(request)
# #         print("after views")
# #         # Code to be executed for each request/response after
# #         # the view is called.

# #         return response


# # class MyTemplateResponseMiddleware:
# #   def __init__(self, get_response):
# #     self.get_response = get_response

# #   def __call__(self, request):
# #     response = self.get_response(request)
# #     return response

# #   def process_template_response(self, request, response):
# #     print("Process Template Response From Middleware")
# #     response.context_data['name'] = 'Sonam'
# #     return response







# # # yourapp/middleware.py
# # class AuthenticationMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         # Check if the user is authenticated
# #         print(request.user,"----------")
        
# #         if not request.user.is_authenticated:
# #             pass
            
# #             # If not authenticated, redirect to a login page or any other desired page
# #             # return redirect(reverse('login'))  # 'login' should be replaced with your login URL name
        
# #         response = self.get_response(request)
# #         print(response,"response")
# #         return response




# # yourapp/middleware.py

# from django.shortcuts import redirect
# from django.urls import reverse

# class AuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Check if the user is authenticated
        
#         allowed_user = ("ss")
#         # if not request.user.is_authenticated:
#         #     # If not authenticated, redirect to a login page or any other desired page
#         #     print('login') # 'login' should be replaced with your login URL name

#         # # Check if the authenticated user is the specific user you want to allow
#         #  # Replace with the username of the allowed user
#         # print(request.user.username,"uuuuuu")
#         if hasattr(request,"field_data"):
#             username=request.field_data.get("username")
#             password=request.field_data.get("password")
#             print(username,password)
#         # if request.user.username not in allowed_user:
#         #     print(request,"middleware")
#         #     print(request.user,"usserrrrrr")
#         #     print(request.user.username,"---")
#         #     print(request.user,"from view")
            
#         #     # If not the allowed user, redirect to a different page (e.g., permission denied)
#         #     return HttpResponseRedirect('log')
#         # else:
#         #     return HttpResponseRedirect('home')
#        # Replace with your desired URL name
#         response = self.get_response(request)
#         return response

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import resolve

# class AuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Check if the user is trying to log in
#         if resolve(request.path_info).url_name == 'login' and request.method == 'POST':
#             # Extract credentials from the request
#             username = request.POST.get('username')
#             password = request.POST.get('password')
            
#             # Authenticate user
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 # Check if the user is authorized (replace this with your authorization logic)
#                 allowed_user = "ss"
#                 if user.username == allowed_user:
#                     # Log in the user
#                     login(request, user)
#                     return redirect('/home')  # Redirect to home page after successful login
#                 else:
#                     return redirect('/log')
#             #         messages.error(request, 'Unauthorized user.')
#             # else:
#             #     messages.error(request, 'Authentication failed.')

#             # If authentication or authorization fails, redirect back to the login page
#         else:
#             messages.error(request, 'Invalid username or password.')
#             return redirect('/')

#         # For all other requests, pass them through to the next middleware or view
#         response = self.get_response(request)
#         return response

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import resolve

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # List of allowed users
        self.allowed_users = ["ss", "priya", "user3"]

    def __call__(self, request):
        # Check if the user is trying to log in
        if resolve(request.path_info).url_name == 'login' and request.method == 'POST':
            # Extract credentials from the request
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Check if the user is in the list of allowed users
                if user.username in self.allowed_users:
                    # Log in the user
                    login(request, user)
                    return HttpResponseRedirect('/home')  # Redirect to home page after successful login
                else:
                    return redirect('/log')
                    # messages.error(request, 'Unauthorized user.')
            else:
                messages.error(request, 'Authentication failed.')

            # If authentication or authorization fails, redirect back to the login page
            return redirect('/')

        # For all other requests, pass them through to the next middleware or view
        response = self.get_response(request)
        return response
