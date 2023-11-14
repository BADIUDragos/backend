from django.urls import path
from base.test.views import TestModelListView

urlpatterns = [
    path('test', TestModelListView.as_view(), name='test_auth'),
    ]
