from django.urls import path
from .views import *

urlpatterns = [
    path('all_factory', AllObjectFactoryView.as_view()),  # 4.1
    path('filter', FilterFactoryListView.as_view()),  # 4.2
    # path('statistics_avg', FilterFactoryListView.as_view()),  # 4.3
    path('filter_product', FilterProductsFactoryListView.as_view()),  # 4.4
    path('create_net', CreateFactoryView.as_view()),  # 4.5
    path('update_delete_net/<int:pk>', UpdateDeleteFactoryView.as_view()),
    path('create_product', CreateProductFactoryView.as_view()),  # 4.5
    path('update_delete_product/<int:pk>', UpdateDeleteProductFactoryView.as_view()),
    path('qrcode_net/<int:pk>',GeneratedQRCodeView.as_view())
]
