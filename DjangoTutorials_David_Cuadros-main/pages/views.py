from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ProductForm
from .models import Product

class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'title': 'Products – Online Store',
            'products': Product.objects.all(),
        })
        return ctx

class ProductShowView(View):
    template_name = 'pages/show.html'

    def get(self, request, id):
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product id must be 1 or greater")
        except (ValueError, TypeError):
            return HttpResponseRedirect(reverse('index'))
        product = get_object_or_404(Product, pk=product_id)
        return render(request, self.template_name, {'product': product})

class ProductCreateView(View):
    template_name = 'pages/create.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('index')
        return render(request, self.template_name, {'form': form})

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'title': 'Contact – Online Store',
            'email': 'info@example.com',
            'address': '123 Fake St, Bogotá',
            'phone': '+57 601 123 4567',
        })
        return ctx
