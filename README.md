# Interactive Bikeshare Data Analysis

A small, user-friendly CLI tool for quickly loading, cleaning, and exploring bikeshare CSV datasets for Chicago, New York City, and Washington. Designed for fast exploratory data analysis (EDA), simple operational reporting, and easy onboarding for analysts.

---

## Features

* Interactive prompts with input validation for city, month, and day filters.
* Automatic datetime parsing and derived features: month, day of week, and start hour.
* Common EDA metrics and operational statistics:

  * Most frequent month, day, and start hour
  * Most common start station, end station, and start→end station pair
  * Total and average trip duration
  * User-type counts, gender counts, and birth-year statistics (handles missing columns per dataset)
* Incremental, on-demand data preview (prints 5 more rows at a time for quick QA).
* Clear, human-readable CLI output suitable for quick analysis and demos.

---

## Tech stack

* Python 3.8+
* pandas, NumPy

---


## Input data

Place the following CSV files in the project directory (or update the `CITY_DATA` mapping in the script):

* `chicago.csv`
* `new_york_city.csv`
* `washington.csv`

**Expected (common) columns**: `Start Time`, `End Time`, `Trip Duration`, `Start Station`, `End Station`, `User Type`, `Gender` (may be missing), `Birth Year` (may be missing).

The script includes defensive checks for missing columns and prints a user-friendly message when data is not available for a city.

---

## Usage

Run the script from the project directory:

```bash
python bikeshare_analysis.py
```

The CLI will prompt for three inputs:

1. Select a city: `chicago`, `new york city`, or `washington`.
2. Select a month: `january`–`june` or `all`.
3. Select a day: `monday`–`sunday` or `all`.

After preprocessing, the tool will ask whether you want to preview more rows and then print EDA summary statistics.

### Example session (user input shown after `>`):

```
Hello! Let's explore some US bikeshare data!

 please select the city you would like to explore: chicago, new york city or washington? > chicago
 please select the month you would like to explore: january, february, march, april, may, june or all? > march
 please select the day you would like to explore: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all? > all
----------------------------------------
Would you like to read more data? Enter yes or no. > yes
   (prints first 5 rows)
Would you like to read more data? Enter yes or no. > no

Calculating The Most Frequent Times of Travel...
 As per the available data , the most common month is  3
The most common day is Wednesday
 As per the available data , the most common start hour is 17

Calculating The Most Popular Stations and Trip...
 As per the available data , the most common start station is Canal St & 6th Ave
 As per the available data , the most common end station is Canal St & 6th Ave
 As per the available data , the most common combination between start and end station is
Start Station         End Station
Canal St & 6th Ave    Canal St & 6th Ave    1234
dtype: int64

Calculating Trip Duration...
 As per the available data , total travel time is 12345678.0
 As per the available data , average travel time is 540.2

Calculating User Stats...
There are 10000 subscribers and 3000 customers
There are 6000 males and 4000 females
Earliest year of birth is: 1946 , recent year of birth is: 2002 and common year of birth is : 1989
```

---

## Output examples

* `Most common start hour: 17`
* `Most common station pair: "Canal St & 6th Ave -> Canal St & 6th Ave" (count: 1234)`
* `Total travel time: 12,345,678 seconds`
* `User types: Subscribers=10,000; Customers=3,000`
* For Washington: `This city does not have gender type` (tool handles missing columns gracefully)

---


## License

Choose a license (MIT recommended for academic/demo code).

---
