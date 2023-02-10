# myapp/urls.py

from django.urls import path
from .views import BookList, BookDetail
from .views import CurrentUserView
# from .views import ObtainTokenPairView

app_name = 'myapp'
urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('current_user/', CurrentUserView.as_view(), name='current_user'),
    # path('api/token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
]
