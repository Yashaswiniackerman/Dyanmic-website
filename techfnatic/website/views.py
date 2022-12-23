from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from website.models import SocialLinks
from website.models import Info
from website.models import Location
from website.models import Product

# Create your views here.


def index(request):
    # if request.method == 'GET':
    
    template = loader.get_template('website/index.html')
    social_links = SocialLinks.objects.all().first()
    info = Info.objects.all().first()
    location = Location.objects.all().first()
    product = Product.objects.all()
    
    
    
    context = {
        'sociallinks': social_links,
        'info' : info,
        'location': location,
        'products' : product,
    }
    
    
    return HttpResponse(template.render(context, request))
    