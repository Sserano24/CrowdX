from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Project
from django.conf import settings
import stripe
from django.views import View

# Create your views here.


def home(request):
    return render(request, 'campaign/index.html')

def projects(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'campaign/projects.html', {'projects': projects})  # Pass to template

def create_project(request):
    return render(request, 'campaign/create_project.html')

def signup(request):
    return render(request, 'campaign/signup.html')

def login(request):
    return render(request, 'campaign/login.html')

def about(request):
    return render(request, 'campaign/about.html')

def contact(request):
    return render(request, 'campaign/contact.html')

def cancel(request):
    return render(request, 'campaign/cancel.html')

def success(request):
    return render(request, 'campaign/success.html')

def payment(request):
    return render(request, 'campaign/payment.html')

def project_detail(request, id):
    return render(request, 'campaign/project_detail.html', {'id': id})

stripe.api_key = settings.STRIPE_SECRET_KEY

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views import View
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

from django.shortcuts import redirect

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        amount = request.POST.get('amount')
        if not amount:
            return JsonResponse({'error': 'Invalid amount'}, status=400)

        try:
            amount_in_cents = int(float(amount) * 100)

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': 'CrowdX Custom Payment'},
                        'unit_amount': amount_in_cents,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://127.0.0.1:8000/success/',
                cancel_url='http://127.0.0.1:8000/cancel/',
            )
            
            return redirect(checkout_session.url)  # ✅ Redirects to Stripe checkout

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
