"""
Resourses I used to help me in the project:
-------------------------------------------- 
1.Udacity.com
2.geeksforgeeks.com
3.stackoverflow.com
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months = ['january', 'february', 'march', 'april', 'may', 'june']
Days = {'Sat':'Saturday','Sun':'Sunday','Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday','Thu':'Thursday','Fri':'Friday'}

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would like to see data for Chicago, New York City, or Washington?\n').strip().lower()

    filter_type = input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter.\n').lower().strip()

    if filter_type.lower().strip() == 'both': # get user input for month (all, january, february, ... , june)

        month = input('Which Month? January, February, March, April, May,or June?\n').lower().strip()
# get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Which Day? Please Type the First Three Letters (e.g. Thu=Thursday)\n').title().strip()
        day = Days[day]
    elif filter_type.lower().strip() == 'month':
        month = input('Which Month? January, February, March, April, May,or June?\n').strip().lower()
        day = 'all'
    elif filter_type.lower().strip() == 'day':
        day = input('Which Day? Please Type the First Three Letters (e.g. Thu=Thursday)\n').title().strip()
        day = Days[day]
        month = 'all'
    else:
        day = 'all' ; month = 'all'
    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.dropna(inplace=True)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    month = Months.index(month.lower().strip()) + 1

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]  # filter by month to create the new dataframe

    if day.title().strip() in list(Days.keys()):
        day = Days[day.title().strip()]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]  # filter by day of week to create the new dataframe

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]    # The number of The month
    print("The Most Common Month:",Months[common_month - 1].title()) # The name of the month in Title case

    # display the most common day of week
    common_day_of_week = pd.DataFrame(df['day_of_week'].value_counts()).index[0]
    print("The Most Common Day of Week:",common_day_of_week)

    # display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("The Most Common Start Hour:",common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = pd.DataFrame(df['Start Station'].value_counts()).index[0]
    print("most commonly used start station:",common_start_station)
    # display most commonly used end station
    common_end_station = pd.DataFrame(df['End Station'].value_counts()).index[0]
    print("most commonly used end station:",common_end_station)
    # display most frequent combination of start station and end station trip
    most_frequent_start_station_and_end_station_trip = pd.DataFrame(df[['Start Station','End Station']].value_counts()).index[0]
    print("most frequent start station and end station trip: (",most_frequent_start_station_and_end_station_trip[0], " => ",most_frequent_start_station_and_end_station_trip[1]," )")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The Total Travel Time:",np.sum(df['Trip Duration']))

    # display mean travel time
    print("The Mean Travel Time:",np.mean(df['Trip Duration']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Type info:")
    print("-"*15)
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df:
        print("\nGender info:")
        print("-"*15)
        print(df['Gender'].value_counts(),"\n")
    # Display earliest, most recent, and most common year of birth
        print('The Earliest Year:   ', np.max(df['Birth Year']))
        print('The Most Recent Year:',np.min(df['Birth Year']))
        print('The Most Common Year:',df['Birth Year'].mode()[0])
    else:
        print('Gender And Birth Year stats cannot be calculated because They do not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month,day)
        #df = load_data('washington','may','all')
        print("number of dataframe rows is:",df.shape[0])
        print("number of dataframe columns is:",df.shape[1])
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        view_data = input("Would you like to view 5 rows of individual trip data? Enter [yes] or [no]?").lower().strip()
        start_loc = 0
        while view_data == 'yes':
            print(df.iloc[start_loc:(start_loc + 5)])
            start_loc += 5
            view_display = input("Do you wish to continue?type[yes|No]: ").lower().strip()
            if view_display == 'no':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower().strip()
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
#print("number of dataframe rows is:",df.shape[0]) #will excute 300000
#print("number of dataframe columns is:",df.shape[1])