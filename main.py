import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        value = 0
        for card in self.hand:
            value += card.value
        return value

class Blackjack:
    def __init__(self, player_name):
        self.deck = Deck()
        self.player = Player(player_name)
        self.dealer = Player("Dealer")

    def start(self):
        self.deck.shuffle()
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

    def hit(self):
        self.player.add_card(self.deck.deal())

    def stand(self):
        while self.dealer.get_value() < 17:
            self.dealer.add_card(self.deck.deal())
        if self.dealer.get_value() > 21:
            print("Dealer busts! Player wins.")
        elif self.player.get_value() > self.dealer.get_value():
            print("Player wins!")
        elif self.player.get_value() == self.dealer.get_value():
            print("It's a tie!")
        else:
            print("Dealer wins.")

def main():
    player_name = input("Enter your name: ")
    game = Blackjack(player_name)
    game.start()

    print("Your hand:")
    for card in game.player.hand:
        print(card)
    print(f"Total value: {game.player.get_value()}")
    print("Dealer's hand:")
    print(game.dealer.hand[0])
    print("???")

    while True:
        action = input("Would you like to hit or stand? ")
        if action == "hit":
            game.hit()
            print("Your hand:")
            for card in game.player.hand:
                print(card)
            print(f"Total value: {game.player.get_value()}")
            if game.player.get_value() > 21:
                print("You bust! Dealer wins.")
                break
        elif action == "stand":
            game.stand()
            break
        else:
            print("Invalid action. Please enter 'hit' or 'stand'.")

if __name__ == "__main__":
    main()

