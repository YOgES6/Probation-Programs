from django.urls import include, path
from rest_framework import routers
from hotel import views 
from hotel.views import Serial


router=routers.DefaultRouter()
#router.register(r'users' , views.UserViewSet)
#router.register(r'hotel' , views.Serial)

app_name='hotel'
book_list = Serial.as_view({'get':'list'})
book_detail = Serial.as_view({'get':'retrieve'})

user_list = Serial.as_view({'get':'list'})
user_detail = Serial.as_view({'get':'retrieve'})

group_list = Serial.as_view({'get':'list'})
group_detail = Serial.as_view({'get':'retrieve'})


urlpatterns = [
    path('', include(router.urls)),
    
    path('serial/',book_list),
    path('serial/<int:id>',book_detail),
    
    path('user/',user_list),
    path('user<int:id>',user_detail),
    
    path('group/',group_list),
    path('group/<int:id>',group_detail),
    
    path('book_post/',views.book_post,name='post'),
    path('book_update/<int:pk>',views.book_update,name='update'),
    
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
