# Todo: Create a c_to_f(temp) function
import random


def c2f(t_c: int) -> float:
    pass

# test driven programming
# assert c2f(0) == 32, f"got {c2f(0)}"

# Todo: Create a list of reminders


# Todo: Get some input from the user
name = "xyz"
conditions = [
    "rainy",
    "sunny",
    "cloudy",
    "snowy"
]
weather_condition = random.choice(conditions)
temp_c = random.randint(18, 28)
reminders = [
    "do x",
    "do y",
    "do z"
]

# Todo: Create a string with email content that includes:
#       - A greeting
#       - The day's weather + temp in c and f
#       - Some reminders
#       - 1-2 more items based on APIs that you've found
greeting = f"greeting text to {name} " \
    f"and it continues to new line " \
    f"under weather condition: {weather_condition} " \
    f"and temperature of {temp_c}!\n" \
    f"Remember to:\n"
final_txt_place_holder = greeting
while len(reminders):
    final_txt_place_holder += f"- {reminder}\n"
for reminder in reminders:
    final_txt_place_holder += f"- {reminder}\n"

# Todo: Print the content to the console
print(final_txt_place_holder)