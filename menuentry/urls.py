from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'validator.views.validate_menu_entry_data', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
