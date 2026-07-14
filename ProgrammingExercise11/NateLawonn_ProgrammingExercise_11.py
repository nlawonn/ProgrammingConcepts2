import random

class Deck:
    #Constructs the deck of cards with rank and suit, n_decks times.
    def __init__(self, n_decks=1):
        self.card_list = [
            num + suit
            for suit in '\u2665\u2666\u2663\u2660'
            for num in 'A23456789TJQK'
            for _ in range(n_decks)
        ]

        #Creates a list of cards in play and discarded. Discarded cards 
        #are not immediately available.
        #Shuffles deck for random dealing.
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        #Clears self.discards_list, shuffles deck and returns to self.card_list
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")

        #Removes one card from self.card_list using pop
        #Appends card to self.cards_in_play_list
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def return_card(self, card):
        #Not immediately available: goes to self.discards_list,
        #Will only be used when deal() reshuffles discards back.
        if card in self.cards_in_play_list:
            self.cards_in_play_list.remove(card)
        self.discards_list.append(card)

#Prints h hand as "Hand:..."
def show_hand(h):
    print("Hand:", h)

#Creates 1 deck object, repeats a full deck my_deck times
#Builds a list of five iterations, calling my_deck.deal
#Prints the hand
def deal_initial_hand(deck, hand_size=5):
    # Deal `hand_size` cards into a list and return it.
    return [deck.deal() for _ in range(hand_size)]

def prompt_cards_to_redeal(max_cards=5):
    # Keep asking until the user enters a valid integer in [0, 5].
    while True:
        new_deal = input(f"How many cards do you want redealt? (1-5, 0 to stop): ").strip()
        if new_deal == "":
            print("Please enter a number.")
            continue

        try:
            cards = int(new_deal)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if 0 <= cards <= max_cards:
            return cards
        print(f"Please enter a number from 0 to {max_cards}.")


def choose_positions(cards, hand_size=5):
    # If redealing all cards, return all indices (1-5).
    if cards == hand_size:
        return list(range(hand_size))

    # Otherwise, prompt for unique positions within the current hand.
    positions = []
    while len(positions) < cards:
        pos = input(f"Enter a hand position to return (1-{hand_size}): ").strip()
        if pos == "":
            print("Please enter a number.")
            continue

        try:
            pos = int(pos)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        new_card = pos - 1
        if new_card < 0 or new_card >= hand_size:
            print("Invalid position. Try again.")
            continue

        if new_card in positions:
            print("That position is already selected. Choose a different one.")
            continue

        positions.append(new_card)
    return positions

def redeal_positions(deck, hand, positions):
    # For each chosen index in the hand:
    # return the old card, then deal a replacement into the same hand slot.
    for new_card in positions:
        old_card = hand[new_card]
        deck.return_card(old_card)
        hand[new_card] = deck.deal()

def main():
    #Creates 1 deck object, repeats a full deck my_deck times
    #Builds a list of five iterations, calling my_deck.deal
    #Prints the hand
    my_deck = Deck(1)
    hand = deal_initial_hand(my_deck, hand_size=5)
    show_hand(hand)

    while True:
        cards = prompt_cards_to_redeal(max_cards=5)
        if cards == 0:
            break
        #Redeal selected positions
        positions = choose_positions(cards, hand_size=5)
        redeal_positions(my_deck, hand, positions)
        show_hand(hand)

if __name__ == "__main__":
    main()