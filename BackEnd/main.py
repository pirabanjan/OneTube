# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import sys
#
# sys.path.append("C:\Users\DELL\PycharmProjects\pythonProject")
from yt_stats import YTStats

API_Key = "AIzaSyAJ0yztvfHwKNU01h5TQaUW4hHuY98DreU"
channel_id = "UCcAd5Np7fO8SeejB1FVKcYw"
yt = YTStats(API_Key, channel_id)
yt.get_stats()
