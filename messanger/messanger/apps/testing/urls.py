from django.urls import path
from . import views
app_name = "article"
from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView,logireg,login,prof,create_prof_user,logout,chek_email,pay,settings,user_searching
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logoutE', LogoutView.as_view()),
    path('logine', views.login),
    path('',views.logireg,name = 'registere'),
    path('<int:id>', views.prof),
    path('add_dannie',views.create_prof_user),
    path('logout',views.logout),
    path('add_comment',views.add_comment),
    path('email_sequriti/<int:id>',views.chek_email),
    path('pay', views.pay),
    path('settings',views.settings),
	path('friend',views.user_searching)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Крч Богдан У тебя баг все идет не только user/23 a может и просто ""  щас занят подтв почты займись ты этим(Я из прошлого)