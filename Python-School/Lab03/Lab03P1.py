hour = int(input("Enter hour: "))
if hour > 12:
    raise ValueError("Please enter the hour in a 12 hour time format")
minute = int(input("Enter minute: "))
if minute > 59:
    raise ValueError("Minutes cannot be greater than 59")
second = int(input("Enter second: "))
if second > 59:
    raise ValueError("Seconds cannot be greater than 59")
# This is why we have the 2400 hour day format!!! :)
forgotten_latin_phrases = input("Enter AM or PM: ")
if forgotten_latin_phrases.upper() not in ("AM", "PM"):
    print(forgotten_latin_phrases.upper())
    raise ValueError("Must be AM or PM")
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

