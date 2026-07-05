from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from contact.models.forms import ContactForm

class SuccessView(TemplateView):
    template_name = "success.html"


class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("contact_success")

    def form_valid(self, form):
        # Récupération des nouveaux champs correspondants à l'image
        full_name = form.cleaned_data["full_name"]
        email = form.cleaned_data["email"]
        phone_number = form.cleaned_data.get("phone_number", "Non renseigné")
        message = form.cleaned_data["message"]

        full_message = (
            f"Received message from {full_name} ({email})\n"
            f"Phone: {phone_number}\n"
            f"________________________\n\n"
            f"{message}"
        )
        
        send_mail(
            subject=f"Contact Form: Message from {full_name}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
            fail_silently=False,
        )
        
        return super().form_valid(form)
