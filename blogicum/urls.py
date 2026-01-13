from django.urls import path, include

urlpatterns = [
    path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
]
