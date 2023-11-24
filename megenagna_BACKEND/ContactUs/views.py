from django.shortcuts import render
from .models import ContactUS
from rest_framework.decorators import api_view
from django.http.response import HttpResponse
from rest_framework import status,serializers
from django.core.mail import send_mail
from django.core import serializers
from datetime import datetime
from django.template.loader import render_to_string

import json
# Create your views here.

@api_view(['Post'])
def collect_feedback(request):

    request_body = request.body.decode('utf-8')
    
    json_data = json.loads(request_body)
    
    first_name = json_data.get('first_name')
    last_name = json_data.get('last_name')
    email = json_data.get('email')
    message = json_data.get('message')
    date = json_data.get('date')
    date = datetime.strptime(date, "%Y-%m-%d")

    subject = 'Hello from Django'
    html_message = render_to_string('email.html', {'recipient_name': 'John Doe'})
    sender = 'your-email@gmail.com'
    recipients = [email]
    

    

    new_model = ContactUS(email = email, first_name=first_name, last_name=last_name, message = message, date = date )
    new_model.save()
    data = serializers.serialize('json',[new_model])
    send_mail(subject, message, sender, recipients, html_message=html_message)
    return HttpResponse(data, status=status.HTTP_200_OK)

        # return HttpResponse("Successfuly Submitted", status = 200)
    # except:

    #     return HttpResponse ("Failed to submit", status=400)

@api_view(['Get'])
def get_feedbacks(request):
    queryset = ContactUS.objects.all().order_by('-date')
    data = serializers.serialize('json', list(queryset))
    return HttpResponse(data , status = 200)
    


