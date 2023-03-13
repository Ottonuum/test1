import random
suits = ['ärtu', 'poti', 'risti', 'ruutu']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'poiss', 'emand', 'kuningas', 'äss']
used_cards = []


while (next_suit + next_rank) in used_cards:
    next_suit = random.choice(suits)
    next_rank = random.choice(ranks)

used_cards.append(next_suit + next_rank)

return[next_suit, next_rank]
def get_hand_score(hand):
    score=0
    for card in hand:


    def:
        next_suit = random.choice(suits)
        next_rank = random.choice(ranks)

        while next_rank
        print(next_rank) 
        next_suit = random.choice
        next_rank = random

    for i in range(2):
        palyer_hand.append(choose_card())
        dealer_hand.append(choose_card())

        print(player_hand, get_hand_score)
