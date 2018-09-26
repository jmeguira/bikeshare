## TODO: import all necessary packages and functions
import time
import datetime
import csv


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

## Month dict to ensure proper user input and help with output
months = {1 : {'days':31, 'name': 'January'},
        2 : {'days':28, 'name': 'February'},
        3 : {'days':31, 'name': 'March'},
        4 : {'days':30, 'name': 'April'},
        5 : {'days':31, 'name': 'May'},
        6 : {'days':30, 'name': 'June'}}

## day dict used to convert datetime integer representation to output
days = {0 : 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'}


def get_data(filename, time_period):
    '''returns the data to be operated on in the user query as a list of dicts
    Args:
        filename- Filename of the csv to be opened and worked with

        time_period- month, day, or none. tells how much data filter out, if any

    returns:
        (list) appropriately filtered data set for a given city file as a list of ordered dictionaries

    converting the DictReader iterator into a list of dictionaries taken from https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries/21572244'''

    with open(filename, newline = '') as csvfile:
        city_dict = [{x: y for x, y in row.items()} for row in csv.DictReader(csvfile)]

    #no time filter
    if time_period == 'none':
        return city_dict

    if time_period == 'month':
        month = get_month()
        city_dict_filter = []
        for row in city_dict:
            #filter for correct month
            if int(row['Start Time'].split('-')[1]) == month:
                city_dict_filter.append(row)
        return city_dict_filter

    if time_period == 'day':
        month = get_month()
        day = get_day(month)
        city_dict_filter = []
        for row in city_dict:
            #used x here for code cleanliness
            x = row['Start Time'].split('-')
            #filter for correct month and day
            if int(x[1]) == month and int(x[2][0:2]) == day:
                city_dict_filter.append(row)
        return city_dict_filter


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''

    x = True
    while x:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n')
        # TODO: handle raw input and complete function
        if city.lower() in ['chicago', 'new york', 'washington']:
            if city.lower() == 'new york':
                return 'new_york_city.csv'
            else:
                return '{}.csv'.format(city.lower())
        else:
            print('That input is not accepted, try again.')
            continue


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) returns user specified time filter period
    '''

    # TODO: handle raw input and complete function
    x = True
    while x:
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')
        if time_period.lower() in ['month', 'day', 'none']:
            return time_period.lower()
        else:
            print('That input is not accepted, try again.')



def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (int) returns integer representation of user's month input
    '''

    # TODO: handle raw input and complete function
    x = True
    x2 = ['january','february','march','april','may','june']
    while x:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
        if month.lower() in ['january','february','march','april','may','june']:
            return x2.index(month.lower()) + 1
        else:
            print('That input is not accepted, try again.')


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        (int) month index representation
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (int) returns a user specified day within a target month
    '''

    x = True
    while x:
        day = int(input('\nWhich day? Please type your response as an integer.\n'))
        # TODO: handle raw input and complete function
        # makes sure that the user selected day is available in the target month
        if day > 0 and day <= months[month]['days']:
            return day
        else:
            print('That input is not accepted, try again.')


def popular_month(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?

    description: iterates over a list of dicts with city data points and finds the most popular month for bike rides

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating the most popular month and how many bike rides in that month

    '''
    # TODO: complete function

    print('Calculating most popular month...')
    if len(data) == 0:
        print('No data in this time period')
        return

    start_time = time.time()
    #buckets for counting, 0 is january etc
    count = [0,0,0,0,0,0]
    for x in data:
        count[int(x['Start Time'].split('-')[1])-1] += 1
    maxcount = max(count)
    print('The most popular month was {} with a total of {} rides.'.format(months[count.index(maxcount)+1]['name'],str(maxcount)))
    print("That took %s seconds.\n" % (time.time() - start_time))

