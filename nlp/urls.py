from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from nlp import views
 
# api versioning
router = routers.DefaultRouter()
router.register(r'nlp', views.TaskView, 'tasks')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('api/v1/getMovies/', views.getMovies, name='getMovies'),
    path('api/v1/process-description/', views.process_description, name='process_description'),
    path('api/v1/recommend-movies/', views.find_similarity, name='find_similarity'),
    path('docs/', include_docs_urls(title="API Documentation"))
]