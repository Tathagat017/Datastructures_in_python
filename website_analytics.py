monday_visitors = {"user1","user2","user3","user4","user5"}
tuesday_visitors = {"user3","user4","user5","user6","user7"}
wednesday_visitors = {"user5","user6","user7","user8","user9"}

def unique_visitors(monday, tuesday, wednesday):
    # Combine all visitors from the three days
    all_visitors = monday.union(tuesday).union(wednesday)
    return all_visitors

def common_visiors_monday_tuesday(monday_visitors, tuesday_visitors):
    # Find common visitors across all three days
    common = monday_visitors.intersection(tuesday_visitors).intersection(wednesday_visitors)
    return common

#New Visitors Each Day

def New_visitors_each_day(monday, tuesday, wednesday):
    new_monday = monday - (tuesday.union(wednesday))
    new_tuesday = tuesday - (monday.union(wednesday))
    new_wednesday = wednesday - (monday.union(tuesday))
    return new_monday, new_tuesday, new_wednesday

def loyalVisitors(monday, tuesday, wednesday):
    # Find loyal visitors who visited all three days
    loyal = monday.intersection(tuesday).intersection(wednesday)
    return loyal

def daily_visitor_overlap(monday, tuesday, wednesday):
    # Find daily visitor overlap
    overlap = monday.intersection(tuesday).intersection(wednesday)
    return overlap
