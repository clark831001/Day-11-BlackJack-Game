from art import logo
import random
import replit


#cards list:
Computer_cards=[]
User_cards=[]

#function parts
def deal_card():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def sumcardnums(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)
def comparescore(computer_score,user_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎" 
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def playgame():
    print(logo)
    for n in range(2):
        Computer_cards.append(deal_card())
        User_cards.append(deal_card())
    is_game_over = False
    
    while not is_game_over:
        Computer_scores=sumcardnums(Computer_cards)
        User_scores=sumcardnums(User_cards)
        print(f"Your card: {User_cards} and current score: {User_scores}")
        print(f"Computer fist card {Computer_cards[0]}")

        if Computer_scores==0 or User_scores==0 or User_scores>21:
            is_game_over=True
        else:
            add_card=input("Do you want to add more cards? y for more, any key to skip>>").lower()
            if add_card=="y":
                User_cards.append(deal_card())
            else:
                is_game_over=True
    while Computer_scores != 0 and Computer_scores < 17:
        Computer_cards.append(deal_card())
        Computer_scores = sumcardnums(Computer_cards)

    
    print(f"Your final score is {User_scores} and your final hand is {User_cards}")
    print(f"Computer final score is {Computer_scores} and computer final hand is {Computer_cards}")
    print(comparescore(Computer_scores,User_scores))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  list.clear(User_cards)
  list.clear(Computer_cards)
  replit.clear()
  playgame()
