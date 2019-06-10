from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Post

from rest_framework.views import APIView
from rest_framework.response import Response

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
