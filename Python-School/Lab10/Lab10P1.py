class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class FormatError(Error):
    """Exception raised for Formatting Errors in strings"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.issue = kwargs.get("issue")
        self.message = kwargs.get("message")


def time_slicing(time_input):
    """Checks a string for 24 hour time formatting [hh:mm:ss]"""
    try:
        if time_input.count(":") != 2:
            raise FormatError(message="Time must be input in [hh:mm:ss]",
                              issue=f"You have {time_input.count(':')} colons")
        time_list = time_input.split(":")
        hour = time_list[0]
        minute = time_list[1]
        second = time_list[2]
        if not hour.isdigit() or len(hour) != 2:
            raise FormatError(message="Hour must be input as a 2 digit integer [hh:mm:ss]",
                              issue=f"Hour input as {str(hour)}")
        if not minute.isdigit() or len(minute) != 2:
            raise FormatError(message="Minute must be input as a 2 digit integer [hh:mm:ss]",
                              issue=f"Minutes input as {str(minute)}")
        if not second.isdigit() or len(second) != 2:
            raise FormatError(message="Seconds must be input as a 2 digit integer [hh:mm:ss]",
                              issue=f"Seconds input as {str(second)}")
        if 0 < int(hour) > 23:
            raise FormatError(message="Hour must be an integer between 0 and 23",
                              issue=f"Hour input as {str(hour)}")
        if 0 < int(minute) > 59:
            raise FormatError(message="Minute must be an integer between 0 and 59",
                              issue=f"Minutes input as {str(minute)}")
        if 0 < int(second) > 59:
            raise FormatError(message="Seconds must be an integer between 0 and 59",
                              issue=f"Seconds input as {str(second)}")
    except FormatError as cha_cha_slide:
        print(cha_cha_slide.message, "\t---\t", cha_cha_slide.issue)
        exit("chickity check yoself\nbecause you just wrecked yoself\nor at the very least broke my code\n"
             "and I just really love the color red, so I keep adding things here")
    else:
        print("Time with colons removed:", ''.join(time_list))


if __name__ == '__main__':
    time = input("Enter time [hh:mm:ss]: ")
    time_slicing(time)

