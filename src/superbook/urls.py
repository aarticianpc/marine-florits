from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import SignInAndSignUp, LogoutView, ProductView, ServiceView, ContactView, AboutView
#from oscar.app import application

urlpatterns = patterns(
    '',

   # url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^home.html$', SignInAndSignUp.as_view(template_name='home.html'),
        name='home.html'),
    url(r'^$', SignInAndSignUp.as_view(template_name='home.html'),
        name='home'),   
    url(r'^product/$', ProductView.as_view(),
        name='product'),
    url(r'^services/$', ServiceView.as_view(),
        name='services'),
	url(r'^contact/$', ContactView.as_view(),
        name='contact'),
     url(r'^about/$', AboutView.as_view(),
        name='about'),
    url(r'^accounts/logout$', LogoutView.as_view(),
        name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^oscar/', include(application.urls)),
)
