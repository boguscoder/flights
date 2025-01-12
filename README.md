# flights
Steps for converting [flightly](https://flighty.com/) exports into https://my.flightradar24.com/ format

Using sqlite for the ~~whole shebang~~ first step 

> NOTE: Flightradar24 import doesn't calculate flight time automatically so we use tzones.cvs that maps IATA airport codes to IANA timezone names (sourced from [here](https://raw.githubusercontent.com/hroptatyr/dateutils/tzmaps/iata.tzmap)), alas sqlite3 can't properly deal with names either so we use smol python script to patch the duration ¯\\_(ツ)_/¯ 

1. Export your data from flightly app into .csv
2. Preprocess it with sqlite
```bash
sqlite3 -cmd '.mode csv' -cmd '.import <your_export>.csv flightly' -cmd '.import tzones.csv tzones' -cmd '.output flightradar24.csv' -cmd '.headers on' < query.sql
```

> NOTE: If you dont care about flight durations, you can skip step 3

3. feed result into calc_duration.py <in> <out>
4. upload to https://my.flightradar24.com/
5. ???
6. PROFIT!

> TODO: get rid of sqlite, rewrite everything into python since we need it anyway