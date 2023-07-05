"""CARDCONTROL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('', views.ShowCardView.as_view()),
    path('card-add/', views.CardAddView.as_view()),
    path('<int:pk>/detail-card/', views.DetailCardView.as_view()),
    path('<int:pk>/detail-card/delete/', views.CardDeleteView.as_view()),
    path('<int:pk>/detail-card/edit/', views.CardEditView.as_view()),
    path('generation-card/', views.CardGenerationView.as_view()),
    # path('purchase/', views.PurchaseView.as_view())

]
