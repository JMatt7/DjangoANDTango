from django.urls import path
from .views import SignUpDetailView

urlpatterns =[
    path('signup/', SignUpDetailView.as_view(), name = 'signup'),

]