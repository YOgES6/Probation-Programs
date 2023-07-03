from django.urls import include, path
from rest_framework import routers
from hotel import views 
from hotel.views import Serial,User,Register,UserList,UpdateUser,List

router=routers.DefaultRouter()
#router.register(r'users' , views.UserViewSet)
#router.register(r'hotel' , views.Seria
app_name='hotel'
book_list = Serial.as_view({'get':'list'})
book_detail = Serial.as_view({'get':'retrieve'})



urlpatterns = [
    path('', include(router.urls)),

    path('serial/',book_list),
    path('serial/<int:id>',book_detail),

    path('register/',Register.as_view()),
    path('users/', UserList.as_view(queryset=User.objects.all()), name='user-list'),
    path('userupdate/', UpdateUser.as_view(queryset=User.objects.all()), name='updateuser'),

    path('list/', List.as_view(), name='list'),

    path('post/',views.post,name='post'),
    path('update/<int:pk>',views.update,name='update'),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
