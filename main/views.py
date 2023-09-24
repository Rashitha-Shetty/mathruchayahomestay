from django.shortcuts import render,redirect,HttpResponse
from . import data as db
from django.contrib import messages





def notifination(request):
    if request.method=='POST':
        id=request.POST.get('id')
        db.delete_doc(id)
    
    data=db.get_doc()
    data={'data':data}
    return render(request, 'admin.html',data)


def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phno=request.POST.get('phno')
        date_in=request.POST.get('date_in')
        date_out=request.POST.get('date_out')
        people=request.POST.get('people')
        msg=request.POST.get('msg')
        place=request.POST.get('place')
        
        print(type(date_in))
        if name==""or phno=="" or date_in=="" or date_out=="" or people=="" or place=="" or date_in>date_out:
            messages.error(request, 'Somthing Went Wrong')
            return redirect('home')  # Redirect to the same page
        
        data = {"Name": name ,"Phone_No":phno,
        "Check_In": date_in, "Check_out": date_out, "No-of-Members": people, "Custom_msg": msg,"Place":place}
        
       
        
        
        result=db.add_doc(data)
        if result:
            messages.success(request, 'Thank You! Contact For Booking Conformation')
            return redirect('home')  # Redirect to the same page
        messages.success(request, 'Somthing Went Wrong')
        return redirect('home')  # Redirect to the same page
        
        
       
   
    
    return render(request, 'home.html')