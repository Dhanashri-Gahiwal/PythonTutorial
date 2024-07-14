from django.shortcuts import render,redirect
from .models import Contact
from contacts.forms import SaveContact
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    contacts = Contact.objects.filter(contactholder=request.user)
    if request.method == 'POST':
        form = SaveContact(request.POST or None)
        if form.is_valid():
            form.save(commit=False).contactholder = request.user
            form.save()
            messages.success(request,('Contact successfully added!'))
            return redirect('/')
    else:    
        return render(request,'index.html',{'contacts':contacts})

@login_required
def delete(request,contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    messages.success(request,('Contact successfully deleted!'))
    return redirect('/')

@login_required
def edit(request,contact_id):
    if request.method == 'POST':
        contact = Contact.objects.get(pk=contact_id)
        form = SaveContact(request.POST or None,instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request,('Contact successfully updated!'))
        return redirect('/')
    else:
        contact = Contact.objects.get(pk=contact_id)
        return render(request,'edit.html',{'contact':contact})