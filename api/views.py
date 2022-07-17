# Feedback
#
# Reduce the read and write of records by 50%
# commit and roll back for errors
# writing tests if you can
#

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user_details
from time import time
from datetime import datetime

# Create your views here


class InsertRecords(APIView):
    def post(self, request):
        start_time = time()
        data = request.data["Payload"]
        for payload_data in data:
            user = user_details()
            user.username = payload_data["username"]
            user.level = payload_data["level"]
            user.stars = payload_data["stars"]
            user.gameType = payload_data["gameType"]
            user.duration = datetime.now()
            user.timestamp = time()
            user.save()
        message = f"Inserted {len(data)} records successfully"
        lastest_record = user_details.objects.last().id
        elapsed_time = time() - start_time
        return Response({
            "message": message,
            "last entry record": lastest_record,
            "elapsed time": elapsed_time
        })


class SyncRecords(APIView):
    def post(self, request):
        start_time = time()

        last_synced_record = user_details.objects.using('users').last().id + 1
        lastest_record = user_details.objects.last().id + 1
        for id in range(last_synced_record, lastest_record):
            detail = user_details.objects.get(id=id)
            new_record = user_details()
            new_record.username = detail.username
            new_record.level = detail.level
            new_record.stars = detail.stars
            new_record.gameType = detail.gameType
            new_record.duration = detail.duration
            new_record.timestamp = detail.timestamp
            new_record.sync = detail.sync
            new_record.isActive = detail.isActive
            new_record.id = id
            new_record.save(using='users')
        last_synced_record = user_details.objects.using('users').last().id
        elp_time = time() - start_time
        return Response({
            "last_record_id": last_synced_record,
            "message": "Synced databases successfully",
            "elapsed time": elp_time
        })


class LastRecord(APIView):
    def get(self, request):
        last_record = user_details.objects.last()
        last_username = last_record.username
        last_entry = last_record.duration.strftime("%d %B %Y - %H:%M:%S")

        return Response({
            "message": "Record Retrived successfully",
            "username": last_username,
            "last_entry_time": last_entry
        })
