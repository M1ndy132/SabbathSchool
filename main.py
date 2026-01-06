from models import Class_Entry, Division, SabbathSchoolClass

UpperDivision = Division("Upper Division")
LowerDivision = Division("Lower Division")

unit_names = [f"Unit {i}" for i in range(1, 13)] + ["Inverse"]
for name in unit_names:
    UpperDivision.classes.append(SabbathSchoolClass(name))

class_names = ["Kindergarten", "Primary", "Junior", "Earliteen", "Cornerstone"]
for name in class_names:
    LowerDivision.classes.append(SabbathSchoolClass(name))
