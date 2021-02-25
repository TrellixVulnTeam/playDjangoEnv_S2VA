from django.shortcuts import render
#from django.http import HttpResponse
#from userModel_app_1184099.models import User
from userModel_app_1184099.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def users(request):
    #user_list = User.objects.order_by('first_name')
    #user_dict = {"users":user_list}
    #return render(request,'users.html',context=user_dict)

    form = NewUserForm()

    #Jika user menekan tombol submit maka
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR: FORM INVALID")
    
    return render(request,'users.html',{'form':form})