import os

# Clear terminal based on OS.
cls = lambda: os.system("cls") if os.name == "nt" else os.system("clear")

cls()
print(
    "Put in newline delimited averages. Double-Enter to exit. Ex:\n\n> 5.6/10\n> 5/10\n"
)

ratings = []

counter = 1

while True:
    user_input = input(f"{counter}. > ")

    if user_input == "":
        break
    elif user_input == "--/10":
        continue
    else:
        ratings.append(user_input)

        counter += 1

cls()

try:
    cleanRatings = [float(i.replace("/10", "")) for i in ratings]
except:
    exit("You screwed something up... Format it as stated.")

average = round(sum(cleanRatings) / len(cleanRatings), 1)

print(f"Your Ratings:")
print()

for num, rating in enumerate(ratings, start=1):

    print(f"{num}. {rating}")

print()
print(f"Average Rating: {average}/10")
