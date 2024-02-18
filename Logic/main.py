import random

# this file will be used for counting cards and making decisions 
class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __eq__(self, other):
    return self.rank == other.rank and self.suit == other.suit
  
  def __str__(self):
    print_suit = self.suit
    match print_suit:
      case "H":
        print_suit = "hearts"
      case "C":
        print_suit = "clubs"
      case "D":
        print_suit = "diamonds"
      case default:
        print_suit = "spades"

    return f"{suit_dict[self.rank]} of {print_suit}"
  
  def get_game_value(self):
    if (self.rank >= 10):
      return 10
    else:
      return self.rank

# GLOBAL VARIABLES
init_deck = ['2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
    '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
    '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC',
    '2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS']

rank_dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
              "9": 9, "10": 10, "J": 11,"Q": 12, "K": 13}

suit_dict = {1:"Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 
              9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}

high_low_rank = {
  1:-1,
  2: 1,
  3: 1,
  4: 1,
  5: 1,
  6: 1,
  7: 0,
  8: 0,
  9: 0,
  10: -1,
  11: -1,
  12: -1,
  13: -1,
}

def generate_deck():
  cards = []
  for card in init_deck:
    cards.append(convert_to_card(card))
  random.shuffle(cards)
  return cards

def convert_to_card(card):
  return Card(
              rank_dict[card[:-1]],
              card[-1]
              )

def initalize_game():
  deck = generate_deck()
  running_count = 0
  return deck, running_count

def play_game(deck, running_count):
  print()
  while len(deck) > 0:
    deck, running_count = run_hand(deck, running_count)
    next_input = input("would you like to play another hand? (y/n) ")
    if next_input.lower() != "y":
      return
  

def get_statistic():
  print("hi")


def run_hand(deck, running_count):
  player_hand = []
  dealer_hand = []
  player_hand.append(deck[0])
  dealer_hand.append(deck[1])
  player_hand.append(deck[2])
  dealer_hand.append(deck[3])
  deck = deck[4:]

  player_hand = [Card(1, "H"), Card(1, "S")]

  print_hands(player_hand, dealer_hand)
  print()
  options = get_options(player_hand)
  # display_statistics = get_statistic()
  player_input = input(f"Would you like to {', '.join(options[:-1])}, or {options[-1]}? ")

  return deck, running_count

def print_hands(player_hand, dealer_hand):
  print("Your hand:")
  for card in player_hand:
    print(card)
  print(f"You have {calc_value(player_hand)}")

  if (check_blackjack(player_hand)):
    print("Blackjack!")
    # possibly return true if blackjack
    # return deck,running_count
  print()
  print("Dealer hand:")
  for card in dealer_hand:
    print(card)
  print(f"Dealer has {calc_value(dealer_hand)}")

  
def check_blackjack(hand):
  return calc_value(hand) == 21


def calc_value(hand):
    total = 0
    num_aces = 0
    for card in hand:
      if card.rank == 1:
        num_aces += 1
    for card in hand:
      if card.rank == 1:
        total += 11
      else:
        total += card.get_game_value()
    
    if total > 21 and num_aces > 0:
      for i in range(num_aces):
        if total > 21:
          total -= 10
    return total

def get_options(hand):
  options = ["hit", "stand", "double"]
  if len(hand) == 2:
    if hand[0].rank == hand[1].rank:
      options.append("split")
  return options

def main():
  deck, running_count = initalize_game()
  play_game(deck, running_count)    


if __name__ == "__main__":
  main()