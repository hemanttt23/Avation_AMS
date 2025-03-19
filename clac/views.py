from django.shortcuts import render
from django.http import HttpResponse
#import mysql.connector as sq
# Create your views here.


def home(request):

    return render(request,'index.html')
def pay(request):

    return render(request,'Payment.html')

def about(request):

    return render(request,'about.html')

def booking(request):

    return render(request,'booking.html')

def final(request):

    return render(request,'final.html')

def login(request):

    return render(request,'login.html')

def regist(request):
    #if request.method == 'POST':
        #name=request.POST['name']
        #password=request.POST['Passsword']
        #email_id=request.POST['email_id']
        #m=sq.connect(host='localhost',user='root',passwd='ajps',databse='ams')
        #cursor=m.cursor()
        #d=request.POST
        #for key,value in d.items():
            #if key=='name':
            #    fn=values
            #if key==password:
            #    password=value
            #if key==email_id:
            #    email_id=value
        #c="insert into register Values('{}','{}','{}')".format(name,password,email_id)
        #cursor.execute(c)
        #m.commit()

    return render(request,'register.html')


def thank(request):

    return render(request,'Thank you.html')

def tour(request):

    return render(request,'tour.html')
