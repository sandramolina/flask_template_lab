from models.event import *
import datetime

event1 = Event(datetime.date(2022, 4, 14), "Spring Party 2022", 300, "Edinburgh Castle", "A party to celebrate the coming of Ssssssspring!!!")

event2 = Event(datetime.date(2022, 6, 20), "Mike & Holly's Wedding", 500, "West Princes Street Gardens", "A Celebration of Looooooooooooove!!!")

event3 = Event(datetime.date(2022, 10, 31), "Halloween 2022!", 500, "Edinburgh Cemetary", "A Spooky Night!!!")

event_list = [event1, event2, event3]

def add_new_event(new_event):
    event_list.append(new_event)