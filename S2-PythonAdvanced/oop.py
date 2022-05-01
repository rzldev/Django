## Object Oriented Programming ##

## Creating a Object
from pickle import FALSE
from random import shuffle


class Sample():
    pass

x = Sample()
print(type(x))


## Attributes and Methods
class Animal():

    # Class Attributes
    kingdom = 'Animal'

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    # Class Methods
    def greets(self):
        print('{x} {x} {x}!'.format(x = self.sound))

dog = Animal('Dog', 'Woof')
print(dog.name)
print(dog.sound)
print(dog.kingdom)
dog.greets()

cat = Animal(name='Cat', sound='Meow')
print(cat.name)
print(cat.sound)
print(cat.kingdom)
cat.greets()


## Inheritance
class Superhero():

    def __init__(self):
        print('Superhero born.')

    def whoAmI(self):
        print('I am a superhero.')

    def fly(self):
        print('I\'m flying.')

class Superman(Superhero):

    def __init__(self):
        self.name = 'Superman'

    def whoAmI(self):
        print('I\'m Superman.')

class Batman(Superhero):

    def __init__(self):
        self.name = 'Batman'

    def whoAmI(self):
        print('I\'m Batman.')

    def fly(self):
        print('I cannot fly. I\'m gliding.')

superman = Superman()
superman.whoAmI()
superman.fly()

batman = Batman()
batman.whoAmI()
batman.fly()


## Special Method
class Book():

    # Special method init
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    # Special method str
    def __str__(self):
        return 'name: {}, author: {}, pages: {}'.format(self.name, self.author, self.pages)

    # Special method len
    def __len__(self):
        return 3

    # Special method delete / destroy
    def __del__(self):
        print('{} book is destroyed!'.format(self.name))

python_book = Book('Python', 'Bob', 1)
print(python_book)
print(len(python_book))
del python_book


## Just some exercises
## Simple Black Jack Game

SUITES = 'Heart Diamond Club Spade'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# Deck class
class Deck():
    def __init__(self):
        print('CREATING A NEW ORDERED DECK!')
        self.all_cards = [(s, r) for s in SUITES for r in RANKS]

    def new(self):
        self.all_cards = [(s, r) for s in SUITES for r in RANKS]
        self.shuffle()

    def shuffle(self):
        print('SHUFFLING CARD')
        shuffle(self.all_cards)

    def take_card_from_deck(self):
        print('TAKING CARD')
        return self.all_cards.pop()

# Player's hand class
class Hand():
    def __init__(self):
        self.cards = []

    def __str__(self):
        return self.cards

    def start_new(self):
        self.cards = []

    def score(self):
        s = 0
        count_ace = 0

        for card in self.cards:
            if card[1] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                s += int(card[1])
            elif card[1] in ['J', 'Q', 'K']:
                s += 11
            elif card[1] == 'A':
                count_ace += 1

        if count_ace > 0:
            s += count_ace
            for _ in range(count_ace):
                if (s + 10 <= 21): s += 10

        return s

    def add_card(self, card):
        self.cards.append(card)

    def is_busted(self):
        return self.score() > 21

# Player class
class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.chips = 1000

    def hit(self, card):
        print(('PUTTING CARD ONTO {}\'S HAND').format(self.name).upper())
        self.hand.add_card(card)

    def stand(self):
        pass

    def win(self, chips_earned):
        print('YOU WIN!!!')
        self.chips += chips_earned

    def lose(self, chips_loss):
        print('YOU LOST!!!')
        self.chips -= chips_loss

# Start
if __name__ == '__main__':
    print('\n\n\n\n')
    print('Welcome to BlackJack')

    player_hand = Hand()
    player_name = input('What\'s your name? ')
    player = Player(player_name, player_hand)

    dealer_hand = Hand()
    dealer = Player('Dealer', dealer_hand)

    round_start = True
    
    while round_start:
        print()
        deck = Deck()
        deck.new()

        dealer.hand.start_new()
        player.hand.start_new()

        # Make a bet
        bet_chips = input('How many chips you are going to bet (you have {} chips)? '.format(player.chips))
        if (player.chips < int(bet_chips)):
            print('LIAR!!! YOU DON\'T HAVE THAT MUCH MONEY!!!')
            round_start = False
            break

        # Prepare cards
        print('')
        dealer.hit(deck.take_card_from_deck())
        player.hit(deck.take_card_from_deck())

        # Init status
        player_turn = True
        dealer_turn = True
        is_doubled = False

        # Player's turn
        while player_turn:
            print()
            print('Dealer\'s cards: {}, score: {}'.format(dealer.hand.cards, dealer.hand.score()))
            print('Your bet: {}'.format(bet_chips))
            print('Your cards: {}, score: {}'.format(player.hand.cards, player.hand.score()))
            
            action = input('Choose action (hit/stand/double): ')

            # Check action
            if action == 'hit':
                player.hit(deck.take_card_from_deck())

            elif action == 'stand':
                player_turn = False

            elif action == 'double':
                if is_doubled:
                    print('\nYou already doubled your bet')
                else:
                    if player.chips >= int(bet_chips) * 2:
                        is_doubled = True
                        bet_chips = str(int(bet_chips) * 2)
                    else:
                        print('\nYou don\'t have enough chips')
                    
            else:
                print('Invalid action!')

            # Player busted
            if player.hand.is_busted():
                print('\nYour cards: {}, score: {}'.format(player.hand.cards, player.hand.score()))
                print('BUSTED!!!')
                player.lose(int(bet_chips))
                player_turn = False

        # Dealer's turn
        if player.hand.is_busted() == False:
            while dealer_turn:
                if dealer.hand.score() < 15:
                    dealer.hit(deck.take_card_from_deck())
                else:
                    dealer_turn = False

                # Dealer busted
                if dealer.hand.is_busted():
                    print('\nDealer\'s cards: {}, score: {}'.format(dealer.hand.cards, dealer.hand.score()))
                    print('DEALER BUSTED!!!')
                    player.win(int(bet_chips))
                    dealer_turn = False

        # Checking score
        if (player.hand.is_busted() == False and dealer.hand.is_busted() == False):
            print('\n\n')
            print('Dealer\'s cards: {}, score: {}'.format(dealer.hand.cards, dealer.hand.score()))
            print('Your cards: {}, score: {}'.format(player.hand.cards, player.hand.score()))
            if (player.hand.score() >= dealer.hand.score()):
                player.win(int(bet_chips))
            else:
                print('DEALER WINS!!!')
                player.lose(int(bet_chips))

        # Play Again
        if (player.chips < 150):
            print('You are broke! You are not allowed to play again!')
            player_turn = False
            round_start = False
        else:
            play_again = input('Do you want to play again (y/n)? ')
            if play_again.lower() == 'n':
                round_start = False