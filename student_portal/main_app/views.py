from django.shortcuts import render
from .models import Student
from .models import Query
# from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            user = Student.objects.filter(stu_email=email)
            if user:
                msg = "Email already exists"
                return render(request, 'login.html', {'msg': msg})
            else:
                Student.objects.create(
                    stu_name=name,
                    stu_email=email,
                    stu_contact=contact,
                    stu_password=password,
                )
                msg = "Registration successful"
                return render(request, "home.html", {'msg': msg})
        else:
            msg = "Passwords do not match"
            return render(request, 'register.html', {'msg': msg})
    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Student.objects.filter(stu_email=email)
        if user:
            user_data = Student.objects.get(stu_email=email)
            if password == user_data.stu_password:
                data = {
                    'name': user_data.stu_name,
                    'email': user_data.stu_email,
                    'contact': user_data.stu_contact,
                    'password': user_data.stu_password
                }
                query_data = Query.objects.filter(stu_email=email)
                return render(request, 'dashboard.html', {'data': data, 'query_data': query_data})
            else:
                msg = "Email & password do not match"
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = "Email not registered"
            return render(request, 'register.html', {'msg': msg})

    else:
        return render(request, 'login.html')

def query(request):
    if request.method=='POST':
        # print(request.POST)
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        query1=request.POST.get('query')
        print(name1,email1,query1)
        Query.objects.create(stu_name=name1,stu_query=query1,stu_email=email1)
        data=Student.objects.get(stu_email=email1)
        data1={'name':data.stu_name,
               'email':data.stu_email,
               'contact':data.stu_contact,
               'password':data.stu_password}
        query_data=Query.objects.filter(stu_email=email1)
        return render(request,'dashboard.html',{'data':data1, 'query_data':query_data})
    else:
        return render(request, 'dashboard.html')

def dashboard(request):
    # You can handle dashboard view here if needed
    return render(request, 'dashboard.html')

def edit(request, x):
    user_data = Query.objects.get(id=x)
    if request.method == 'POST':
        user_data.stu_name = request.POST.get('name')
        user_data.stu_email = request.POST.get('email')
        user_data.stu_query = request.POST.get('query')
        user_data.save()

        email = user_data.stu_email
        data = Student.objects.get(stu_email=email)
        my_data = {
            'name': data.stu_name,
            'email': data.stu_email,
            'contact': data.stu_contact,
            'password': data.stu_password
        }
        all_query = Query.objects.filter(stu_email=email)

        return render(request, 'dashboard.html', {
            'key': None,
            'data': my_data,
            'query_data': all_query
        })

    email = user_data.stu_email
    data = Student.objects.get(stu_email=email)
    my_data = {
        'name': data.stu_name,
        'email': data.stu_email,
        'contact': data.stu_contact,
        'password': data.stu_password
    }
    all_query = Query.objects.filter(stu_email=email)

    return render(request, 'dashboard.html', {
        'key': user_data,
        'data': my_data,
        'query_data': all_query
    })

def delete(request, pk):
    data = Query.objects.get(id=pk)
    email = data.stu_email
    data.delete()
    alldata = Query.objects.filter(stu_email=email)
    return render(request, 'dashboard.html', {
        'query_data': alldata
    })

def all_data(request):
    students = Student.objects.all()
    queries = Query.objects.all()
    return render(request, 'all_data.html', {'students': students, 'queries': queries})

def logout_view(request):
    return render(request, 'home.html', {'msg': 'Logged out successfully!'})
