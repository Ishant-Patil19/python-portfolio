from art import logo
import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def highest_bidder(bidding_record: dict):
    highest_bid = 0
    winner = ""
    for bidder, amount in bidding_record.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"\n🏆 Winner: {winner} with a bid of ${highest_bid}")

def main():
    print(logo)

    bids = {}
    continue_bidding = True

    while continue_bidding:
        name = input("What is your name?\n").strip()

        try:
            price = int(input("Enter your bid amount: $"))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        bids[name] = price

        should_continue = input("Are there other bidders? (yes/no): ").lower()

        if should_continue == "no":
            continue_bidding = False
            highest_bidder(bids)
        elif should_continue == "yes":
            clear_screen()
        else:
            print("❌ Invalid choice. Exiting.")
            break


if __name__ == "__main__":
    main()

