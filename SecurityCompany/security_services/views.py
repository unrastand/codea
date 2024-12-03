from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import InquiryForm

def home(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            # Send emails
            send_mail(
                "New Inquiry Received",
                f"Name: {inquiry.name}\nEmail: {inquiry.email}\nPhone: {inquiry.phone}\nMessage: {inquiry.message}",
                'your-email@example.com',
                ['site-owner@example.com'],
            )
            send_mail(
                "Thank you for your inquiry",
                "We have received your inquiry and will get back to you soon.",
                'your-email@example.com',
                [inquiry.email],
            )
            return redirect('thank_you')
    else:
        form = InquiryForm()
    return render(request, 'security_services/home.html', {'form': form})

def thank_you(request):
    return render(request, 'security_services/thank_you.html')
