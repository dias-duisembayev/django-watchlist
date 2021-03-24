from django.urls import path

from .views import WatchListView, WatchListFinishedView, WatchUpdateView, WatchCreateView, WatchDeleteView, SignUpView

urlpatterns = [
    path('', WatchListView.as_view(), name='home'),
    path('finished/', WatchListFinishedView.as_view(), name='finished'),
    path('watch/new', WatchCreateView.as_view(), name='watch_new'),
    path('watch/<int:pk>/', WatchUpdateView.as_view(), name='watch'),
    path('watch/delete/<int:pk>/', WatchDeleteView.as_view(), name='watch_delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
