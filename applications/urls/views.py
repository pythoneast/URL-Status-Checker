import requests
from concurrent import futures

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from applications.urls.models import URL


@login_required
def url_list_view(request):
    urls = URL.objects.all()
    return render(request, 'url_list.html', locals())


def check_url_status_view(request):
    def getData(url):
        url_id = url.id

        try:
            response = requests.get(url.url)
            url_status = response.status_code
        except requests.exceptions.ConnectionError:
            url_status = 0  # for connection error case

        return url_id, url_status

    max_thread_number = 100
    urls = URL.objects.all()

    with futures.ThreadPoolExecutor(max_workers=max_thread_number) as executor:
        res = executor.map(getData, urls)
    return JsonResponse({'status': 200, 'results': dict(res)})
