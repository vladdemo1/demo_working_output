"""
Contains base urls
"""

from django.urls import path

from .views import BaseView, PositionView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path("workers/<int:page>/", BaseView.as_view(), name="workers-by-page"),
    path("positions/<str:position>/<int:page>/", PositionView.as_view(), name="workers-by-position")
]
