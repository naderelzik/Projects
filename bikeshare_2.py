import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = {'chicago', 'new_york_city', 'washington'}
months = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}
days = {'all', 'monday', 'tueasday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago','new york city', 'washington']
        city = input ('\n please select the city you would like to explore: chicago, new york city or washington?').lower()
        
        if city in cities:
            break
        else:
            print('\n please select one of the valid options: chicago, new york city or washington')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input ('\n please select the month you would like to explore: january, february, march, april, may, june or all?').lower()
        if month in months:
            break
        else:
            print('\n please select a valid month: january, february, march, april, may, june or all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = months = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day = input ('\n please select the day you would like to explore: monday, tueasday, wednesday, thursday, friday, saturday, sunday or all?').lower()
        if day in days:
            break
        else:
            print('\n please select a valid day of the week: monday, tueasday, wednesday, thursday, friday, saturday, sunday or all')

    print('-'*40)
    return city,month,day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print(city)
    
    df= pd.read_csv(CITY_DATA[city])
    
    df["Start_Time"]= pd.to_datetime(df["Start Time"])
    df["month"] = df["Start_Time"].dt.month  
    df["day_of_week"] = df["Start_Time"].dt.day_name()
    
    
    if month != "all" :
        months_list = ['january' , 'february', 'march' , 'april' , 'may' , 'june']
        month = months_list.index(month)+1
        
        #df = df[df["month"] == month]       
        #if day != "all" :
            #df = df [df["day_of_week"] == day.title()]
            
    i=5       
    while i<len(df):
        question = input('\nWould you like to read more data? Enter yes or no.\n')
        if question.lower() != 'yes':
            break
        else:
            print(df.head(i))
        i+=5
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df["Start Time"]= pd.to_datetime(df["Start Time"])
    print('\nCalculating The Most Frequent Times of Travel...\n','sunday')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df["month"].mode()
    print(" As per the avialable data , the most common month is ",common_month)
    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("The most common day is",common_day)
    # TO DO: display the most common start hour
    common_start_hour =df["Start_Time"].dt.hour.mode()[0]
    print(" As per tha avialable data , the most common start hour is",common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print(f" As per tha avialable data , the most common start station is {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print(f" As per tha avialable data , the most common end station is {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    combination_of_two_stations =df.groupby(['Start Station','End Station'])
    common_start_end_stations = combination_of_two_stations.size().sort_values(ascending=False).head(1)                          
    print(f" As per tha avialable data , the most common combination btween start and end station is {common_start_end_stations}") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f" As per tha avialable data , total travel time is {total_travel_time}") 

    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    (f" As per tha avialable data , average travel time is {average_travel_time}") 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    #Displaying counts of user types
    subscribers=df['User Type'].value_counts()[0]
    customers=df['User Type'].value_counts()[1]
    if city=='chicago':
        dependents=df['User Type'].value_counts()[2]
        print("There are {} subscribers {} customers and {} dependents".format(subscribers, customers,dependents))
    if city=='washington':
        print("This city does not have gender type")
        return
        
    else:
        print("There are {} subscribers and {} customers ".format(subscribers, customers))
    
    # Display counts of gender
    
    males=df['Gender'].value_counts()[0]
    females=df['Gender'].value_counts()[1]
    print("There are {} males and {} females".format(males,females))
    
    # Display earliest, most recent, and most common year of birth
    earliest_birthYear=int(df['Birth Year'].min())
    recent_birthYear=int(df['Birth Year'].max())
    #print(df['Birth Year'].value_counts())
    common_birthYear=int(df['Birth Year'].mode()[0])
    print("Earliest year of birth is: {} , recent year of birth is: {} and common year of birth is : {}".format(earliest_birthYear,recent_birthYear,common_birthYear))
    
    
    start_time = time.time()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()