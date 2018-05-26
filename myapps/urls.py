from django.urls import path, include

''' リダイレクトのみ行う '''
urlpatterns = [
    path('mnist/', include('myapps.mnist.urls')),
]
