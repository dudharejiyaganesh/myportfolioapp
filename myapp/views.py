from django.shortcuts import render
from . models import Contact

# Create your views here.
def index(request):
	return render(request,'index.html')

def single(request):
	return render(request,'single.html')

def contact(request):
	print(request.POST['message'])
	Contact.objects.create(
		name=request.POST['name'],
		email=request.POST['email'],
		subject=request.POST['subject'],
		message=request.POST['message'],
		)
	msg="Contact Saved SuccessFully.Will Reach You Very Soon."
	return render(request,'index.html', {'msg':msg})
