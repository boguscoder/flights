select 
    Date, "Flight" as "Flight number", 
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
    "Tail Number" as Registration,
    t1.Zone as "TZ From",
    t2.Zone as "TZ To"
    from flightly 
        join tzones t1 on "From" == t1.Code 
        join tzones t2 on "To" == t2.Code;