from django.contrib import admin
from website.models import SocialLinks
from website.models import Info
from website.models import Location
from website.models import Product


# class SocialLinksInstanceInline(admin.TabularInline):
#     model = SocialLinks
    
    
# class InfoInstanceInline(admin.TabularInline):
#    model = Info
    
    
# class LocationInstanceInline(admin.TabularInline):
#     model = Location
    
    
# class ProductInstanceInline(admin.TabularInline):
#     model = Product

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')

#     inlines = [BooksInstanceInline]


# class SocialLinksAdmin(admin.ModelAdmin):
#    fields1 = ('facebook','email', 'whatsapp', 'phoneno',)
    

# class InfoAdmin(admin.ModelAdmin):
#    fields2 = ('webimage','aboutus', 'weblogo', 'webintro',)
    
    
# class LocationAdmin(admin.ModelAdmin):
#    fields3 = ('address',)
    
    
# class ProductAdmin(admin.ModelAdmin):
#    fields4 = ('productimage', 'productname', 'description',)
    
    
# Register your models here.
# @admin.register(SocialLinks)
# class SocialLinksAdmin(admin.ModelAdmin):
#     list_display = ("facebook", "email", "whatsapp", "phoneno",)
# #     inlines = [SocialLinksInstanceInline]
    
    
# @admin.register(Info)
# class InfoAdmin(admin.ModelAdmin):
#    list_display = ("webimage", "aboutus", "weblogo", "webintro",)
# #     inlines = [InfoInstanceInline]
    
    
# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#    list_display = ("address",)
# #     inlines = [LocationInstanceInline]
    
    
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#    list_display = ("productimage", "productname", "description",)
# #     inlines = [ProductInstanceInline]

admin.site.register(SocialLinks)

admin.site.register(Info)

admin.site.register(Location)
admin.site.register(Product)


