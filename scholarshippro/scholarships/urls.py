from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [ 
    path('scholarships/', views.ScholarshipsList.as_view()), 
    path('scholarships/<int:pk>/', views.ScholarshipDetail.as_view()),
    path('scholarships/favorite/<int:pk>/', views.FavoriteDetail.as_view()), 
]

urlpatterns = format_suffix_patterns(urlpatterns)