class Weeker:
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def __init__(self, day):
        if day not in self.days:
            return "Invaild Day Name"
        self.day_index = self.days.index(day)

    
    def next_day(self, gap):
        days_left = len(self.days) - (self.day_index + 1)
        day_travel = (gap - days_left) - 1
        print(days_left, day_travel)
        day = self.days[day_travel]

        return day

    def prev_day(self, gap):
        days_left = len(self.days) - (len(self.days) - self.day_index)
        day_travel = gap - days_left
        day = self.days[-day_travel]

        return day

weeker_obj = Weeker("Mon")

print("Next day:", weeker_obj.next_day(3))
print("Prev day:", weeker_obj.prev_day(6))