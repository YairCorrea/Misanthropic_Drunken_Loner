from django.urls import path
from . import views
from django.views.generic import TemplateView;
class AboutView(TemplateView):
    template_name="Home/about.html"
urlpatterns = [
        path('',views.index, name='index'),
        path('<int:Post_id>/',views.OnePost,name="OnePost"),
        ]
