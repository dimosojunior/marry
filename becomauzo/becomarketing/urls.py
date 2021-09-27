from django.urls import path
from .import views


urlpatterns = [

   
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    
    path('<slug:category_slug>/', views.blog, name="product_by_category"),
    path('add_to_cart/<int:id>/<slug>/', views.add_to_cart, name="add_to_cart"),
    path('remove_from_cart/<int:id>/<slug>/', views.remove_from_cart, name="remove_from_cart"),
    path('order_summary', views.OrderSummaryView.as_view(), name="order_summary"),
    path('remove_single_from_cart/<int:id>/<slug>/', views.remove_single_from_cart, name="remove_single_from_cart"),
   
   
    path('<int:id>/<slug:slug>/', views.blog_detail, name="blog_detail"),
   
    
   
   

 
    
    
 
    
 
]