from random import random, randint

from django.contrib import messages
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
import poster.tasks

# Create your views here.
from poster.models import Poster


def index(request):
    context = {}
    get_all_posts = Poster.objects.all().order_by('link_name')
    if request.method == "POST":
        request_posted = request.POST
        search = request_posted.get('search')
        get_all_posts = Poster.objects.filter(Q(link__icontains=search)|Q(link_name__icontains=search)).order_by('link_name')
    paginator = Paginator(get_all_posts, 5)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({"all_posted_urls": paginator, 'page_obj': page_obj})
    return render(request, "poster/index.html", context)


def post_link(request):
    context = {}
    if request.method == "POST":
        request_posted = request.POST
        link = request_posted.get('link')
        link_name = request_posted.get('link_name')
        try:
            post_success = Poster(link=link, link_name=link_name)
            post_success.save()
        except IntegrityError:
            random_id = randint(0,10000)
            link_name = link_name + str(random_id)
            post_success = Poster(link=link, link_name=link_name)
            post_success.save()
    return render(request, "poster/post.html", context)
