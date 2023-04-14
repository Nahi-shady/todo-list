from django.urls import path, include
from .views import RegisterPage, TaskList, TaskDetail,  TaskCreate, TaskUpdate, TaskDelete, CustomLogin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
]
