from django.urls import path
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import MovieList, MovieDetail


urlpatterns = [
    path('list/', MovieList.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie-details'),
]
