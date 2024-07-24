from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from .forms import EmailForm


@api_view(['POST'])
def send_email_api(request):
    if request.method == 'POST':
        form = EmailForm(request.data)
        if form.is_valid():
             to_email = form.cleaned_data['to_email']
             subject = form.cleaned_data['subject']
             message = form.cleaned_data['message']

             send_mail(
                 subject,
                 message,
                 'ganeshganesh44634@gmail.com',
                 [to_email],
                 fail_silently=False,
                )

             return Response({'message':'Email send Successfully!'})
        return Response({'error':'Invalid data'},status=400)
    return Response({'error':'Invalid request method'},status=405)
        