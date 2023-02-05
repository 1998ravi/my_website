from django.contrib import messages
from django.http import request
from django.shortcuts import redirect, render
from . models import post,User,Comments,enq,dem,cat
from django.shortcuts import HttpResponse


# Create your views here.
def show(request):
    k=post.objects.all()
    n=cat.objects.all()
    return render(request,'index.html',{'p':k,'c':n})
def full(request,id):
    k=post.objects.get(id=id)
    comments=Comments.objects.filter(post=k)
    print(comments)
    no=len(comments)

    return render(request,'show.html',{"p": k,"c":comments,"k":no})
def comments(request):
    if request.method=='POST':
        name=request.session.get('name')
        id=request.POST['o']
        request.session['kid']=id
    
        if name!=None:
            id=request.POST['o']
            print(id)
            print("hi")
            cmnt=request.POST['cmnt']
            data=post.objects.get(id=id)
            c=Comments(name=name,post=data,commets=cmnt)
            messages.success(request,"comnt posted")
           
            c.save()
            return redirect(f'/full/{id}')
    return render(request,'login.html')

def login(request):
    if request.method=='POST':
        email=request.POST['em']
        password=request.POST['ps']
     
        user=User()
        k=user.get_cust_email(email)
        id=request.session.get('kid')
        print(id)
        if k.password==password:
          
            messages.success(request,"user exist")
            request.session['name']=k.name
            request.session['email']=k.email
            if id==None:
                return redirect(show)
            else:
                return redirect(f'/full/{id}')
    return render(request,'login.html')
    
def logout(request):
    
    request.session.clear()
    messages.success(request,'user logout')
    return redirect(show)

def register(request):
    if request.method=='POST':
       
        name=request.POST['name']
        email=request.POST['email']
        passw=request.POST['pass']
        confimpass=request.POST['confpass']
        if len(passw)<8:
            messages.error(request,"password length must be greater then 8")
            return redirect('register')
            
        if passw!=confimpass:
            messages.error(request,"password miss matching")
            return redirect('register')
        if len(name)<5:
            messages.error(request,"name length must be 5")
            
    
        u=User.objects.filter(email=email)
        if u:
            print("exist")
        else:
            
            k=User(name=name,email=email,password=passw)
            k.save()
       
            messages.success(request,"Registered")
            
    return render(request,'register.html')

def enquiry(request):
    if request.method=='POST':
        em=request.POST['emg']
        question=request.POST['inq']
        k=enq(emailenq=em,ques=question)
        k.save()
     
        messages.success(request,"mesaage sent")
   
 
    return redirect('/')
def search(request):
    if request.method=='POST':
        query=request.POST['serch']
        if len(query)>30:
            allpst=post.objects.none()
        else:
            t=post.objects.filter(title__icontains=query)
            p=post.objects.filter(post__icontains=query)
            allpst=t.union(p)
            l=allpst.count
            
        if allpst.count==0:
            messages.warning(request,'nothing found')
        print(allpst)
        par={'allpost':allpst,'query':query}
        return render(request,'search.html',par)   
    return render(request,'search.html')

def add(request):
    c=cat.objects.all()
    if request.method=='POST':
   
        if request.session.get('email'):
            catem=request.POST['category']
         
            categor=cat.objects.get(category=catem)
            n=request.session.get('email')
            k=User.objects.get(email=n)
            name=k.name
            j=request.FILES['myfile']
            tittle=request.POST['tittle']
            
            
            para=request.POST['para']
            print(para)
            pos=post(title=tittle,post=para,user=name,email=n,Image=j,cate=categor)
            pos.save()
            
        else:
            return redirect(login)
    m=request.session.get('email')
 
    k=post.objects.filter(email=m)
   
    return render(request,'addpost.html',{'post':k,"cat":c})
def de(request,id):
    if request.method=='POST':
        d=post.objects.get(id=id)
        d.delete()
        return redirect(add)
    return render(request,'index.html')
def showbycat(request,id):
    j=cat.objects.get(id=id)
    
    t=post.objects.filter(cate=j)
    if len(t)==0:
      return render(request,'category.html',{'msg':"Nothing found"})


    return render(request,'category.html',{'p':t})
