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

def date_to_quater(date: date, desired_quater, year):
    """ Returns true or false if a date is in the desired quarter in the correct year"""

    """If date is not in the correct year, returns False."""
    if date.year != year:
        return False

    """Groups months into quarters by numerical position"""
    Q1 = [1, 2, 3]
    Q2 = [4, 5, 6]
    Q3 = [7, 8, 9]
    Q4 = [10, 11, 12]

    quaters = {
        1: Q1,
        2: Q2,
        3: Q3,
        4: Q4
    }

    """Attributes the desired quarter to variable compare_quarter for precices comparision.
    Returns True if month falls into the compare_quarter else, Returns False"""

    compare_quarter = quaters[desired_quater]
    month = date.month
    
    if month in compare_quarter:
        return True
    else:
        return False
    
def calculate_quarterly_totals(updivision, lowdivision, quater_number, year):
    """Initializes sabbath_dates set and division_totals and church_total dictionaries to hold retrived stats"""
    sabbath_dates = set()

    division_totals = {
        "upper": {
            "attendance": 0,
            "study": 0,
            "visitors": 0,
            "offering": 0.0
        },
        "lower": {
            "attendance": 0,
            "study": 0,
            "visitors": 0,
            "offering": 0.0
        }
    }

    church_total = {
            "attendance": 0,
            "study": 0,
            "visitors": 0,
            "offering": 0.0
        }
    
    """Loops through entries to determine Sabbaths in the requested quarter"""
    for cls in updivision.classes:
        for entry in cls.entries:
            if date_to_quater(entry.date, quater_number, year):
                sabbath_dates.add(entry.date)

    for cls in lowdivision.classes:
        for entry in cls.entries:
            if date_to_quater(entry.date, quater_number, year):
                sabbath_dates.add(entry.date)

    """Sabbath stats from Sabbaths in the quarter are added to division_totals dictionary"""
    for sabbath_date in sabbath_dates:
        upper_total = calculate_division_totals(updivision, sabbath_date)
        division_totals["upper"]["attendance"] += upper_total["attendance"]
        division_totals["upper"]["study"] += upper_total["study"]
        division_totals["upper"]["visitors"] += upper_total["visitors"]
        division_totals["upper"]["offering"] += upper_total["offering"]

        lower_total = calculate_division_totals(lowdivision, sabbath_date)
        
        division_totals["lower"]["attendance"] += lower_total["attendance"]
        division_totals["lower"]["study"] += lower_total["study"]
        division_totals["lower"]["visitors"] += lower_total["visitors"]
        division_totals["lower"]["offering"] += lower_total["offering"]

    """Church totals are calculated and added to the church_total dictionary; adds upper and lower division stats"""
    church_total["attendance"] = division_totals["upper"]["attendance"] + division_totals["lower"]["attendance"]
    church_total["study"] = division_totals["upper"]["study"] + division_totals["lower"]["study"]
    church_total["visitors"] = division_totals["upper"]["visitors"] + division_totals["lower"]["visitors"]
    church_total["offering"] = division_totals["upper"]["offering"] + division_totals["lower"]["offering"]

    """Returns humman readable data in dictionary form. Clearly differentiates Upper_division, 
    lower_division and church_total."""
    return {
        "upper_division": division_totals["upper"],
        "lower_division": division_totals["lower"],
        "church_total": church_total 
    }