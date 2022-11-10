from django.urls import path
from .views import *

urlpatterns = [
    path('all_dialership', AllObjectDealershipView.as_view()),  # 4.1
    path('filter', FilterDealershipListView.as_view()),  # 4.2
    path('statistics_avg', StatisticsAvgDealershipView.as_view()),  # 4.3
    path('filter_product', FilterProductsDealershipListView.as_view()),  # 4.4
    path('create_net', CreateDealershipView.as_view()),  # 4.5
    path('update_delete_net/<int:pk>', UpdateDeleteDealershipView.as_view()),
    path('create_product', CreateProductDealershipView.as_view()),  # 4.5
    path('update_delete_product/<int:pk>', UpdateDeleteProductDealershipView.as_view()),
]
