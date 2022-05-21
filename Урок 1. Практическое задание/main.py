seconds_in_hour = 3600
seconds_in_minute = 60


seconds = int(input("Enter a number of seconds: "))


hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print(" {0:.0f} hours, {1:.0f} minutes, {2:.0f} seconds.".format(
    hours, minutes, seconds))
