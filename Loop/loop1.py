name = ""
count = 0
MAX_TICKETS = 5  # max amount of tickets

while name != "Xxx" and count != MAX_TICKETS:  # while loop
    print(f" you have {MAX_TICKETS - count} tickets left")
    name = input("What's your name? ").title()  # input name
    count += 1  # count + 1

