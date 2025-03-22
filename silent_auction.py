import art

print(art.logo)

def max_bid(bids):
    highest = 0
    for key in bids:
        if records[key] > highest:
            highest = bids[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest}.")

records = {}
more_bids = 'yes'
while more_bids == 'yes':
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    records[name] = bid

    more_bids = input("Are there any other bids? Type 'yes' or 'no'.\n").lower()
    if more_bids == 'yes':
        print("\n" * 500)
    elif more_bids == 'no':
        max_bid(records)


