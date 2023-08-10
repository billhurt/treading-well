from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "booking"

urlpatterns = [
    path('', TemplateView.as_view(template_name="booking/index.html"), name='index'),
    path('treatments/', TemplateView.as_view(template_name="booking/treatments.html"), name='treatments'),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('success/', TemplateView.as_view(template_name="booking/success.html"), name="success")
]