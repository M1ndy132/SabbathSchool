class WeeklyTally:
    def __init__(self) -> None:
        self.week_number = 0
        self.attendance = 0
        self.study = 0
        self.vistors = 0
        self.offering = 0.0


class SabbathSchoolClass:
    def __init__(self) -> None:
        self.class_name = ""
        self.weekly_tallys = []


class Division:
    def __init__(self) -> None:
        self.division_name = ""
        self.classes = []

