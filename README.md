# Bike Share Analysis

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Motivate, a bike-share system provider for many major cities in the United States, to uncover bike-share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.
The Datasets

## Meta Data
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

## The Program
The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! Four questions will change the answers:

- Would you like to see data for `Chicago`, `New York`, or `Washington`?
- Would you like to filter the data by `month`, `day`, or `not at all`?
- (If they chose `month`) Which month - January, February, March, April, May, or June?
- (If they chose `day`) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

- The script will also prompt the user whether they would like to see the raw data.

  If the user answers `'yes'`, then the script should print 5 rows of the data at a time,
  then ask the user if they would like to see 5 more rows of the data.
  The script should continue prompting and printing the next 5 rows at a time until the user chooses `'no'`,
  because they do not want any more raw data to be displayed.
