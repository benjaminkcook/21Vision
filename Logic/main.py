# this file will be used for counting cards and making decisions 
class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

  def __eq__(self, other):
    return self.rank == other.rank and self.suit == other.suit
  
  def __str__(self):
    return f"{self.rank} of {self.suit}"

# GLOBAL VARIABLES
init_deck = ['2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
    '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
    '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC',
    '2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS']
rank_dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
              "9": 9, "10": 10, "J": 11,"Q": 12, "K": 13}
high_low_rank = {
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
  14: -1
}

def generate_deck():
  cards = []
  for card in init_deck:
    cards.append(convert_to_card(card))
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
  while True:
    deck, running_count = run_hand(deck, running_count)
    # if len(deck) > 0:
    #   card = convert_to_card(input("Enter a card: "))
    #   if card not in deck:
    #     print("Card not in deck")
    #     continue

    #   running_count += high_low_rank[card.rank]
    #   deck.remove(card)
    #   print(f"Running count: {running_count}")

    # else:
    #   restart = input("The deck is empty, play again? (y/n)")

    #   if restart == "y":
    #     deck, high_low_rank, running_count = initalize_game()
      
    #   else:
    #     break
  

def run_hand(deck, running_count):
  player_hand = []
  dealer_hand = []
  player_hand.append(deck[0])
  dealer_hand.append(deck[1])
  player_hand.append(deck[2])
  dealer_hand.append(deck[3])
  deck = deck[4:]

  print("Your hand:")
  print_hand(player_hand)
  print("Dealer hand:")
  for card in dealer_hand:
    if card == dealer_hand[0]:
      print("hidden")
      continue
    print(card)
  player_input = input("Would you like to hit, stand, or kys? ")
  if player_input.lower() == "hit":
    player_hand.append(deck[0])
    print_hand(player_hand)
    second_input = input("would you like to hit, stand or kys? ")
  return deck, running_count

def print_hand(hand):
  for card in hand:
    print(card)

def main():
  deck, running_count = initalize_game()
  play_game(deck, running_count)    


if __name__ == "__main__":
  main()