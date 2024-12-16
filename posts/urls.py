from django.urls import path 
from .views import PostListView, PostDetailVeiw, PostCreateview, PostUpdateView, PostDeleteView

app_name ="posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateview.as_view(), name="create"),
    path("<int:pk>/", PostDetailVeiw.as_view(), name="detail"),
    path("<int:pk>/update", PostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="delete"),
]