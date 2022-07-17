from django.urls import path
from .views import InsertRecords, SyncRecords, LastRecord


urlpatterns = [
    path('insertRecords/', InsertRecords.as_view()),
    path('syncRecords/', SyncRecords.as_view()),
    path('lastRecords/', LastRecord.as_view()),
]
