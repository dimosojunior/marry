from django.contrib import admin

from becomarketing.models import * 

admin.site.register(Customer)
admin.site.register(OurTeam)
admin.site.register(HomeHeaderImage)
admin.site.register(HomeSlidingDetails)
admin.site.register(ContactImages)
admin.site.register(OurServices)
admin.site.register(OrderItem)
admin.site.register(Order)


@admin.register(HomeServices)
class HomeServicesAdmin(admin.ModelAdmin):
    list_display=['title','slug','available','created','updated','price']
    list_filter=['available','created','updated']
    list_editable=['price','available']
    prepopulated_fields={'slug':('title',)}
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['title','slug','available','created','updated','price']
    list_filter=['available','created','updated']
    list_editable=['price','available']
    prepopulated_fields={'slug':('title',)}




@admin.register(LatestServices)
class LatestServices(admin.ModelAdmin):
    list_display=['title','slug','available','created','updated','price']
    list_filter=['available','created','updated']
    list_editable=['price','available']
    prepopulated_fields={'slug':('title',)}



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

