from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import RegisterForm, LoginForm, ContactForm
from .models import Contact

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created successfully! Please log in, {user.first_name}.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'crm/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'crm/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required
def dashboard_view(request):
    contacts = Contact.objects.filter(user=request.user)
    total = contacts.count()
    leads = contacts.filter(status='lead').count()
    customers = contacts.filter(status='customer').count()
    prospects = contacts.filter(status='prospect').count()
    recent_contacts = contacts.order_by('-created_at')[:5]
    return render(request, 'crm/dashboard.html', {
        'total': total, 'leads': leads, 'customers': customers,
        'prospects': prospects, 'recent_contacts': recent_contacts,
    })

@login_required
def contacts_view(request):
    query = request.GET.get('q', '')
    contacts = Contact.objects.filter(user=request.user)
    if query:
        contacts = contacts.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) |
            Q(email__icontains=query) | Q(company__icontains=query)
        )
    contacts = contacts.order_by('-created_at')
    return render(request, 'crm/contacts.html', {'contacts': contacts, 'query': query})

@login_required
def add_contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, f'Contact {contact.full_name} added successfully!')
            return redirect('contacts')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'crm/contact_form.html', {'form': form, 'action': 'Add'})

@login_required
def edit_contact_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, f'Contact {contact.full_name} updated successfully!')
            return redirect('contacts')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'crm/contact_form.html', {'form': form, 'action': 'Edit', 'contact': contact})

@login_required
def delete_contact_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method == 'POST':
        name = contact.full_name
        contact.delete()
        messages.success(request, f'Contact {name} deleted.')
        return redirect('contacts')
    return render(request, 'crm/confirm_delete.html', {'contact': contact})
