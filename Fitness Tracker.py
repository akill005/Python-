# Fitness tracker
from dateutil import parser
from fitness_tracker import gpsdistance
class Workout(object):
    cal_per_hour=200
    def __init__(self,start,end,calories=None):
        self.start=parser.parse(start)
        self.end=parser.parse(end)
        self.calories=calories
        self.icon='💪'
        self.kind='Workout'
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_calories(self):
        if self.calories==None:
            return Workout.cal_per_hour*(self.end - self.start).total_seconds()/3600
        else:
            return self.calories
    def get_duration(self):
        return self.end - self.start
    def set_start(self,st):
        self.start=st
    def set_end(self,end):
        self.end=end
    def set_calories(self,cal):
        self.calories=cal
    def __eq__(self,other):
        return type(self)==type(other) and self.start==other.start and self.end==other.end and self.kind==other.kind
    def __str__(self):
        wid=16
        retstr=f" {"_"*wid}\n"
        retstr+=f"|{" "*wid}|\n"
        retstr+=f"| {self.icon}{" "*(wid-3)}|\n"
        retstr+=f"| {self.kind}{" "*(wid-len(self.kind)-1)}|\n"
        retstr+=f"|{" "*wid}|\n"
        dur=str(self.get_duration())
        retstr+=f"| {dur}{" "*(wid-len(dur)-1)}|\n"
        cal=f"{self.get_calories():.0f}"
        retstr+=f'| {cal} Calories{" "*(wid-len(cal)-10)}|\n'
        retstr+=f"|{" "*wid}|\n"
        retstr+=f"|{"_"*wid}|\n"
        return retstr
        
class Running(Workout):
    cal_per_km=100
    def __init__(self,start,end,elev=0,calories=None,gps_pts=None):
        super().__init__(start,end,calories)
        self.icon='🏃‍'
        self.kind='Running'
        self.elev=elev
        self.gps_pts=gps_pts
    def __eq__(self,other):
        return super().__eq__(other) and self.elev==other.elev
    def get_elev(self):
        return self.elev
    def set_elev(self,el):
        self.elev=el
    def get_calories(self):
        if self.gps_pts!=None:
            dis=gpsdistance(40.748817, -73.985428, 40.689247, -74.044502)
            return dis*Running.cal_per_km
        else:
            return super().get_calories()
    
 
    
    
    
# w1=Workout('Jan 1 2021 1:30 PM','Jan 1 2021 2:15 PM')
# print(w1.get_calories())
# print(w1)
# w2=Running('Jan 1 2021 12:30 PM','Jan 1 2021 2:15 PM')
# print(w2)

w=Running('Jan 1 2021 1:30 PM','Jan 1 2021 2:15 PM',0,None)
print(w)

w1=Workout('Jan 1 2021 1:30 PM','Jan 1 2021 2:15 PM')
w2=w1=Workout('Jan 1 2021 1:30 PM','Jan 1 2021 2:15 PM')
rw1=Running('Jan 1 2021 1:30 PM','Jan 1 2021 2:15 PM')
rw2=Running('Jan 1 2021 1:30 PM','Jan 1 2021 2:15 PM')

print(w1==w2)
print(rw1==w2)

print(rw1==rw2)
print(w1==rw2)















