from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.template import loader
from .forms import ContactForm
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.

class ContactView(FormView):
    
    template_name = "booking/contact.html"
    form_class = ContactForm
    success_url = "../success/"
    
    def form_valid(self, form):
        name=form.cleaned_data.get('name')
        email=form.cleaned_data.get('email')
        message=form.cleaned_data.get('message')
        send_mail(
            subject=f'Treadwell contact message from {name}',
            message=f"Sender's email address: {email} \n\n Sender's name: {name} \n\n Their message: \n\n" + message,
            from_email=email,
            recipient_list=['william.hurt6@gmail.com', 'treadwellfootcare@outlook.com'],
        )
        return super(ContactView, self).form_valid(form)