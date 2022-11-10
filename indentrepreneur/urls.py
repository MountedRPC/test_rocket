from django.urls import path
from .views import *

urlpatterns = [
    path('all_distributor', AllObjectDistributorView.as_view()),  # 4.1
    path('filter', FilterDistributorListView.as_view()),  # 4.2
    path('statistics_avg', StatisticsAvgDistributorView.as_view()),  # 4.3
    path('filter_product', FilterProductsDistributorListView.as_view()),  # 4.4
    path('create_net', CreateDistributorView.as_view()),  # 4.5
    path('update_delete_net/<int:pk>', UpdateDeleteDistributorView.as_view()),
    path('create_product', CreateProductDistributorView.as_view()),  # 4.5
    path('update_delete_product/<int:pk>', UpdateDeleteProductDistributorView.as_view()),
]
