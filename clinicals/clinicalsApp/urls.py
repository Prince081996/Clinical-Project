from django.urls import path
from . import views


urlpatterns=[
      path('',views.PatientListView.as_view(),name = 'index'),
      path('create/',views.PatientCreateView.as_view(),name='PatientCreateView'),
      path('update/<int:pk>/',views.PatientUpdateView.as_view(),name='PatientUpdateView'),
      path('delete/<int:pk>/',views.PatientDeleteView.as_view(),name='PatientDeleteView'),
      path('adddata/<int:pk>/',views.add_data),
      path('analyze/<int:pk>/',views.analyze),

      
]