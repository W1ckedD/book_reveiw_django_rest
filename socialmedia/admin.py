from django.contrib import admin
from .models import SocialMediaType, SocialMedia

admin.site.register(SocialMedia)
admin.site.register(SocialMediaType)