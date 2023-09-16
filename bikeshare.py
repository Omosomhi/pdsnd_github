import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    main_cities = ["chicago", "new york city", "washington"]

    while True:
        city = input("Please enter a city: ").strip().lower()

        if city in main_cities:
            break
        else:
            print("Invalid city name. Please enter one of the following cities: Chicago, New York City, Washington.")

    # TO DO: get user input for month (all, january, february, ..., june)
    main_months = ["all", "january", "february", "march", "april", "may", "june"]

    while True:
        month = input("Please enter a month: ").strip().lower()

        if month in main_months:
            break
        else:
            print("Invalid month. Please enter 'all' or a valid month name (January, February, March, April, May, June).")

    # TO DO: get user input for day of the week (all, monday, tuesday, ... sunday)
    main_days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    while True:
        day = input("Please enter a day of the week: ").strip().lower()

        if day in main_days:
            break
        else:
            print("Invalid day. Please enter a valid day of the week (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).")

    print('-' * 40)
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

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time' to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')  # Format day of the week

    # Filter by month if applicable
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month.lower() not in months:
            print("Invalid month name. Please choose from January to June or 'all'.")
            return None
        month_num = months.index(month.lower()) + 1
        df = df[df['month'] == month_num]

    # Filter by day of the week if applicable
    if day.lower() != 'all':
        if day.lower() not in df['day_of_week'].str.lower().unique():
            print("Invalid day of the week. Please choose a valid day or 'all'.")
            return None
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is:", most_common_day)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_common_hour = df['start_hour'].mode()[0]
    print("The most common start hour is:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is:", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    most_frequent_combination = df['combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is:", most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time, "seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel_time, "seconds")

    #The amount of time taken for the query is stated
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_type_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:")
        print(gender_counts)
    else:
        print("We're sorry! There is no data available for gender in this dataset.")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nThe oldest rider in this dataset was born in the year:", earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("The youngest rider in this dataset was born in the year:", most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("The most common birth year among riders in this dataset is:", most_common_birth_year)
    else:
        print("We're sorry! There is no data available for birth years in this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #Prompt the user if they want to see 5 lines of raw data
def raw_data(df):
    
    """Displays 5 rows of raw data depending on the selected city.
    """
    #maximum of 5 rows are displayed based on user's input

    rows_to_display = 5
    start_row = 0
    while True:
        show_data = input("Do you want to see 5 lines of raw data? (yes/no): ").strip().lower()
        if show_data == 'yes':
            if start_row >= len(df):
                print("No more raw data to display.")
                break
            end_row = start_row + rows_to_display
            print(df.iloc[start_row:end_row])
            start_row = end_row
        elif show_data == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")
    print("Thank you for using the data viewer.")
   
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
