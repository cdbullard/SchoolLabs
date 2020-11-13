import random


# TODO: add unit tests
class Card:
    def __init__(self, suit, key, val):
        self.suit = suit
        self.value = {"card": key, "value": val}

    def show(self):
        return "{} of {}".format(self.value["card"], self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        self.build(game="blackjack")

    def build(self, game):
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        value_keys = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King",
                      "Ace"]
        # TODO: add more games
        if game == "blackjack":
            value_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]]
        else:
            value_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        values = {value_keys[i]: value_value[i] for i in range(len(value_keys))}
        # print(values)
        for suit in suits:
            for k in values:
                self.cards.append(Card(suit, k, values[k]))

    def show(self):
        # count = 0
        for card in self.cards:
            card.show()
            return card
            # count += 1
        # print(count)

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        for card in self.hand:
            card.show()

    def hand_total(self):
        position = len(self.hand) - 1
        # TODO: add logic to handle other games aside from blackjack, and move below section into blackjack game logic
        if self.name == "Dealer":
            if isinstance(self.hand[position].value["value"], list):
                if 17 > self.total + self.hand[position].value["value"][1] < 21:
                    self.hand[position].value["value"] = self.hand[position].value["value"][1]
                elif 17 > self.total and self.total + self.hand[position].value["value"][1] < 21:
                    self.hand[position].value["value"] = self.hand[position].value["value"][1]
                else:
                    self.hand[position].value["value"] = self.hand[position].value["value"][0]
        # TODO: consider giving player option to play two hands if dealt a pair of cards ie: 2 jacks or 2 sixes
        # Give player choice of how of value for the Ace
        elif self.name != "Dealer":
            if isinstance(self.hand[position].value["value"], list):
                ace_values = (1, 11)
                player_input = 0
                while player_input not in ace_values:
                    player_input = int(input("You have drawn an Ace, choose the value [1/11]: "))
                    if player_input == 1:
                        self.hand[position].value["value"] = self.hand[position].value["value"][0]
                    elif player_input == 11:
                        self.hand[position].value["value"] = self.hand[position].value["value"][1]
        self.total = self.total + self.hand[position].value["value"]
        return self.total


if __name__ == '__main__':
    # instantiate 52 card deck
    deck = Deck()
    # shuffle the deck
    deck.shuffle()
    # create players
    player = Player("Jessica")
    dealer = Player("Dealer")
    # start for game loop
    draw_card = 'Y'
    # begin game
    # draw two cards for player
    print("\nPlayer initial draw")
    for i in range(2):
        player.draw(deck)
        print("Player dealt: {}  {}'s Total: {}".format(player.hand[i].show(), player.name, player.hand_total()))
    # handle scenario where player gets Blackjack on first two cards
    # draw two cards for Dealer
    print("Dealer initial draw")
    for i in range(2):
        dealer.draw(deck)
        print("Dealer dealt: {}  {}'s Total: {}".format(dealer.hand[i].show(), dealer.name, dealer.hand_total()))
    if player.total == 21 and player.total != dealer.total:
        print("Blackjack! Player {} has won!".format(player.name))
        exit(0)
    elif player.total == 21 and dealer.total == 21:
        print("Dealer has won! That's really unfortunate.")
        exit(0)
    # If player total isn't 21 after two cards, continue with game flow
    else:
        print("\nDealer total: {}\nPlayer total: {}".format(dealer.total, player.total))
        while draw_card == 'Y':
            draw_card = input("Do you want another card? [y/n]: ").upper()
            if draw_card == 'Y':
                pass
            else:
                break
            player.draw(deck)
            print("Player dealt: {}  {}'s Total: {}".format(player.hand[(len(player.hand) - 1)].show(), player.name,
                                                            player.hand_total()))
            if player.total > 21:
                print("Bust! You've lost!")
                draw_card = "N"
                exit(0)
# If player stops and doesn't bust, continue with Dealer's hand
    if player.total <= 21:
        print("Dealer's turn")
        while player.total > dealer.total:
            if dealer.total >= 17:
                print("Dealer has 17 or more, Dealer must stand")
                break
            dealer.draw(deck)
            print("Dealer dealt: {}  {}'s Total: {}".format(dealer.hand[-1].show(), dealer.name, dealer.hand_total()))
            if dealer.total > 21:
                print("Dealer has busted! Player {} has won!".format(player.name))
                exit(0)
        if dealer.total >= player.total:
            print("Dealer has won!")
            exit(0)
        elif player.total > dealer.total:
            print("Player {} has won".format(player.name))
            exit(0)
