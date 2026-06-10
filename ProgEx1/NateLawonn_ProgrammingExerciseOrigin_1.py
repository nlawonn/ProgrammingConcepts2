def main():
    #Sets available tickets at 20 and buyer count at 0
    remaining_tickets = 20
    total_buyers = 0

    #Loops the ticket transaction until no remaining tickets
    while remaining_tickets > 0:
        tickets = int(input("How many tickets would you like to buy? "))

        # Catch both the updated ticket count AND the success status
        remaining_tickets, was_successful = process_purchase(tickets, remaining_tickets)

        # Only increment the buyer accumulator if the transaction actually went through
        if was_successful:
            total_buyers += 1
            print(f"Tickets remaining: {remaining_tickets}\n")

    #Displays when all the tickets have been sold and how many transactions
    print(f"All tickets sold! Total number of buyers: {total_buyers}")

def process_purchase(requested_tickets, current_remaining):
    #Does not allow more than 4 tickets in a single transaction
    if requested_tickets > 4:
        print("That number is not allowed. Please enter 4 or less.")
        # Transaction failed: remaining tickets stay the same, success is False
        return current_remaining, False

    #Does not allow more than the remaining number of tickets to be sold
    elif requested_tickets > current_remaining:
        print(f"We only have {current_remaining} tickets left!")
        return current_remaining, False

    #Successful transaction of 4 or less tickets within the remaining tickets
    else:
        print("Enjoy the show.")
        # Transaction succeeded: subtract tickets, success is True
        current_remaining -= requested_tickets
        return current_remaining, True

if __name__ == "__main__":
    main()
#test change
