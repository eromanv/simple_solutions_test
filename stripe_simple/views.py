from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Item
import stripe
from django.urls import reverse
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
domain = settings.DOMAIN

def buy(request, pk):
    item = get_object_or_404(Item, pk=pk)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='payment',
        line_items=[
            {
                'price': item.stripe_price_id,
                'quantity': 1,
            },
        ],
        success_url=domain + reverse('success'),
        cancel_url=domain + reverse('item', kwargs={'pk': item.pk})
    )
    return JsonResponse({'id': checkout_session.stripe_id})


def item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request, 'stripe_simple/item.html', context)


def success(request):
    return HttpResponse('success')
