from django.urls import path
from .views import UAPSList, UAPSDetail

urlpatterns = [
    path('', UAPSList.as_view(), name='uap_list'),
    path('<int:pk>', UAPSDetail.as_view(), name='uap-detail'),
]