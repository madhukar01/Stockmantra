
#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from log.forms import LoginForm

from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'index', TemplateView.as_view(template_name="index.html"),name='index'),
    url(r'main', TemplateView.as_view(template_name="main.css"),name='main'),
    url(r'trade', TemplateView.as_view(template_name="trade.html"),name='trade'),
    url(r'news', TemplateView.as_view(template_name="news.html"),name='news'),
    url(r'livestocks', TemplateView.as_view(template_name="livestocks.html"),name='livestocks'),
    url(r'Stocks', TemplateView.as_view(template_name="Stocks.html"),name='Stocks'),
    url(r'News/Indian Stocks', TemplateView.as_view(template_name="Indian Stocks.html"),name='Indian Stocks'),
    url(r'Motors', TemplateView.as_view(template_name="Motors.html"),name='Motors'),
    url(r'Gold', TemplateView.as_view(template_name="Gold.html"),name='Gold'),
    url(r'Dollar', TemplateView.as_view(template_name="Dollar.html"),name='Dollar'),
    url(r'Bihar', TemplateView.as_view(template_name="Bihar.html"),name='Bihar'),
    url(r'Market', TemplateView.as_view(template_name="Market.html"),name='Market'),
    url(r'Taiwan', TemplateView.as_view(template_name="Taiwan.html"),name='Taiwan'),
    url(r'Wallstreet', TemplateView.as_view(template_name="Wallstreet.html"),name='Wallstreet'),
    url(r'Oil', TemplateView.as_view(template_name="Oil.html"),name='Oil'),
    

]

