from django.urls import path
from .views import *

urlpatterns = [
    path('all_dealership', AllObjectDealershipView.as_view()),  # 4.1
    path('filter', FilterDealershipListView.as_view()),  # 4.2
    path('statistics_avg', StatisticsAvgDealershipView.as_view()),  # 4.3
    path('filter_product', FilterProductsDealershipListView.as_view()),  # 4.4
    path('create', CreateDealershipView.as_view())  # 4.5
]
