from django.contrib import admin
from .models import butterfly, Feeding, Toy, Photo

admin.site.register(butterfly)
# Register the new Feeding model
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)

