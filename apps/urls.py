from django.conf import urls
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include

from apps.utils import send_email
from apps.views import IndexView, CustomLoginView, RegisterFormView, BlogDetailView, BlogListView, Shoplistview, \
    WishlistView, EmailView


def send_email_task(req):
    return HttpResponse(send_email('Xabar', 'Izzatulloh', ['fayzullaxojaevi@gmail.com']).get('message'))


urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('blog-list', BlogListView.as_view(), name='blog_list_page'),
    path('blog-detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail_page'),
    path('send', send_email_task),
    path('logout', LogoutView.as_view(next_page='index_page'), name='logout'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('register', RegisterFormView.as_view(), name='register_page'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path("shop-list", Shoplistview.as_view(), name='shop-list'),
    path("wishlist-page", WishlistView.as_view(), name='wishlist-page'),
    path('newletter-page', EmailView.as_view(), name="newletter-page"),
    path('shopping-page', Shoplistview.as_view(), name="sopping-page")

]


def page_404(request, *args, **kwargs):
    return render(request, 'apps/404.html', status=404)


urls.handler404 = 'apps.urls.page_404'
