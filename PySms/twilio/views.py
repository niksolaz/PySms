from django.shortcuts import render

# Create your views here.
from .models import Sms

def index(request):
	latest_sms = Sms.objects.order_by('-pub_date')[:5]
	context = {'latest_sms': latest_sms}
	return render(request,'twilio/index.html',context)
