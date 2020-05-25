import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.#ADDED FOR GITHUB PROJECT
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#added for task 5

    while True:
        City = input("\n Filter by which city?  chicago,new york city or washington?\n")
        City=City.lower()
        if City not in ( 'chicago','new york city', 'washington'):
            print("Error wrong input, try again.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        Mon = input("\n Filter by which month? January, February, March, April, May, June or type 'any' if you do not have any preference?\n")
        if Mon not in ('any','January', 'February', 'March', 'April', 'May', 'June'):
            print("Error wrong input. Try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        Day = input("\n Enter the day from: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'any' if you do not have any preference.\n")
        if Day not in ('any','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
            print("Error. Try again.")
            continue
        else:
            break

    print('-'*40)
    return City, Mon, Day


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
    dataf = pd.read_csv(CITY_DATA[city])

    dataf['Start Time'] = pd.to_datetime(dataf['Start Time'])
    dataf['month'] = dataf['Start Time'].dt.month
    dataf['day_of_week'] = dataf['Start Time'].dt.weekday_name

    if month != 'any':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        dataf = dataf[dataf['month'] == month]

    if day != 'any':
        dataf = dataf[dataf['day_of_week'] == day.title()]

    return dataf


def time_stats(dataf):
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating Most Popular Timee of Travel...\n')
    starting_time = time.time()

    # TO DO: display the most common month

    frequent_month = dataf['month'].mode()[0]
    print('Most Frequent Month:', frequent_month)



    frequent_day = dataf['day_of_week'].mode()[0]
    print('Most Frequent day:', frequent_day)

    dataf['hour'] = dataf['Start Time'].dt.hour
    frequent_hour = dataf['hour'].mode()[0]
    print('Most Frequent Hour:', frequent_hour)


    print("\ Process took %s seconds." % (time.time() - starting_time))
    print('-'*40)



def station_stats(dataf):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    starting_time = time.time()


    first_station = dataf['Start Station'].value_counts().idxmax()
    print('Most Frequent first station:', first_station)


    # TO DO: display most commonly used end station

    last_station = dataf['End Station'].value_counts().idxmax()
    print('\nMost Frequent  Last station:', last_station)



    Combination_Station = dataf.groupby(['Start Station', 'End Station']).count()
    print('\nMost Frequently used combination of start station and end station trip:', first_station, " & ",last_station)


    print("\Process took %s seconds." % (time.time() - starting_time))
    print('-'*40)


def trip_duration_stats(dataf):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    starting_time = time.time()


    
    travel_time_total = sum(dataf['Trip Duration'])
    print('Travel Time Total:', travel_time_total/86400, " Days")



    Average_Travel_Time = dataf['Trip Duration'].mean()
    print('Mean travel time:', Average_Travel_Time/60, " Minutes")


    print("\nProcess took %s seconds." % (time.time() - starting_time))
    print('-'*40)


def user_stats(dataf):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    starting_time = time.time()

    # TO DO: Display counts of user types

    user_type = dataf['User Type'].value_counts()
    print('User Types:\n', user_type)


    try:
      gender_type = dataf['Gender'].value_counts()
      print('\nGender Types:\n', gender_type)
    except KeyError:
      print("\n Gender Types:\n data  not available for this month.")


    try:
      oldest_Year = dataf['Birth Year'].min()
      print('\noldest Year:', oldest_Year)
    except KeyError:
      print("\noldest Year:\n data nor available for this month.")

    try:
      Latest_Year = dataf['Birth Year'].max()
      print('\nLatest Year:', Latest_Year)
    except KeyError:
      print("\nLatest Year:\n data not available for this month.")

    try:
      most_frequent_Year = dataf['Birth Year'].value_counts().idxmax()
      print('\nMost frequent Year:', most_frequent_Year)
    except KeyError:
      print("\nMost frequen Year:\ndata not available for this month.")

    print("\nProcess took %s seconds." % (time.time() - starting_time))
    print('-'*40)

def raw_data(dataf):
    first_index=0
    last_index=5
    starting_time = time.time()
    while True:
        answer=input('Would you like to see 5 lines of raw data? Enter yes or no:').lower()
        if answer == 'yes':
            print(dataf[first_index:last_index])
            first_index=last_index
            last_index=last_index+5
            continue
        else:
            break
    
    print("\nProcess took %s seconds." % (time.time() - starting_time))
            
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        


        

       


if __name__ == "__main__":
	main()