def popular_day(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?

    description: iterates over a list of dicts with city data points and finds the most popular day of the week for bike rides

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating the most popular day of the week and how many bike rides on that day
    '''
    # TODO: complete function

    print('Calculating most popular day...')
    if len(data) == 0:
        print('No data in this time period')
        return
    start_time = time.time()
    #buckets for counting, 0 is monday, 6 is sunday
    count = [0,0,0,0,0,0,0]
    for x in data:
        #split start time to find day of the week
        y = x['Start Time'].split('-')
        #only time datetime is used, need correct formatting from start time to generate correct answers
        count[datetime.date(int(y[0]),int(y[1]),int(y[2][0:2])).weekday()] += 1
    maxcount = max(count)
    print('The most popular day was {} with a total of {} rides.'.format(days[count.index(maxcount)],str(maxcount)))
    print("That took %s seconds.\n" % (time.time() - start_time))


def popular_hour(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?

    description: iterates over a list of dicts with city data points and finds the most popular hour for bike rides

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating the most popular hour and how many bike rides in that month
    '''
    # TODO: complete function
    print('Calculating most popular hour...')
    if len(data) == 0:
        print('No data in this time period')
        return
    start_time = time.time()
    #buckets for counting
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in data:
        #count, relies on hour of day being first : instance
        y = x['Start Time'].find(':')
        count[int(x['Start Time'][(y-2):y])] += 1
    maxcount = max(count)
    #only way I saw to handle outputting am/pm hours correctly, 1200 is 12pm, 2400 is 12 am
    if count.index(maxcount) == 0:
        print('The most popular hour was 12 am with a total of {} rides.'.format(str(maxcount)))
    elif count.index(maxcount) == 12:
        print('The most popular hour was 12 pm with a total of {} rides.'.format(str(maxcount)))
    elif count.index(maxcount) > 12:
        print('The most popular hour was {} pm with a total of {} rides.'.format(str(count.index(maxcount)-12),str(maxcount)))
    else:
        print('The most popular hour was {} am with a total of {} rides.'.format(str(count.index(maxcount)),str(maxcount)))
    print("That took %s seconds.\n" % (time.time() - start_time))


def trip_duration(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?

    description: iterates over a list of dicts with city data points and finds the total trip duration and average trip duration for bike rides
    in this period

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating trip duration statistics
    '''
    # TODO: complete function
    print('Calculating trip duration statistics...')
    if len(data) == 0:
        print('No data in this time period')
        return

    start_time = time.time()
    total = 0
    average = 0
    for x in data:
        total += int(float(x['Trip Duration']))
    #this is what caused me to add the data length catch. got a divide by 0 error in one of the test cases
    average = total / (len(data))
    print('The total duration of all {} bike rides in this period was {} seconds'.format(len(data),total))
    print('The average duration of a bike ride in this period was {} seconds'.format(average))
    print("That took %s seconds.\n" % (time.time() - start_time))


def popular_stations(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?

    description: iterates over a list of dicts with city data points and finds the most popular stations for bike rides

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating the most popular start and end stations for the data set

    '''
    # TODO: complete function
    print('Calculating popular station statistics...')
    if len(data) == 0:
        print('No data in this time period')
        return

    start_time = time.time()
    #dicts for start and end stations
    count1 = {}
    count2 = {}
    #populating dicts and counting number of rides
    for x in data:
        if x['Start Station'] in count1:
            count1[x['Start Station']] += 1
        else:
            count1[x['Start Station']] = 1
        if x['End Station'] in count2:
            count2[x['End Station']] += 1
        else:
            count2[x['End Station']] = 1
    #lists needed for evaluating max values, order is necessary for correct output, couldn't sort
    station = []
    trips = []
    for x,y in count1.items():
        station.append(x)
        trips.append(y)
    #index of max trips is same as index of station with max trips
    max1 = trips.index(max(trips))
    print('The most popular start station was {} with {} ride starts.'.format(station[max1],trips[max1]))
    #repeat above process for end station
    station2 = []
    trips2 = []
    for x,y in count2.items():
        station2.append(x)
        trips2.append(y)
    max2 = trips2.index(max(trips2))
    print('The most popular end station was {} with {} ride ends.'.format(station2[max2],trips2[max2]))
    print("That took %s seconds.\n" % (time.time() - start_time))

def popular_trip(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    description: iterates over a list of dicts with city data points and finds the most popular trip for bike riders

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating the most popular trip and how many bike rides in the data set
    '''
    # TODO: complete function
    print('Calculating most popular trip...')
    if len(data) == 0:
        print('No data in this time period')
        return

    start_time = time.time()

    #essentially the same procedure as popular stations, depends on clean data in the data set
    #added : in order to easily generate output with split function
    count = {}
    for x in data:
        if x['Start Station'] + ':' + x['End Station'] in count:
            count[x['Start Station'] + ':' + x['End Station']] += 1
        else:
            count[x['Start Station'] + ':' + x['End Station']] = 1
    station = []
    trips = []
    for x,y in count.items():
        station.append(x)
        trips.append(y)
    max1 = trips.index(max(trips))
    print('The most popular trip was from {} to {} with a total of {} rides.'.format(station[max1].split(':')[0],station[max1].split(':')[1],trips[max1]))

    print('That took %s seconds.\n' % (time.time() - start_time))


def users(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?

    description: iterates over a list of dicts with city data points and finds the user counts for bike rides in the data set

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating the user counts for the data set
    '''
    # TODO: complete function
    print('Calculating user type statistics...')
    if len(data) == 0:
        print('No data in this time period')
        return

    start_time = time.time()
    count = [0,0]
    #access user type in data set and count using buckets
    for x in data:
        if x['User Type'] == 'Subscriber':
            count[0] += 1
        elif x['User Type'] == 'Customer':
            count[1] += 1
        else:
            continue
    print('There were {} subscriber user types and {} customer user types in this time period.'.format(str(count[0]),str(count[1])))
    print("That took %s seconds.\n" % (time.time() - start_time))

def gender(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    description: iterates over a list of dicts with city data points and finds the gender counts for riders in the data set

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating the gender counts for riders in the data set
    '''
    # TODO: complete function
    print('Calculating user gender statistics...')
    if len(data) == 0:
        print('No data in this time period')
        return

    start_time = time.time()
    count = [0,0]
    #access user gender and count using buckets
    for x in data:
        if x['Gender'] == 'Male':
            count[0] += 1
        elif x['Gender'] == 'Female':
            count[1] += 1
        else:
            continue
    print('There were {} subscriber male users and {} female in this time period.'.format(str(count[0]),str(count[1])))
    print("That took %s seconds.\n" % (time.time() - start_time))

def birth_years(data):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest, most recent, and most popular birth years?
    description: iterates over a list of dicts with city data points and finds the most popular birth year for bike riders as well as oldest and youngest riders

    arguments:
        data - a list of dicts containing all the data points to be evaluated

    return values:
        none, prints a string stating user age data for the data set
    '''
    # TODO: complete function
    print('Calculating most popular trip...')
    if len(data) == 0:
        print('No data in this time period')
        return

    start_time = time.time()

    count = {}
    for x in data:
        if x['Birth Year'] in count:
            count[x['Birth Year']] += 1
        else:
            count[x['Birth Year']] = 1
    year = []
    riders = []
    for x,y in count.items():
        if x != '':
            year.append(int(float(x)))
            riders.append(y)
    max1 = riders.index(max(riders))
    print('The most popular birth year was {} with {} riders.'.format(year[max1],riders[max1]))
    #after calculating year frequency, okay to sort year list to find oldest and youngest riders
    year.sort()
    print('The earliest birth year was {} and the most recent was {}.'.format(year[0],year[-1]))
    print('That took %s seconds.\n' % (time.time() - start_time))

def print_data(data):
    #helper function for display_data(), pops the first item in the data set to keep place
    for i in range(5):
        for k,v in data.pop(0).items():
            print(k + ' : ' + v)
        print('\n')

def display_data(data):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        none, prints out data points in order until user exits function
    '''
    # TODO: handle raw input and complete function


    #this could definitely be cleaner
    x = True
    while x == True:
        display = input('Would you like to view individual trip data? Type \'yes\' or \'no\'. \n')
        if display.lower() == 'yes':
            #if less than 5 data entries left, return to avoid error
            if len(data) <= 5:
                print('Not enough data to display.')
                return
            print_data(data)
            while display == 'yes':
                display = input('Would you like to view more individual trip data? Type \'yes\' or \'no\'. \n')
                if len(data) <= 5:
                    print('Not enough data remaining.')
                    return

                if display.lower() == 'yes':
                    print_data(data)
                elif display.lower() == 'no':
                    return
                else:
                        print('That input is not accepted, try again.')
        elif display.lower() == 'no':
            break
        else:
            print('That input is not accepted, try again.')
            continue


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    # Filter by time period (month, day, none)
    time_period = get_time_period()
    # filter data set by user designated time period
    data = get_data(city, time_period)
    # What is the most popular month for start time?
    if time_period == 'none':
        popular_month(data)
    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'month' or time_period == "none":
        popular_day(data)
    # What is the most popular hour of day for start time?
    popular_hour(data)
    # What is the total trip duration and average trip duration?
    trip_duration(data)
    # What is the most popular start station and most popular end station?
    popular_stations(data)
    # What is the most popular trip?
    popular_trip(data)
    # What are the counts of each user type?
    users(data)
    # What are the counts of gender?
    # What are the earliest, most recent, and most popular birth years?
    if city == "chicago.csv" or city == "new_york_city.csv":
        gender(data)
        birth_years(data)
    # Display five lines of data at a time if user specifies that they would like to
    display_data(data)

    #Restart?
    x = True
    while x:
        restart = input('Would you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() == 'yes':
            statistics()
        elif restart.lower() == 'no':
            print('Exiting...')
            return
        else:
            print('That input is not accepted, try again.')
            continue


if __name__ == "__main__":
	statistics()
