# Get the time formatted as --> 13:19:49.078205
from datetime import datetime
import re


def time_format_check(input_time:str)->bool:
        """Function that checks if obtained current time is formatted as : "%H:%M:%S.%f"
        params: input_time : str
        return bool
        """
        if (re.fullmatch("\d{2}:\d{2}:\d{2}.\d{6}", input_time)):
            print(f"Curent time is : {input_time} and is corretly formatted like: \"%H:%M:%S.%f\"")
            return True
        else:
            return False
        

""" current_time_unformatted = datetime.now() # current date and time
current_time_formatted = current_time_unformatted.strftime("%H:%M:%S.%f")
result = time_format_check(current_time_formatted)
print(result) """