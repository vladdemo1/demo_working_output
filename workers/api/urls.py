"""
Contains base urls
"""

from django.urls import path

from .views import BaseView, PositionView, WorkerDetailView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path("workers/<int:page>/", BaseView.as_view(), name="workers-by-page"),
    path("positions/<str:position>/<int:page>/", PositionView.as_view(), name="workers-by-position"),
    path("worker-detail/<str:position>/<str:first_name>/<str:last_name>/", WorkerDetailView.as_view(), name="worker-detail"),
]
