<<<<<<< HEAD
##import time
=======
>>>>>>> master
import pandas as pd
import numpy as np


CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

DAY_WEEK = {
    '1': 'Sunday',
    '2': 'Monday',
    '3': 'Tuesday',
    '4': 'Wednesday',
    '5': 'Thursday',
    '6': 'Friday',
    '7': 'Saturday', }

MONTHS = {

    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6, }

# Used for formatting. print('-' *x)
x = 45

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-' * x)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-' * x)

    city = None
    month = None
    day = None

    # Loop Till good input
    while True:
        # Prompt User for City input
        city = input("Would you like to see data for Chicago, New York, or Washington?")

        # Lower case all values
        city = city.lower()

        if city in CITY_DATA.keys():
            break
        else:
        # If bad input
            print("Incorrect value.")

    # Loop till good input
    while True:
        # Prompt User for date filter
        filter_type = input(
            "Would you like to filter the data by month, day, both, or not at all. Type all for no filter.\n")
        filter_type = filter_type.lower()

        if filter_type in ['month', 'day', 'both', 'all']:
            break
        # If bad input
        else:
            print("Incorrect value.")

    # Now if month or both scenario
    if filter_type in ['month', 'both']:
        # Loop till good input
        while True:
            # Prompt User for month
            month = input(
                "Which month? January, February, March, April, May, June, or all?\n")
            # Lower case all values
            month = month.lower()

            if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                pass
            else:
                # if bad input
                print("Incorrect value.")

    if filter_type in ['day', 'both']:
        # Loop till good input
        while True:
            # Prompt User for day
            day = input(
                "Which day? Please type your response as an integer(e.h, 1=Sunday\n")
            day = day.lower()
            if day in ['1', '2', '3', '4', '5', '6', '7', 'all']:
                pass
            else:
                print("Incorrect value.")

    print('-' * x)
    return city, month, day




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
    df = None
    filtered = None

    # Load Data in
    df = pd.read_csv(CITY_DATA[city])

    # Replace Gender NaN with 0
    #gender_null = df['Gender'].fillna(0)
    #df['Gender'].update(gender_null)

    # Convert to time date
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create Weekday Index
    df['weekday'] = df['Start Time'].dt.weekday_name

    # Create Month Index
    df['month'] = df['Start Time'].dt.month

    # Now Filter out Months
    if month is not None:
        df = df[df.month == MONTHS[month]]
        pass
    if day is not None:
        df = df[df.weekday == DAY_WEEK[day]]
        pass


    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    print('Most common start hour:', popular_hour)

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month

    popular_month = df['month'].mode()[0]
    print('Most common start month:', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', popular_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * x)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is:", start_station)
    # Alternative way, same results
    # start_station2 = df['Start Station'].value_counts().keys()[0]
    # print("Most commonly used start station is rev 2: {}".format(start_station2))

    # Display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print( "Most commonly used end station:", end_station)

    # Display most frequent combination of start station and end station trip
    stations = df['Start Station'] + df['End Station']
    most_common_combination = stations.mode()[0]
    print("The most common combination is:", most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' *x)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip = df['Trip Duration'].sum()/60
    print("Total trip time in hours:", total_trip)

    # display mean travel time
    mean_time = total_trip.mean()
    print("Mean of travel:", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*x)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()
    print("Number of Customers: {}\n"
          "Number of Subscribers: {}".format(user_count['Customer'], user_count['Subscriber']))

    # Display counts of gender
    try:
        count_genders = df['Gender'].value_counts()
        print("Count of genders is:", count_genders)
    except KeyError:
        print("No gender data available")

    # Display earliest, most recent, and most common year of birth
    try:
        most_recent = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("The most recent birth year is: {}\nMost common year of birth is: {} ".format(most_recent, most_common_year))
    except KeyError:
        print("No birth year data available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' *x)

def disp_data(df):
<<<<<<< HEAD
    # Displays raw user request
=======
>>>>>>> master
    raw_start = 0 # start
    raw_end = 5   # cycle ends
    while True:
        raw_data = ' '
        if raw_data.lower() != 'yes' :
            raw_data = str(input("Would you like to see the raw data? Enter yes/no"))
            if raw_data.lower() == 'yes':
                print(df.iloc[raw_start : raw_end])
                raw_start += 5
                raw_end += 5
            else:
                break
        elif raw_data.lower() == 'no':
            break
"""
# Version 2 concept. 
        if next_pass == False:
            display = input("Select yes or no.")
        elif next_pass:
            display = input("Select no or yes.")
        display = display.lower()
"""

def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
