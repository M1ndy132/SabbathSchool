from datetime import date

def calculate_division_totals(division, date):
    totals = {
        "attendance": 0,
        "study": 0,
        "visitors": 0,
        "offering": 0
    }

    for cls in division.classes:
        for entry in cls.entries:
            if entry.date == date:
                totals["attendance"] += entry.attendance
                totals["study"] += entry.study
                totals["visitors"] += entry.visitors
                totals["offering"] += entry.offering
    print(totals)
    return totals
        

def calculate_church_totals(updivision, lowdivision, date):
    combine_total = {
        "attendance": 0,
        "study": 0,
        "visitors": 0,
        "offering": 0,
    }

    Upper_div_total = calculate_division_totals(updivision, date)
    Lower_div_total = calculate_division_totals(lowdivision, date)

    combine_total["attendance"] += Upper_div_total.get("attendance", 0) + Lower_div_total.get("attendance", 0)
    combine_total["study"] += Upper_div_total.get("study", 0) + Lower_div_total.get("study", 0)
    combine_total["visitors"] += Upper_div_total.get("visitors", 0) + Lower_div_total.get("visitors", 0)
    combine_total["offering"] += Upper_div_total.get("offering", 0) + Lower_div_total.get("offering", 0)

    print(combine_total)
    return combine_total
