from django.contrib import admin
from hostapp.models import audImag
import hostapp.models as hm
hm.prepare()
admin.site.register(audImag)
