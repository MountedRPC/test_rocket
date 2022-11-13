from django.urls import path
from .views import *

urlpatterns = [
    path('all_retailnetwork', AllObjectRetailnetworkView.as_view()),  # 4.1
    path('filter', FilterRetailnetworkListView.as_view()),  # 4.2
    path('statistics_avg', StatisticsAvgRetailnetworkView.as_view()),  # 4.3
    path('filter_product', FilterProductsRetailnetworkListView.as_view()),  # 4.4
    path('create_net', CreateRetailnetworkView.as_view()),  # 4.5
    path('update_delete_net/<int:pk>', UpdateDeleteRetailnetworkView.as_view()),
    path('create_product', CreateProductRetailnetworkView.as_view()),  # 4.5
    path('update_delete_product/<int:pk>', UpdateDeleteProductRetailnetworkView.as_view()),
]
