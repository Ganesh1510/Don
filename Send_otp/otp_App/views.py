# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from Send_otp import settings
from twilio.rest import Client
import random

@api_view(['POST'])
def send_otp(request):
    if request.method == 'POST':
        phone_number = request.data.get('phone_number')

        # Generate OTP
        otp = str(random.randint(100000, 999999))

        # Save OTP in the session (you can use a database or cache for production)
        request.session['otp'] = otp

        # Send OTP via Twilio
        send_otp_via_twilio(phone_number, otp)

        return Response({'status': 'success'})

    return Response({'status': 'error'})


# views.py (continue)

def send_otp_via_twilio(phone_number, otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=f'Your OTP is: {otp} : python application',
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number,
    )
