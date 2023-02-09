# myapp/urls.py

from django.urls import path
from .views import BookList, BookDetail
# from .views import ObtainTokenPairView


urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),
    # path('api/token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
]
