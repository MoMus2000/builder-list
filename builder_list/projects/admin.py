from django.contrib import admin

from projects.models import *

admin.site.site_header = " "
admin.site.site_title = " "
admin.site.index_title = " "

admin.site.register(Project)
admin.site.register(Checklist)
admin.site.register(Design)

