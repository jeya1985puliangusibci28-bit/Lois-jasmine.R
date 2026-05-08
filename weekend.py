
import datetime

def date_operations():
    1. Convert a string into a date object
    date_str = "2024-03-24"
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    print(f"1. String '{date_str}' converted to date: {date_obj}")

    2. Find the difference between two timestamps in seconds
    ts1 = datetime.datetime(2024, 3, 24, 10, 0, 0)
    ts2 = datetime.datetime(2024, 3, 24, 12, 30, 0)
    diff_seconds = (ts2 - ts1).total_seconds()
    print(f"2. Difference between {ts1} and {ts2}: {diff_seconds} seconds")

    3. Display current date, time, and weekday name
    now = datetime.datetime.now()
    print(f"3. Current Date & Time: {now}")
    print(f"   Current Weekday: {now.strftime('%A')}")

    4. Add and subtract a specific number of days
    base_date = datetime.date(2024, 1, 1)
    days_to_change = 15
    added = base_date + datetime.timedelta(days=days_to_change)
    subtracted = base_date - datetime.timedelta(days=days_to_change)
    print(f"4. Base Date: {base_date}")
    print(f"   Added {days_to_change} days: {added}")
    print(f"   Subtracted {days_to_change} days: {subtracted}")

    5. Calculate the number of weekends (Saturdays and Sundays) between two dates
    start_date = datetime.date(2024, 3, 1)
    end_date = datetime.date(2024, 3, 31)
    
    weekend_count = 0
    current_day = start_date
    while current_day <= end_date:
        # .weekday() returns 5 for Saturday and 6 for Sunday
        if current_day.weekday() >= 5:
            weekend_count += 1
        current_day += datetime.timedelta(days=1)
    
    print(f"5. Total weekends between {start_date} and {end_date}: {weekend_count}")

if __name__ == "__main__":
