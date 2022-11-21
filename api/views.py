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
    client_id = "f29aaa8f-d5fe-474c-b7ec-e7fbad79fe57"
    client_secret = "8d7OT14hv7MQxWrQcADomiPSjeBqRoiVBJqx9gEZ"
    response = requests.post("https://api.sms.fortres.net/v1/messages", auth=(client_id, client_secret), data={
        "recipient": toNumber,
        "message": text
    })

    if response.status_code == 200:
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'Not Acceptable'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # sms_client = vonage.Client(key="f0c06dc3", secret="Hh1rFYeJuqMq7iXG")
    # sms = vonage.Sms(sms_client)
    # responseData = sms.send_message(
    #     {
    #         "from": "+14254752924",
    #         "to": toNumber,
    #         "text": text,
    #     }
    # )
    # if responseData["messages"][0]["status"] == "0":
    #     return Response({'status': 'ok'}, status=status.HTTP_200_OK)
    # else:
    #     return Response({'status': 'Not Acceptable'}, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def email(request):
    toEmail = request.data['to']
    toName = request.data['name']

    dueDate = request.data['date']
    bill = request.data['bill']
    reading = request.data['reading']
    totalPayed = request.data['payed']
    penalty = request.data['penalty']

    api_key = '6d922bbc6a50f716bf403a751852a61d'
    api_secret = '354614009dc1dac05a4dc4816f7498bf'
    mailjet = Client(auth=(api_key, api_secret))
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
