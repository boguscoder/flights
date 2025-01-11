# flights
Steps for converting flightly exports into https://my.flightradar24.com/ format

Using sqlite for the whole shebang 

1. Export your data from flightly app into .csv
2. Open exported file in sqlite: `sqlite3 :memory: -cmd '.mode csv' -cmd '.import <your_export>.csv flightly' -cmd '.mode column' `
3. Set it to write to .csv too:
```bash
sqlite> .mode csv
sqlite> .output flightradar24.csv
sqlite> <query here>
```

where query is

```sql
select 
  Date, Flight as "Flight number", 
  "From", "To", 
  coalesce(
    NULLIF("Take off (Actual)", ""),
    NULLIF("Take off (Scheduled)", ""),
    NULLIF("Gate Departure (Actual)", ""),
    NULLIF("Gate Departure (Scheduled)", "")
  ) as "Dep time",
  coalesce(
    NULLIF("Landing (Actual)" , ""),
    NULLIF("Landing (Scheduled)", ""),
    NULLIF("Gate Arrival (Actual)", ""),
    NULLIF("Gate Arrival (Scheduled)" , "")
  ) as "Arr time",
  Airline,
  "Aircraft Type Name" as Aircraft,
  "Tail Number" as Registration
  from flightly;
```

TODO: Flightradar24 doesn't do flight time math for you :( but it should be trivial to [get timezone by iata code](https://raw.githubusercontent.com/hroptatyr/dateutils/tzmaps/iata.tzmap) and subtract right in the sql query