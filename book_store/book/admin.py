from django.contrib import admin

# Register your models here.
from .models import Book , Author , Address , Country

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("ratings","author",)
    list_display = ("title","author",)

class AddressAdmin(admin.ModelAdmin):
    list_filter = ("postal_code",)
    list_display = ("street","postal_code","city")

admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
