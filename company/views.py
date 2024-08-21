from django.shortcuts import render, HttpResponse, redirect
from .models import register

# Create your views here.
def registerpage(request):
    if request.method == 'POST':
        getname = request.POST['name']
        getaddress = request.POST['address']
        getusername = request.POST['username']
        getpassword = request.POST['password']
        users = register()
        users.Name = getname
        users.Address = getaddress
        users.Username = getusername
        users.Password = getpassword
        users.save()

    return render(request, 'register.html')
#code for user login
def userlog(request):
    if request.method =='POST':
        getusername = request.POST['username']
        getpassword = request.POST['password']
        try:
            register.objects.get(Username=getusername,Password=getpassword)
            return HttpResponse('Welcome User')
        except:
            return HttpResponse('Invalid User')
    return render(request, 'userlogin.html')

# code for admin login
def adminlog(request):
    if request.method == 'POST':
        getusername = request.POST['username']
        getpassword=request.POST['password']
        if getusername == 'admin' and getpassword == 'admin':
            return redirect('/adminhome')
        else:
            return HttpResponse('Invalid Credentials')
    return render(request,'adminlogin.html')

#code for admin home
def adminhome(request):
    return render(request,'adminhome.html')

#code for pending data
def pending(request):
    details = register.objects.filter(Status=False)
    return render(request,'pendinglist.html',{'value':details})

#code for approve status
def approve(request,id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pending')

#code for approved data
def approved(request):
    details = register.objects.filter(Status=True)
    return render(request, 'approvelist.html', {'value': details})

#code for displaying all data
def operations(request):
    details = register.objects.all()
    return render(request,'operations.html',{'value': details})

#code for update particular data
def edit(request,id):
    details = register.objects.all()
    user_data = register.objects.get(id=id)
    if request.method == 'POST':
        getaddress = request.POST['address']
        getpassword = request.POST['password']
        user_data.Address = getaddress
        user_data.Password = getpassword
        user_data.save()
        return redirect('/operations')
    return render(request,'operations.html',{'value':details,'data':user_data})

#code for delete particular data
def delete(request,id):
    data = register.objects.get(id=id).delete()
    return redirect('/operations')

#code for upload files 
def upload (request):
    if request.method == 'POST':
        getname = request.POST['name']
        getmail = request.POST['mail']
        getdesigination = request.POST['designation']
        getpicture = request.FILES['img']
        getdocument = request.FILES['doc']
        fileupload(Name=getname,Mail=getmail,Designation=getdesigination,Picture=getpicture,Document=getdocument).save()
    return render(request,'uploadfile.html')

#code for download files
def downfile(request):
    data = fileupload.objects.all()
    return render(request,'downloadfile.html',{'value':data})