from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import render
from.models import Booking
from rest_framework.decorators import api_view
import json
from Room.models import RoomProfile, Room
import http.client
from django.db.models import Q
from django.core import serializers
from datetime import datetime

# Create your views here.


@api_view(['Post'])
def book(request):
   
    request_body = request.body.decode('utf-8')
    json_data = json.loads(request_body)
    #getting id for the room
    id = int (json_data['id'])

    #calculating the total prize of the booking
    room = Room.objects.get(id = id)
    start_date = datetime.strptime(json_data["start_date"], "%Y-%m-%d")
    end_date = datetime.strptime(json_data["end_date"], "%Y-%m-%d")
    room_profile = RoomProfile.objects.get(id = room.room_profile.id)
    print((end_date-start_date).days,"**********************88" )
    total_amount = ((end_date-start_date).days) *room_profile.price


    #creating booking object with pending status
    booking  = Booking.objects.create(
        customer_first_name = json_data["customer_first_name"],
        customer_last_name = json_data["customer_last_name"],
        customer_email = json_data["customer_email"],
        customer_phone_number = json_data["customer_phone_number"],
        start_date = start_date,
        end_date = end_date,
        room = room,
        total_amount = total_amount,
        currency = json_data["currency"]
    )
    booking.save()


    
    #sending request to chapa API
    conn = http.client.HTTPSConnection("api.chapa.co")
    payload = json.dumps({
    "amount": total_amount,
    "currency": "ETB",
    "email": booking.customer_email,
    "first_name": booking.customer_first_name,
    "last_name": booking.customer_last_name,
    "phone_number": booking.customer_phone_number,
    "tx_ref":  "N-H-S-"+str(booking.id),
    "callback_url": "https://webhook.site/077164d6-29cb-40df-ba29-8a00e59a7e60",
    "return_url": "http://127.0.0.1:8000/booking/book/",
    "customization[title]": "Payment for my favourite merchant",
    "customization[description]": "I love online payments"
    })

    headers = {
    'Authorization': 'Bearer CHASECK_TEST-heQb56CbxYnUmhaJciSft8k2sirz3bO7',
    'Content-Type': 'application/json'
    }

    conn.request("POST", "/v1/transaction/initialize", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data_str = data.decode('utf-8')
    data_dict = json.loads(data_str)
    data_dict['tx_ref'] = "N-H-S-"+str(booking.id)
    data_str_modified = json.dumps(data_dict)
    data_modified = data_str_modified.encode('utf-8')


    

    return HttpResponse(data_modified, status=status.HTTP_200_OK)

@api_view(['Get'])
def check_availability(request, start_date, end_date):
    overlapping_bookings = Booking.objects.filter(Q(start_date__lt=end_date) & Q(end_date__gt=start_date)).values('room')
    available_rooms = Room.objects.exclude(id__in=overlapping_bookings)
    print(available_rooms)
    types_of_rooms = {}
    for room in available_rooms:
        types_of_rooms[room.room_profile.name] = types_of_rooms.get(room.room_profile,0) +1
    data = serializers.serialize('json', available_rooms)
    print(types_of_rooms)
    return HttpResponse(data, status=status.HTTP_200_OK) 

def check_payment(request,unique_id):
    try:
        conn = http.client.HTTPSConnection("api.chapa.co")
        payload = ''
        headers = {
            'Authorization': 'Bearer CHASECK_TEST-heQb56CbxYnUmhaJciSft8k2sirz3bO7'
        }
        conn.request("GET", "/v1/transaction/verify/"+ "N-H-S-"+str(unique_id), payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode('utf-8')
        data = json.loads(data)
        booking  = Booking.objects.get(id = unique_id)
        print("***************************", data['data'], booking.payment_status)
        booking.payment_status = "approved" if data['data'] != None else "rejected"
        booking.save()
        response = serializers.serialize('json', [booking])
        return HttpResponse(data, status=status.HTTP_200_OK)
    except:
        return "suii"


    
    