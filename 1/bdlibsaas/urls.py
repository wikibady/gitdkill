from django.conf.urls import include, url
from django.contrib import admin
from library.views import*
 
urlpatterns = [
    url(r'^$', 'library.views.index', name='index'),
    url(r'^Find$', 'library.views.Find', name='index'),
    url(r'^Add$', 'library.views.Add', name='index'),
    url(r'^AddBook$', 'library.views.AddBook', name='index'),
    url(r'^AddBook2$', 'library.views.AddBook2', name='index'),
    url(r'^BookList$', 'library.views.BookList', name='index'),
    url(r'^DelBook$', 'library.views.DelBook', name='index'),
    url(r'^UpdateBook$', 'library.views.UpdateBook', name='index'),
    url(r'^UpdateBook2$', 'library.views.UpdateBook2', name='index'),
    url(r'^FindByAuthor$', 'library.views.FindByAuthor', name='index'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include(admin.site.urls)),
]