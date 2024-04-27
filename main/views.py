from django.shortcuts import render,redirect,HttpResponse
from . import data as db
from django.contrib import messages
import os

# from dotenv import load_dotenv
# load_dotenv()

def top():
    data=db.get_doc()
    d=[]
    for i in range(3):
        try:
            d.append(data[i])
        except:
            break
        
    data={'data':d}
    return data

def notifination(request,key=""):

    
    if key==os.getenv('NOT_KEY'):
        if request.method=='POST':
            id=request.POST.get('id')
            db.delete_doc(id)
        
        data=db.get_doc()
        data={'data':data,"key":os.getenv('NOT_KEY')}
        return render(request, 'admin.html',data)
    
    data=db.get_doc()
    data=top()
    return render(request, 'home.html',data)

def feedbacks(request):
    data=db.get_doc()
    data={'data':data}
    return render(request, 'feedbacks.html',data)

def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        # phno=request.POST.get('phno')
        # date_in=request.POST.get('date_in')
        # date_out=request.POST.get('date_out')
        Ratings=request.POST.get('Ratings')
        msg=request.POST.get('msg')
        # place=request.POST.get('place')
        
        # print(type(date_in))
        if name=="":
            messages.error(request, 'Somthing Went Wrong')
            return redirect('home')  # Redirect to the same page
        
        data = {"Name": name , "Ratings": Ratings, "Custom_msg": msg}
        
       
        
        
        result=db.add_doc(data)
        if result:
            messages.success(request, 'Thank You For Responding!')
            return redirect('home')  # Redirect to the same page
        messages.success(request, 'Somthing Went Wrong')
        return redirect('home')  # Redirect to the same page
        
        
       
   
    
        
    data=top()
    return render(request, 'home.html',data)