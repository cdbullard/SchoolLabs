hour = int(input("Enter hour: "))
while hour < 1 or hour > 12:
    print("Hour must be from 1 to 12.")
    hour = int(input("Enter hour: "))

minute = int(input("Enter minute: "))
while minute < 0 or minute > 59:
    print("Minute must be from 0 to 59.")
    minute = int(input("Enter minute: "))

second = int(input("Enter second: "))
while second < 0 or second > 59:
    print("Second must be from 0 to 59.")
    second = int(input("Enter second: "))

# This is why we have the 2400 hour day format!!! :)
forgotten_latin_phrases = input("Enter AM or PM: ")
while forgotten_latin_phrases.upper() not in ("AM", "PM"):
    print("Must be either AM or PM")
    forgotten_latin_phrases = input("Enter AM or PM: ")

afternoon_seconds = 43200 # 3600 seconds * 12 hours

if forgotten_latin_phrases.upper() == "PM" and hour < 12:
    seconds_since_midnight = 3600 * hour + minute * 60 + second + afternoon_seconds
    print("Seconds since midnight: ", seconds_since_midnight)
elif forgotten_latin_phrases.upper() == "PM" and hour == 12:
    seconds_since_midnight = 3600 * hour + minute * 60 + second
    print("Seconds since midnight: ", seconds_since_midnight)
elif forgotten_latin_phrases.upper() == "AM" and hour != 12:
    seconds_since_midnight = 3600 * hour + minute * 60 + second
    print("Seconds since midnight: ", seconds_since_midnight)
elif forgotten_latin_phrases.upper() == "AM" and hour == 12:
    hour = 0
    seconds_since_midnight = 3600 * hour + minute * 60 + second
    print("Seconds since midnight: ", seconds_since_midnight)
else:
    x = 0
    while x == 0:
        print("Don\'t press CTRL + C")

