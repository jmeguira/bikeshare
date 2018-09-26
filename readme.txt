README for bikeshare.py

Only borrowed code was from the stackoverflow post for creating a list of ordered dicts from a csv file.
found here:
https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries/21572244

Run instructions:

1. place bikeshare.py in directory with new york, washington, and chicago csvs with appropriate filenames
2. navigate to this directory from the commandline
3. > python bikeshare.py
4. follow user prompts

Sample output:

Hello! Let's explore some US bikeshare data!
Would you like to see data for Chicago, New York, or Washington?
chicago

Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.
none
Calculating most popular month...
The most popular month was June with a total of 505164 rides.
That took 1.5077462196350098 seconds.

Calculating most popular day...
The most popular day was Tuesday with a total of 237586 rides.
That took 3.4538652896881104 seconds.

Calculating most popular hour...
The most popular hour was 5 pm with a total of 186899 rides.
That took 1.5329265594482422 seconds.

Calculating trip duration statistics...
The total duration of all 1551505 bike rides in this period was 1458069892 seconds
The average duration of a bike ride in this period was 939.7777590146342 seconds
That took 1.3126587867736816 seconds.

Calculating popular station statistics...
The most popular start station was Streeter Dr & Grand Ave with 36686 ride starts.
The most popular end station was Streeter Dr & Grand Ave with 39537 ride ends.
That took 1.5166354179382324 seconds.

Calculating most popular trip...
The most popular trip was from Lake Shore Dr & Monroe St to Streeter Dr & Grand Ave with a total of 4647 rides.
That took 2.2811849117279053 seconds.

Calculating user type statistics...
There were 1234339 subscriber user types and 317162 customer user types in this time period.
That took 0.45545482635498047 seconds.

Calculating user gender statistics...
There were 935854 subscriber male users and 298784 female in this time period.
That took 0.4222090244293213 seconds.

Calculating most popular trip...
The most popular birth year was 1989 with 76489 riders.
The earliest birth year was 1899 and the most recent was 2016.
That took 0.5866565704345703 seconds.

Would you like to view individual trip data? Type 'yes' or 'no'.
yes
Start Time : 2017-01-01 00:00:36
End Time : 2017-01-01 00:06:32
Trip Duration : 356
Start Station : Canal St & Taylor St
End Station : Canal St & Monroe St (*)
User Type : Customer
Gender :
Birth Year :


Start Time : 2017-01-01 00:02:54
End Time : 2017-01-01 00:08:21
Trip Duration : 327
Start Station : Larrabee St & Menomonee St
End Station : Sheffield Ave & Kingsbury St
User Type : Subscriber
Gender : Male
Birth Year : 1984.0


Start Time : 2017-01-01 00:06:06
End Time : 2017-01-01 00:18:31
Trip Duration : 745
Start Station : Orleans St & Chestnut St (NEXT Apts)
End Station : Ashland Ave & Blackhawk St
User Type : Subscriber
Gender : Male
Birth Year : 1985.0


Start Time : 2017-01-01 00:07:28
End Time : 2017-01-01 00:12:51
Trip Duration : 323
Start Station : Franklin St & Monroe St
End Station : Clinton St & Tilden St
User Type : Subscriber
Gender : Male
Birth Year : 1990.0


Start Time : 2017-01-01 00:07:57
End Time : 2017-01-01 00:20:53
Trip Duration : 776
Start Station : Broadway & Barry Ave
End Station : Sedgwick St & North Ave
User Type : Subscriber
Gender : Male
Birth Year : 1990.0


Would you like to view more individual trip data? Type 'yes' or 'no'.
no
Would you like to restart? Type 'yes' or 'no'.
no
Exiting...
