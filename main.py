from models import Class_Entry, Division, SabbathSchoolClass
from datetime import date

UpperDivision = Division("Upper Division")
LowerDivision = Division("Lower Division")

unit_names = [f"Unit {i}" for i in range(1, 13)] + ["Inverse"]
for name in unit_names:
    UpperDivision.classes.append(SabbathSchoolClass(name))

class_names = ["Kindergarten", "Primary", "Junior", "Earliteen", "Cornerstone"]
for name in class_names:
    LowerDivision.classes.append(SabbathSchoolClass(name))

Sabbath_Date = date(2026, 1, 10)

for cls in UpperDivision.classes:
    entry = Class_Entry(
        date=Sabbath_Date,
        class_name =cls.class_name,
        attendance = 8,
        study=5,
        vistors=1,
        offering=1000.0
    )
    cls.entries.append(entry)


for cls in LowerDivision.classes:
    entry = Class_Entry(
        date=Sabbath_Date,
        class_name=cls.class_name,
        attendance=14,
        study=10,
        vistors=5,
        offering=500.0
    )
    cls.entries.append(entry)