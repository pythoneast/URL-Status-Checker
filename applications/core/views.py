from django.shortcuts import redirect
from django.urls import reverse


def main_page_view(request):
    return redirect(reverse('urls:url-list'))
