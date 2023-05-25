from django.shortcuts import render,redirect
from . models import userreg,shopreg,product,feedback,complaints,notification

# Create your views here.

def admin_login(request):
    return render(request,'login.html')
def admin_dashboard(request):
    return render(request,'dashboard.html')
def admin_approveshop(request):
    return render(request,'approveshop.html') 
def admin_complaints(request):
    return render(request,'complaints.html') 
def admin_feedback(request):
    return render(request,'feedback.html')
def admin_managecounciling(request):
    return render(request,'managecounciling.html')    
def admin_manageshop(request):
    return render(request,'manageshop.html')    

def admin_notification(request):
    return render(request,'notification.html')  
def admin_product(request):
    return render(request,'product.html')    
   

# def notification(request):
#     if request.method=='POST':
#       notification=request.POST.get('notification')
#       date=request.POST.get('date')  
#       data=notification(Name=notification,date=date)
#       data.save()          
#       return redirect('dashboard')

def admin_manageusers(request):
    data=userreg.objects.all() 
    return render(request,'manageusers.html',{'data':data})

def admin_viewuser(request):
    data=userreg.objects.all() 
    return render(request,'viewuser.html',{'data':data})


def admin_approve_users(request,id):
    data=userreg.objects.get(id=id) 
    data.userstatus=1
    data.save()
    return redirect('admin_viewuser')  

def admin_delete_user(request,id):
    data=userreg.objects.get(id=id) 
    print(data)
    data.delete()
    return redirect('admin_viewuser')  


def admin_manageshop(request):
    data=shopreg.objects.all() 
    return render(request,'manageshop.html',{'data':data})    

def admin_approveshop(request):
    data=shopreg.objects.all() 
    return render(request,'approveshop.html',{'data':data})    

def admin_approve_shop(request,id):
    data=shopreg.objects.get(id=id) 
    data.shopstatus=1
    data.save()
    return redirect('admin_approveshop')  
def admin_delete_shop(request,id):
    data=shopreg.objects.get(id=id) 
    print(data)
    data.delete()
    return redirect('admin_approveshop')   

def admin_view_product(request):
    data=product.objects.all() 
    return render(request,'product.html',{'data':data})  

def admin_view_feedback(request):
    data=feedback.objects.all() 
    return render(request,'feedback.html',{'data':data}) 

def admin_view_complaints(request):
    data=complaints.objects.all() 
    return render(request,'complaints.html',{'data':data}) 

def admin_view_notification(request):
    data=notification.objects.all() 
    return render(request,'notification.html',{'data':data}) 
       

    
