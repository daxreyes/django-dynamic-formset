from django.views.generic import TemplateView
from django.urls import path, include
from .forms import AutoCompleteOrderedItemForm, OrderedItemForm, ContactFormset, MaxFiveContactsFormset, EmptyContactFormset, EventFormset
from .forms import AutoCompleteSelectFieldForm
from . import views

app_name='example'
urlpatterns = [
    path('stacked/', views.formset, {'formset_class': ContactFormset, 'template': 'example/formset-stacked.html'}, name='example_stacked'),
    path('table/', views.formset, {'formset_class': ContactFormset, 'template': 'example/formset-table.html'}, name='example_table'),
    path('form-template/', views.formset_with_template, {'formset_class': EmptyContactFormset, 'template': 'example/form-template.html'}, name='example_form_template'),
    path('admin-widget/', views.formset, {'formset_class': EventFormset, 'template': 'example/formset-admin-widget.html'}, name='example_admin_widget'),
    path('multiple-formsets/', views.multiple_formsets, {'template': 'example/formset-multiple-formsets.html'}, name='example_multiple_formsets'),
    path('inline-formset/', views.inline_formset,
       {'form_class': OrderedItemForm, 'template': 'example/inline-formset.html'}, name='example_inline_formset'),
    path('inline-formset-autocomplete/', views.inline_formset,
       {'form_class': AutoCompleteOrderedItemForm, 'template': 'example/inline-formset-autocomplete.html'}, name='example_inline_autocomplete'),
    path('inline-formset-ajax-selects/', views.inline_formset,
       {'form_class': AutoCompleteSelectFieldForm, 'template': 'example/inline-formset-django-ajax-select.html'}, name='example_inline_ajax_selects'),
    path('autocomplete-products/', views.autocomplete_products, name='example_autocomplete_products')
]

#import django
#major, minor = django.VERSION[:2]
#if major >= 1 and minor >= 2:
#    # These examples require Django 1.2 and above:
#    urlpatterns += patterns('example.views',
#        url(r'^max-forms/$', 'formset', {'formset_class': MaxFiveContactsFormset, 'template': 'example/max-forms.html'}, name='example_max_forms'),
#        url(r'^empty-form/$', 'formset', {'formset_class': EmptyContactFormset, 'template': 'example/empty-form.html'}, name='example_empty_form'),
#    )
#
#if major >=1 and minor >= 7:
#    from example.forms import MinTwoContactsFormset
#    # These examples require Django 1.7 and above:
#    urlpatterns += patterns('example.views',
#        url(r'^min-forms/$', 'formset', {'formset_class': MinTwoContactsFormset, 'template': 'example/min-forms.html'}, name='example_min_forms'),
#    )
