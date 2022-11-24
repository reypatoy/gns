from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import vonage
from mailjet_rest import Client
import os
import requests


@api_view(['POST'])
def sms(request):
    toNumber = request.data['recipient']
    text = request.data['message']
    sms_client = vonage.Client(key="f20098bc", secret="e4RPKVZlwEJx53bE")
    sms = vonage.Sms(sms_client)
    responseData = sms.send_message(
        {
            "from": "+639565283327",
            "to": toNumber,
            "text": text,
        }
    )
    if responseData["messages"][0]["status"] == "0":
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'Not Acceptable'}, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def email(request):
    toEmail = request.data['to']
    toName = request.data['name']

    dueDate = request.data['date']
    bill = request.data['bill']
    reading = request.data['reading']
    totalPayed = request.data['payed']
    penalty = request.data['penalty']

    api_key = '1afdfa69d12ff3319b3b9ce17abeedbc'
    api_secret = '309be1056d38f5eb2913b6fbfe5ca47b'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "aiwell.talaironwater@gmail.com",
                    "Name": "Aiwell"
                },
                "To": [
                    {
                        "Email": toEmail,
                        "Name": toName
                    }
                ],
                "Subject": "Payment Confirmation",
                "HTMLPart": f"<h3>Dear {toName}</h3> <h5>Payment Confirmation!!!</h5><br><span>Due Date: {dueDate}</span><br><span>Bill: {bill}</span><br><span>Reading: {reading}m<sup>3</sup></span><br><span>Penalty: {penalty}</span><br><span>Total Payed: {totalPayed}</span><br><h3>Thank You!!!</h3>",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)
