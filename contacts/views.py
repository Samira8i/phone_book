from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact


def contact_list(request):
    query = request.GET.get('q', '')
    contacts = Contact.objects.filter(first_name__icontains=query) | Contact.objects.filter(last_name__icontains=query)
    return render(request, 'contacts/contact_list.html', {'contacts': contacts, 'query': query})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})


def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {'form': form})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})

