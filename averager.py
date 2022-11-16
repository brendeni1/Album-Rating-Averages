import os

# Clear terminal based on OS.
cls = lambda: os.system("cls") if os.name == "nt" else os.system("clear")

cls()
print(
    "Put in newline delimited averages. Double-Enter to exit. Ex:\n\n> 5.6/10\n> 5/10\n"
)

ratings = []

while True:
    user_input = input("> ")

    if user_input == "":
        break
    elif user_input == "--/10":
        continue
    else:
        ratings.append(user_input)

cls()

try:
    cleanRatings = [float(i.replace("/10", "")) for i in ratings]
except:
    exit("You screwed something up... Format it as stated.")

average = round(sum(cleanRatings) / len(cleanRatings), 1)

print(f"Your Ratings:")
print()
print("\n".join(ratings))
print()
print(f"Average Rating: {average}/10")
