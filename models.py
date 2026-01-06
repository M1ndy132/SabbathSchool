class Class_Entry:
    def __init__(self, date, class_name, attendance = 0, study = 0, vistors = 0, offering = 0.0) -> None:
        self.date = date
        self.class_name = class_name
        self.attendance = attendance
        self.study = study
        self.vistors = vistors
        self.offering = offering


class SabbathSchoolClass:
    def __init__(self, class_name) -> None:
        self.class_name = class_name
        self.entries = []


class Division:
    def __init__(self, division_name) -> None:
        self.division_name = division_name
        self.classes = []

