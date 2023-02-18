from django.urls import path
from employee import views


urlpatterns = [

    path('employee/add', views.EmployeeCreateView.as_view(), name='add-employee'),
    path('employee/list', views.EmployeeListView.as_view(), name='list-employee'),
    path('employee/<int:id>', views.EmployeeDetail.as_view(), name='detail-employee'),
    path('employee/<int:id>/remove', views.EmployeeDelete.as_view(), name='delete-employee'),
    path('', views.IndexView.as_view(), name='home'),
    path('login', views.SigninView.as_view(), name='signin'),
    path('signup', views.SignupView.as_view(), name='register'),



]
