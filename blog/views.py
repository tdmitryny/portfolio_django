from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView

from .forms import ContactForm


class PostListView(ListView):
    model = Post
    context = Post.objects.all().order_by('-date')
    template_name = 'home.html'
    paginate_by = 3
    
    
class PostListDetailsView(ListView):
    model = Post
    context = Post.objects.all().order_by('-date')
    template_name = 'blog/post.html'
    paginate_by = 4
    
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html' #Can be changed to post_detail.html


class SuccessView(ListView):
    template_name = "success.html"
    


class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)