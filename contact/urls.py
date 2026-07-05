from django.urls import path
from contact.views.contact_view import ContactView, SuccessView

urlpatterns = [
   path('', ContactView.as_view(), name='contact_view'),
   path('success/', SuccessView.as_view(), name='contact_success'),
]

