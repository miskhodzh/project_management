from django.shortcuts import render
from django.contrib.auth import authenticate

def index(request):
    template = 'accounts/index.html'
    return render(request, template)

# def login(request):
#     template = 'accounts/login.html'
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#     else:
#         form = UserLoginForm()
    
#     context = {'form': form}
#     return render(request, template)
