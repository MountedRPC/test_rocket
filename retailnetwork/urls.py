from django.urls import path
from .views import *

urlpatterns = [
    path('all_indentrepreneur', AllObjectIndentrepreneurView.as_view()),  # 4.1
    path('filter', FilterIndentrepreneurListView.as_view()),  # 4.2
    path('statistics_avg', StatisticsAvgIndentrepreneurView.as_view()),  # 4.3
    path('filter_product', FilterProductsIndentrepreneurListView.as_view()),  # 4.4
    path('create_net', CreateIndentrepreneurView.as_view()),  # 4.5
    path('update_delete_net/<int:pk>', UpdateDeleteIndentrepreneurView.as_view()),
    path('create_product', CreateProductIndentrepreneurView.as_view()),  # 4.5
    path('update_delete_product/<int:pk>', UpdateDeleteProductIndentrepreneurView.as_view()),
]
