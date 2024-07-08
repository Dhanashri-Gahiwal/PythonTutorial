from django.shortcuts import render,redirect
from .models import Contact
from contacts.forms import SaveContact

# Create your views here.
def index(request):
    contacts = Contact.objects
    if request.method == 'POST':
        form = SaveContact(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'contacts':contacts})

def delete(request,contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()

    return redirect('/')

def edit(request,contact_id):
    if request.method == 'POST':
        contact = Contact.objects.get(pk=contact_id)
        form = SaveContact(request.POST or None,instance=contact)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        contact = Contact.objects.get(pk=contact_id)
        return render(request,'edit.html',{'contact':contact})