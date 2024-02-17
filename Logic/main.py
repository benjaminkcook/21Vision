# this file will be used for counting cards and making decisions 
def initalize_game():
  deck = ['2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
        '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
        '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC',
        '2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS']

  high_low_rank = {
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1,
    "6": 1,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": -1,
    "J": -1,
    "Q": -1,
    "K": -1,
    "A": -1
  }

  running_count = 0

  return deck, high_low_rank, running_count


def play_game(deck, high_low_rank, running_count):
  while True:
    if len(deck) > 0:
      card = input("Enter a card: ")
      if card not in deck:
        print("Card not in deck")
        continue

      running_count += high_low_rank[card[:-1]]
      deck.remove(card)
      print(f"Running count: {running_count}")

    else:
      restart = input("The deck is empty, play again? (y/n)")

      if restart == "y":
        deck, high_low_rank, running_count = initalize_game()
      
      else:
        break
  

def main():
  deck, high_low_rank, running_count = initalize_game()
  play_game(deck, high_low_rank, running_count)    


if __name__ == "__main__":
  main()