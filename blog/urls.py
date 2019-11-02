from django.conf.urls import url ,include
from . import views

urlpatterns = [
    url(r"^$", views.blog_index, name="blog_index"),
    url(r'^(?P<pk>\d+)$', views.blog_detail, name="blog_detail"),
    url(r"^category/(?P<category>\w+)/$", views.blog_category, name="blog_category"),
    url(r"^contact/$", views.blog_contact, name="blog_contact"),

]
