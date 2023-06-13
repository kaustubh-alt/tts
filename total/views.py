from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout
from datetime import date
from .models import client
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from datetime import date
from datetime import datetime

today = date.today()



def Login_page(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']   
        user = authenticate(request , username=username , password=password )
        if user is not None:
            #print('authenticate')
            login(request, user)
            global usr
            usr = user
            return redirect('dashboard')
        else:
            context = {'msg' : 'Login not successfull . Try Again','color':'danger'}
            return render(request , 'login.html' , context)
    
    return render(request , 'login.html')


def match(query , data):
    print(data)
    if(query.lower() in data.name.lower() or query.lower() in data.domainname.lower()):
        return True


@login_required
def lists(request):
    if request.method == 'POST':
        q = request.POST['q']
        props = client.objects.all().order_by('name')
        fildata = [item for item in props if match(q,item)]
        context = {'props':fildata}
        return render(request , 'lists.html',context)
    else:
        props = client.objects.all().order_by('name').values()
        context = {'props':props}
        return render(request , 'lists.html',context)

def Logout_request(request):
	logout(request)
	return redirect("login")


def lastdays(datee):
    if datee == None:
        return False
    else:
        str_d2 = str(datee)
        d1 = date.today()
        int_d2 = datetime.strptime(str_d2, "%Y-%m-%d")
        d2 = int_d2.date()
        diff = d2 - d1
        print(diff.days)
        if diff.days <= 30 and diff.days >= 0:
            print(diff.days)
            return True

@login_required
def dashboard(request):
    pro1 = client.objects.only("domainname", "domainexpiry").order_by('domainexpiry')
    pro2 = client.objects.only("domainname", "hostexpiry").order_by('hostexpiry')
    pro3 = client.objects.only("domainname", "emailexpiry").order_by('emailexpiry')
    prop1 = [item for item in pro1 if lastdays(item.domainexpiry)]
    prop2 = [item for item in pro2 if lastdays(item.hostexpiry)]
    prop3 = [item for item in pro3 if lastdays(item.emailexpiry)]

    context = {'domain':prop1 , 'host':prop2 , 'email': prop3}
    return render(request , 'dashboard.html' , context)



@login_required
def form(request):
     if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        mail = request.POST['mail']
        location = request.POST['location']
        domain = request.POST['domain']
        domainname = request.POST['domainname']
        domainpurchase = request.POST['domainpurchase']
        domainexpiry = request.POST['domainexpiry']
        host = request.POST['hosting']
        hostpurchase = request.POST['hostpurchase']
        hostexpiry = request.POST['hostexpiry']
        if 'emailcheck' in request.POST:
            emailtype = request.POST['emailtype']
            email = request.POST['email']
            emailcompany = request.POST['emailprovider']
            emailpurchase =request.POST['emailpurchase']
            emailexpiry = request.POST['emailexpiry']
            inst = client(name=name,date=today,phone=phone,mail=mail,
                          location=location,domain=domain,domainname=domainname,
                          domainpurchase=domainpurchase,domainexpiry=domainexpiry,host=host,
                          hostpurchase=hostpurchase,hostexpiry=hostexpiry,emailtype=emailtype,
                          email=email,emailcompany=emailcompany,emailpurchase=emailpurchase,
                          emailexpiry=emailexpiry)
            inst.save()
            context = {'msg' : 'Data stored succesfully','color':'success'}
            return render(request , 'form.html' , context)
        
        else:
            inst = client(name=name,date=today,phone=phone,mail=mail,
                          location=location,domain=domain,domainname=domainname,
                          domainpurchase=domainpurchase,domainexpiry=domainexpiry,host=host,
                          hostpurchase=hostpurchase,hostexpiry=hostexpiry)
            inst.save()
            context = {'msg' : 'Data stored succesfully','color':'success'}
            return render(request , 'form.html' , context)
     
     return render(request , 'form.html')

@login_required
def infochg(request):
    id = request.GET['id']
    if request.method == 'POST':
        obj = props = client.objects.get(id = id)
        name = request.POST['name']
        phone = request.POST['phone']
        mail = request.POST['mail']
        location = request.POST['location']
        domain = request.POST['domain']
        domainname = request.POST['domainname']
        domainpurchase = request.POST['domainpurchase']
        domainexpiry = request.POST['domainexpiry']
        host = request.POST['hosting']
        hostpurchase = request.POST['hostpurchase']
        hostexpiry = request.POST['hostexpiry']
        if 'emailcheck' in request.POST:
            emailtype = request.POST['emailtype']
            email = request.POST['email']
            emailcompany = request.POST['emailprovider']
            emailpurchase =request.POST['emailpurchase']
            emailexpiry = request.POST['emailexpiry']

            #updating

            obj.name=name
            obj.phone=phone
            obj.mail=mail
            obj.location=location
            obj.domain=domain
            obj.domainname=domainname
            obj.domainpurchase=domainpurchase
            obj.domainexpiry=domainexpiry
            obj.host=host
            obj.hostpurchase=hostpurchase
            obj.hostexpiry=hostexpiry
            obj.emailtype=emailtype
            obj.email=email
            obj.emailcompany=emailcompany
            obj.emailpurchase=emailpurchase
            obj.emailexpiry=emailexpiry
            obj.save()
        else:
            obj.name=name
            obj.phone=phone
            obj.mail=mail
            obj.location=location
            obj.domain=domain
            obj.domainname=domainname
            obj.domainpurchase=domainpurchase
            obj.domainexpiry=domainexpiry
            obj.host=host
            obj.hostpurchase=hostpurchase
            obj.hostexpiry=hostexpiry
            obj.save()
            print('updated')
            context = {'msg' : 'Data stored succesfully','color':'success'}
        return redirect('list')

    else:
        props = client.objects.values().filter(id = id)
       
        context = {'info' : props}
        return render(request , 'editinfo.html' , context)
    
def Log(request):
    return render(request , 'temp.html')


def back(request):
    fil = request.GET['obj']
    props = client.objects.filter(id=fil)
    context = {'obj': props} 
    return render(request , 'back.html' , context)

def delete(request, id):
  member = client.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('list'))