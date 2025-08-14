from django.urls import path
from .views import IndexView, ProductShowView, ProductCreateView, ContactPageView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:id>/', ProductShowView.as_view(), name='show'),
    path('products/create/', ProductCreateView.as_view(), name='form'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]
