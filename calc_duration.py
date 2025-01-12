import csv
import sys
from zoneinfo import ZoneInfo
from datetime import datetime

def localize(datetime_str, timezone_str):
    try:
        dt = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        dt = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M")
    tz = ZoneInfo(timezone_str)
    return dt.replace(tzinfo=tz)

with open(sys.argv[1], newline='') as flights, open(sys.argv[2], 'w', newline='') as outfile:
    reader = csv.DictReader(flights)
    fieldnames = reader.fieldnames + ["Duration"]
    fieldnames.remove("TZ To")
    fieldnames.remove("TZ From")
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, extrasaction="ignore")
    
    writer.writeheader()

    for row in reader:
        duration = localize(row["Arr time"], row["TZ To"]) - localize(row["Dep time"], row["TZ From"])
        row["Duration"] = duration
        writer.writerow(row)