from django.urls import path
from .views import *

urlpatterns = [
    path('all_factory', AllObjectFactoryView.as_view()),  # 4.1
    path('filter', FilterFactoryListView.as_view()),  # 4.2
    # path('statistics_avg', FilterFactoryListView.as_view()),  # 4.3
]
