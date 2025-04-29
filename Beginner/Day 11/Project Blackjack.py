import random

def draw_card(card_list, player_card, num_draw):
    """
    draw a card randomly from cards list and add it to player card list
    :param card_list: list of the cards (int)
    :param player_card: player/card list (int)
    :param num_draw: number of cards to draw (int)
    :return: None
    """
    for card in range(num_draw):
        player_card.append(random.choice(card_list))

def scoring(list):
    """
    Calculate the score of the list of cards
    :param list: player/computer list of cards (int)
    :return: Score of the list of cards
    """
    return sum(list)

def final_decision(player, comp):
    """
    Determine the result of a Blackjack game
    based on player and computer scores
    :param player: Player's score (int)
    :param comp: Computer's score (int)
    :return: Result of the game (str)
    """
    # Check for bust conditions
    if player > 21:
        return "You Bust! You lose."
    elif comp > 21:
        return "Computer Bust! You win."
    # Check for Blackjack conditions
    elif player == 21 and comp == 21:
        return "Both have a Blackjack. It's a tie!"
    elif player == 21:
        return "You have a Blackjack. You win!"
    elif comp == 21:
        return "Computer has a Blackjack. You lose."
    # Check if no Bust or Blackjack
    elif player == comp:
        return "it's a tie!"
    elif player > comp:
        return "You win!"
    elif player < comp:
        return "You lose."

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def Blackjack():
    """
    Blackjack Game
    :return: None
    """
    user_cards = []
    comp_cards = []
    play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_or_not== "y":
        draw_card(cards, user_cards, 2) # draw 2 card for user
        draw_card(cards, comp_cards, 2) # draw 2 card for computer)

        print(f"Your cards: {user_cards}, current score: {scoring(user_cards)}")
        print(f"Computer's first card: [{comp_cards[0]}, X]")
        ask_flag = False
        while not ask_flag:
            ask_user = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if ask_user == "y":
                draw_card(cards, user_cards, 1) # draw 1 card for computer
                print(f"Your cards: {user_cards}, current score: {scoring(user_cards)}")
            else:
                ask_flag = True
                if scoring(comp_cards) < 17:
                    seventeen = False
                    while not seventeen:
                        draw_card(cards, comp_cards, 1) # draw 1 card for computer
                        if scoring(comp_cards) >= 17:
                            seventeen = True
                print(f"Your final hand: {user_cards}, final score: {scoring(user_cards)}")
                print(f"Computer's final hand: {comp_cards}, final score: {scoring(comp_cards)}")
                print(final_decision(scoring(user_cards), scoring(comp_cards)))
                Blackjack()
    else:
        print("Goodbye!")

Blackjack()
