from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, View
from django import forms
from django.shortcuts import render, redirect

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact Us - Online Store",
            "subtitle": "Get in Touch",
            "email": "info@onlinestore.com",
            "phone": "+1 (555) 123-4567",
            "address": "123 Main Street, Downtown, City, Country 12345",
            "business_hours": "Monday - Friday: 9:00 AM - 6:00 PM",
            "support_email": "support@onlinestore.com"
        })
        return context

class Product:
    products = [
        {"id":1, "name":"TV", "description":"Best TV", "price": 599.99},
        {"id":2, "name":"iPhone", "description":"Best iPhone", "price": 999.99},
        {"id":3, "name":"Chromecast", "description":"Best Chromecast", "price": 49.99},
        {"id":4, "name":"Glasses", "description":"Best Glasses", "price": 199.99}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            # Convert string id to int and check if it's valid
            product_id = int(id)
            if product_id < 1 or product_id > len(Product.products):
                return HttpResponseRedirect('/')
            
            product = Product.products[product_id - 1]
            viewData = {}
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product
            return render(request, self.template_name, viewData)
        except (ValueError, IndexError):
            # If id is not a valid number or product doesn't exist
            return HttpResponseRedirect('/')

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'
    success_template_name = 'products/success.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            viewData = {}
            viewData["title"] = "Product Created - Online Store"
            viewData["product_name"] = form.cleaned_data['name']
            viewData["product_price"] = form.cleaned_data['price']
            return render(request, self.success_template_name, viewData)
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)