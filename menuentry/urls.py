from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'validator.views.validate_menu_entry_data', name='home'),
    url(r'^ajax/format_input/$', 'validator.views.format_input', name='ajax_format_input'),
)
