from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User,Comment,info
from django.shortcuts import render,HttpResponse,redirect
import jwt, datetime
from datetime import date
from email.message import EmailMessage
import smtplib
import random
import asyncio

from .forms import GeeksForm
def user_searching(request):
    token = request.COOKIES.get('jwt')

    if not token:
        return HttpResponse('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        return HttpResponse('Unauthenticatede!')
    data = {'id':payload['id']}
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']

        user_searching_name = info.objects.filter(usernames=username).first()
        print(user_searching_name)
        if user_searching_name is None:
            user_searching_name = info.objects.filter(phone=username).first()
            if user_searching_name is None:
                return HttpResponse('No user')
            
        data = {'id_user':payload['id'],'friend':user_searching_name}
        return render(request,'articals/friend_searching_found.html',data)
    else:

        return render(request,'articals/friend_searching.html',data)
def settings(request):
    token = request.COOKIES.get('jwt')

    if not token:
        return HttpResponse('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        return HttpResponse('Unauthenticated!')
        id_user = {'id':payload['id']}
    return render(request,'articals/settings.html')

def chats(request,id):
    pass

def messages(request,id):
    pass

async def pay(request):
    while True:
        await asyncio.sleep(2)
        print('Hello world')

def chek_email(request,id):
    if request.method == 'POST':
        user = User.objects.filter(id=id).first()

        cods = request.POST['cod']

        cod = user.email_cod
        if cod == cods:
            user.email_chek = 'Truest'
            user.save()
            payload = {
                'id': id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60000),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
            z = datetime.datetime.utcnow() + datetime.timedelta(minutes=600000)
            user = User.objects.filter(id = payload['id']).first()
            info_user = user.info_set.filter(user_prof_id = payload['id']).first()
            if info_user is None:

                response = redirect('http://127.0.0.1:8000/user/add_dannie') # replace redirect with HttpResponse or render
                response.set_cookie('jwt', token, max_age=100000000,httponly=True)
                return response
            else: 
                response = redirect('http://127.0.0.1:8000/user/'+str(payload['id'])) # replace redirect with HttpResponse or render
                response.set_cookie('jwt', token, max_age=100000000,httponly=True)
                return response
        else:
            return render(request,'articals/log_sequr_non.html')
    else:
    
        return render(request,"articals/login_sequriti.html")




def send_emails(email):
        login = 'pasaharpsuk@gmail.com'
        password = 'Boda1006'

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        try:
            em = EmailMessage()

            server.login(login,password)
            rand = str(random.randint(100000,999999))
            msg = f'Ваш код: {rand}'
            em.set_content("{}".format(msg))
            to_ = email
            from_ = 'pasaharpsuk@gmail.com'
            subject = 'Код подтверждение с сайта BodaShop.com'
            em['Subject'] = subject
            em['From'] = from_
            em['To'] = to_
            global cod 
            cod = rand
            server.send_message(em)
            
            

        except Exception as err:
            print(err)


def add_comment(request):
    if request.method == 'POST':
        print(request.POST)
        token = request.COOKIES.get('jwt')

        if not token:
            return HttpResponse('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            return HttpResponse('Unauthenticated!')
        
        id = payload['id']      
        post_id = request.POST['post_id']
        post_id = int(post_id)
        user = User.objects.filter(id=id).first()
        users = user.info_set.filter(user_prof_id=id).first()
        test = Comment.objects.all()

        text_comm = request.POST['text_com']
        text_comm = text_comm.replace(' ','_')
        if text_comm != '':
            test = Comment.objects.all()

        
            datas = date.today()
            

            test.create(name_user=users.name + '_' + users.last_name,id_user=user.id,text_comm=text_comm,data_comment=datas,post_id_id=post_id)
            return redirect(request,'http://127.0.0.1:8000/user/'+str(payload['id']))    
        else:
            return redirect(request,'http://127.0.0.1:8000/user/'+str(payload['id']))    
    else:
        return HttpResponse("d,exs")    

def logout(request):
    response = HttpResponse("Logout securiti")
    response.delete_cookie('jwt')
    
    return response
def create_prof_user(request):
    token = request.COOKIES.get('jwt')

    if not token:
        return HttpResponse('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        return HttpResponse('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    users = user.info_set.filter(user_prof_id=payload['id']).first()
    if request.method == 'POST':
        print(request.FILES)
        image = request.FILES["geeks_field"]
        print(image)
        post = request.POST
        phone = post['phone']
        if post['usernames'] == '':
            username = post['phone']
        else:
            username = post['usernames']
        user_info = info.objects.filter(usernames=username).first()
        user_info_searching_phone = info.objects.filter(phone=phone).first()
        
        if user_info_searching_phone is None:
            print('1000')
        else:
            print('Hello world')
            if phone !=users.phone:
                return HttpResponse('такой phone уже есть')
            else:
                print('Вось так как то')





        if user_info is None:
            print('1000')
        else:
            print('Hello world')
            if username !=users.usernames:
                return HttpResponse('такой username уже есть')
            else:
                print('Вось так как то')
        if not users:
            

            user.info_set.create(name=post['username'],last_name=post['last_name'],pol=post['pol'],year=post['year'],o_sebe=post['info'],ville=post['ville'],phone=post['phone'],usernames=usernmame)
            return redirect('http://127.0.0.1:8000/user/'+str(payload['id']))
        else:
            form = GeeksForm(request.FILES)
            img = request.FILES['geeks_field']
            users.image = img
            post = request.POST
            users.name=post['username']
            users.last_name=post['last_name']
            users.pol=post['pol']
            users.year=post['year']
            users.o_sebe=post['info']
            users.ville=post['ville']
            users.phone=post['phone']
            users.usernames=username
            users.save()
            return redirect('http://127.0.0.1:8000/user/'+str(payload['id']))
    else:
        if users is None:
            
            return render(request,'articals/list_3.html')
        else:
            context = {}
            form = GeeksForm()
            user = {'user':users,'info':users.o_sebe,'form':form,'id':payload['id']}
            return render(request,'articals/list_4.html',user)
def prof(request,id):
    if not request.method == 'POST':
            token = request.COOKIES.get('jwt')

            if not token:
                return HttpResponse('Unauthenticated!')

            try:
                payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            except jwt.ExpiredSignatureError:
                return HttpResponse('Unauthenticated!')

           
            ids = payload['id']
            if id == ids:
                user = User.objects.filter(id=payload['id']).first()
                useres = user.post_set.filter(user_prof_id=payload['id'])
                usere = user.info_set.filter(user_prof_id=payload['id']).first()
                test = Comment.objects.all()
                list_test = []
                slovar = {}
                for g in range(0,len(test)):
                    b = test[g]
                    b = str(b)
                    b = b.split()
                    for i in range(0,len(b)):
                        
                        
                        if i % 5 == 0:
                            b[i-4] = b[i-4].replace('_',' ')
                            print(b[i-4])
                            slovar = {'name':b[i-5],'text':b[i-4],'id':int(b[i-3]),'date':b[i-2],'id_user':b[i-1]}

                            list_test.append(slovar)
                            slovar = {}
                useree = {'user':usere,'post':useres,'com':list_test,'id':payload['id']}
                if not usere:            
                    return render(request,'articals/prof_null.html',useree)
                if not useres:
                    return render(request,'articals/prof.html',useree)
                    print(1)
                else: 
                    return render(request,'articals/prof_2.html',useree)
                    print(2)
            else:
                test = Comment.objects.all()

                list_test = []
                slovar = {}
                for g in range(0,len(test)):
                    b = test[g]
                    b = str(b)
                    b = b.split()
                    for i in range(0,len(b)):
                        b[i] = b[i].replace('_',' ')
                        
                        if i % 5 == 0:
                            slovar = {'name':b[i-5],'text':b[i-4],'id':int(b[i-3]),'date':b[i-2],'id_user':b[i-1]}
                            list_test.append(slovar)
                            slovar = {}
                user = User.objects.filter(id=id).first()

                usere = user.info_set.filter(user_prof_id=id).first()
                useres = user.post_set.filter(user_prof_id=id)
                useree = {'user':usere,'post':useres,'com':list_test,'id':payload['id']}
                if not usere:            
                    return render(request,'articals/prof_null.html',useree)
                
                else: 
                    return render(request,'articals/prof_stranger.html',useree)
    else:
        user = User.objects.filter(id=id).first()

        info = request.POST
        datas = 'datetime.today()'
        user.post_set.create(name_post=info['name_stat'],text_post=info['text_stat'],date_public=datas)
        user = User.objects.filter(id=id).first()
        useres = user.post_set.filter(user_prof_id=id)
        usere = user.info_set.filter(user_prof_id=id).first()
        test = Comment.objects.all()
        list_test = []
        slovar = {}
        for g in range(0,len(test)):
            b = test[g]
            b = str(b)
            b = b.split()
            for i in range(0,len(b)):
                b[i] = b[i].replace('_',' ')
                        
                if i % 5 == 0:
                    slovar = {'name':b[i-5],'text':b[i-4],'id':int(b[i-3]),'date':str(b[i-2]),'id_user':b[i-1]}

                    list_test.append(slovar)
                    slovar = {}
        useree = {'user':usere,'post':useres,'com':list_test,'id':payload['id']}
        if not usere:            
            return render(request,'articals/prof_null.html',useree)
        if not useres:
            return render(request,'articals/prof.html',useree)
        else: 
            return render(request,'articals/prof_2.html',useree)
    
        

        

                
       
def logireg(request):
    token = request.COOKIES.get('jwt')

    if not token:

            

        if request.method == 'POST':
            email = request.POST['email']

            login = User.objects.filter(email=email).first()
            password = request.POST['passworg']
            email = request.POST['email']
            dats = {'password':password,'email':email,'email_chek':'Nonest'}
            if login is None:
                

            
                try:
                    serializer = UserSerializer(data=dats)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return redirect('http://127.0.0.1:8000/user/logine')

                except:
                    return HttpResponse("Некоректные данные!")
            else:

                return HttpResponse('Такой пользователь уже есть!')
        else:
            return render(request,'articals/list_2.html')
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        return redirect('http://127.0.0.1:8000/user/'+str(payload['id']))
    except jwt.ExpiredSignatureError:
        return HttpResponse('Просрочено!')


def login(request):
    token = request.COOKIES.get('jwt')

    if not token:
        if request.method == 'POST':

            email = request.POST['email']
            password = request.POST['password']
            print(request.POST)

            user = User.objects.filter(email=email).first()

            if user is None:
                return HttpResponse('No to user')

            if not user.check_password(password):
                return HttpResponse('No Paaword')
            user_chek = user.email_chek
            print(user_chek)
            if user_chek == 'Nonest':
                send_emails(email)
                user.email_cod = cod
                user.save()
                return redirect('http://127.0.0.1:8000/user/email_sequriti/'+str(user.id))
            else:
            
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
                    'iat': datetime.datetime.utcnow()
                }
                token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
                z = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                user = User.objects.filter(id = payload['id']).first()
                info_user = user.info_set.filter(user_prof_id = payload['id'])
                
                if info_user is None:

                    response = redirect('http://127.0.0.1:8000/user/add_dannie') # replace redirect with HttpResponse or render
                    response.set_cookie('jwt', token, max_age=100000000,httponly=True)
                    return response
                else:


                        
                    response = redirect('http://127.0.0.1:8000/user/'+str(payload['id'])) # replace redirect with HttpResponse or render
                    response.set_cookie('jwt', token, max_age=100000000,httponly=True)
                    return response
        else:
            return render(request,'articals/logine.html')
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        return redirect('http://127.0.0.1:8000/user/'+str(payload['id']))
    except jwt.ExpiredSignatureError:
        return HttpResponse('Просрочено!')
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response