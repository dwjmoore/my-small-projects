"""
This code runs a Monte Carlo simulation of Black Jack games
with the player using the Martingale betting system. That is,
the player dooubles his losing bet until he wins. Once he wins,
the player returns to the original bet.
"""



import random

sets = int(input("How many sets of games do you want to play? "))
sets_counter = sets
games = 500 #int(input("How many games do you want to play? "))
#counter = games

#Initial Conditions
p_score = 0
d_score = 0
push = 0
PandL = 0
goal = 650
starting_wager = 1
p_wins = True
stop = "go"
set_num = 0

#Sets of Games
while sets_counter > 0:
    sets_counter -= 1
    counter = games
    stop = "go"
    set_num += 1
    purse = 600
    wager = starting_wager

    #The Game
    while counter > 0 and stop != "stop":

        if p_wins == True:
            wager = starting_wager            
        elif p_wins == False:
            wager = wager * 2
        else:
            wager = wager
            
        if purse >= goal:
            print(f"You have reached your goal. Your purse is ${purse}.  You played {games - counter} games.")
            PandL += (purse - 600)
            stop = "stop"
        elif wager > 300:
            print(f"The wager is over $300.  You played {games - counter} games.")
            if purse > 600:
                PandL += (purse - 600)
            else:
                PandL -= (600 - purse)
            stop = "stop"
        elif wager > purse:
            print(f"You don't have enough money to make a bet. Your purse is ${purse} and the wager is ${wager}. You played {games - counter} games.")
            PandL -= (600 - purse)
            stop = "stop"
        elif purse == 0:
            print(f"You have run out of money! You played {games - counter} games.")
            PandL -= 600
            stop = "stop"
        
        if stop == "stop":
            print("To the next set.")
        else:

            counter -= 1
            starter_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
            game_deck = starter_deck
            player_hand = []
            split_hand1 = []
            split_hand2 = []
            dealer_hand = []
            print(f"Wager: ${wager}")

            #The Deal
            player_card = random.choice(game_deck)
            game_deck.remove(player_card)
            player_hand.append(player_card)

            dealer_card = random.choice(game_deck)
            game_deck.remove(dealer_card)
            dealer_hand.append(dealer_card)

            player_card = random.choice(game_deck)
            game_deck.remove(player_card)
            player_hand.append(player_card)

            dealer_card = random.choice(game_deck)
            game_deck.remove(dealer_card)
            dealer_hand.append(dealer_card)

            #print(f"player: {player_hand}")
            #print(f"dealer: {dealer_hand}")

            player_sum = int(sum(player_hand))
            dealer_sum = int(sum(dealer_hand))

            #print(player_sum)
            #print(dealer_sum)


            #Blackjacks
            if player_sum == 21 and dealer_sum == 21:
                push += 1
                p_wins = "push"
                print("Both player and dealer have blackjacks. Push!")
                print(f"Purse: ${purse}")
            elif player_sum == 21:
                p_score += 1
                purse += (wager*(3/2))
                p_wins = True
                print("21! Player wins!")
                print(f"Purse: ${purse}")
            elif dealer_sum == 21:
                d_score += 1
                purse -= wager
                p_wins = False
                print("21! Dealer wins!")
                print(f"Purse: ${purse}")
            else:
                #Player Splits
                if (player_hand == [2, 2] and (dealer_hand[0] >= 3 and dealer_hand[0] <= 7)) or (player_hand == [3, 3] and (dealer_hand[0] >= 4 and dealer_hand[0] <= 7)) or (player_hand == [6, 6] and (dealer_hand[0] >= 2 and dealer_hand[0] <= 6)) or (player_hand == [7, 7] and (dealer_hand[0] >= 2 and dealer_hand[0] <= 7)) or (player_hand == [8, 8]) or (player_hand == [9, 9] and ((dealer_hand[0] >= 2 and dealer_hand[0] <= 6) or (dealer_hand[0] >= 8 and dealer_hand[0] <= 9))) or (player_hand == [11, 11]):
                    split_hand1.append(player_hand[0])
                    split_hand2.append(player_hand[0])
                    player_card = random.choice(game_deck)
                    game_deck.remove(player_card)
                    split_hand1.append(player_card)
                    split_sum1 = int(sum(split_hand1))
                    player_card = random.choice(game_deck)
                    game_deck.remove(player_card)
                    split_hand2.append(player_card)
                    split_sum2 = int(sum(split_hand2))

                    #Play split_hand1
                    while split_sum1 <= 11:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand1.append(player_card)
                        split_sum1 = int(sum(split_hand1))
                        while split_sum1 > 21 and 11 in split_hand1:
                            split_hand1.remove(11)
                            split_hand1.append(1)
                            split_sum1 = int(sum(split_hand1))
                    
                    while split_sum1 == 12 and (dealer_hand[0] < 4 or dealer_hand[0] > 6):
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand1.append(player_card)
                        split_sum1 = int(sum(split_hand1))
                        while split_sum1 > 21 and 11 in split_hand1:
                            split_hand1.remove(11)
                            split_hand1.append(1)
                            split_sum1 = int(sum(split_hand1))
                    
                    while (split_sum1 >= 13 and split_sum1 <= 16) and 11 not in split_hand1 and dealer_hand[0] > 6:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand1.append(player_card)
                        split_sum1 = int(sum(split_hand1))
                        while split_sum1 > 21 and 11 in split_hand1:
                            split_hand1.remove(11)
                            split_hand1.append(1)
                            split_sum1 = int(sum(split_hand1))
                    
                    while (split_sum1 >= 13 and split_sum1 <= 17) and 11 in split_hand1:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand1.append(player_card)
                        split_sum1 = int(sum(split_hand1))
                        while split_sum1 > 21 and 11 in split_hand1:
                            split_hand1.remove(11)
                            split_hand1.append(1)
                            split_sum1 = int(sum(split_hand1))
                    
                    while split_sum1 == 18 and 11 in split_hand1 and dealer_hand[0] >= 9:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand1.append(player_card)
                        split_sum1 = int(sum(split_hand1))
                        while split_sum1 > 21 and 11 in split_hand1:
                            split_hand1.remove(11)
                            split_hand1.append(1)
                            split_sum1 = int(sum(split_hand1))

                    while split_sum2 <= 11:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand2.append(player_card)
                        split_sum2 = int(sum(split_hand2))
                        while split_sum2 > 21 and 11 in split_hand2:
                            split_hand2.remove(11)
                            split_hand2.append(1)
                            split_sum2 = int(sum(split_hand2))
                    
                    while split_sum2 == 12 and (dealer_hand[0] < 4 or dealer_hand[0] > 6):
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand2.append(player_card)
                        split_sum2 = int(sum(split_hand2))
                        while split_sum2 > 21 and 11 in split_hand2:
                            split_hand2.remove(11)
                            split_hand2.append(1)
                            split_sum2 = int(sum(split_hand2))
                    
                    while (split_sum2 >= 13 and split_sum2 <= 16) and 11 not in split_hand2 and dealer_hand[0] > 6:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand2.append(player_card)
                        split_sum2 = int(sum(split_hand2))
                        while split_sum2 > 21 and 11 in split_hand2:
                            split_hand2.remove(11)
                            split_hand2.append(1)
                            split_sum2 = int(sum(split_hand2))
                    
                    while (split_sum2 >= 13 and split_sum2 <= 17) and 11 in split_hand2:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand2.append(player_card)
                        split_sum2 = int(sum(split_hand2))
                        while split_sum2 > 21 and 11 in split_hand2:
                            split_hand2.remove(11)
                            split_hand2.append(1)
                            split_sum2 = int(sum(split_hand2))
                    
                    while split_sum2 == 18 and 11 in split_hand2 and dealer_hand[0] >= 9:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        split_hand2.append(player_card)
                        split_sum2 = int(sum(split_hand2))
                        while split_sum2 > 21 and 11 in split_hand2:
                            split_hand2.remove(11)
                            split_hand2.append(1)
                            split_sum2 = int(sum(split_hand2))
                    
                    if split_sum1 > 21 and split_sum2 > 21:
                        d_score += 2
                        purse -= wager*2
                        p_wins = False
                        print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Dealer wins!")
                        print(f"Purse: ${purse}")

                    elif split_sum1 <= 21 and split_sum2 <= 21:
                        #Dealer must hit at < 17
                        while dealer_sum < 17:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                                            
                            while dealer_sum >21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))
                                
                        #Dealer must hit at Soft 17
                        while dealer_sum == 17 and 11 in dealer_hand:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                        
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                    
                            while dealer_sum > 21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))
                        
                        #Compare sums if no BJ's and player doesn't bust.
                        if dealer_sum > 21:
                            p_score += 2
                            purse += wager*2
                            p_wins = True
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player wins!")
                            print(f"Purse: ${purse}")
                        elif split_sum1 == dealer_sum and split_sum2 == dealer_sum:
                            push += 2
                            p_wins = "push"
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Push!")
                            print(f"Purse: ${purse}")
                        elif split_sum1 > dealer_sum and split_sum1 > dealer_sum:
                            p_score += 2
                            purse += wager*2
                            p_wins = True
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player wins!")
                            print(f"Purse: ${purse}")
                        elif split_sum1 > dealer_sum:
                            p_score += 1
                            d_score += 1
                            p_wins = "push"
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player wins one and dealer wins one.")
                            print(f"Purse: ${purse}")
                        elif split_sum2 > dealer_sum:
                            p_score += 1
                            d_score += 1
                            p_wins = "push"
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player wins one and dealer wins one.")
                            print(f"Purse: ${purse}")
                        else:
                            d_score += 2
                            purse -= wager*2                            
                            p_wins = False
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Dealer wins!")
                            print(f"Purse: ${purse}")
                    
                    elif split_sum1 <= 21:
                        #Dealer must hit at < 17
                        while dealer_sum < 17:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                                            
                            while dealer_sum >21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))
                                
                        #Dealer must hit at Soft 17
                        while dealer_sum == 17 and 11 in dealer_hand:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                        
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                    
                            while dealer_sum > 21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))

                        #Compare sums if no BJ's and player doesn't bust with hand1.
                        if dealer_sum > 21:
                            p_score += 1
                            d_score += 1
                            p_wins = "push"
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player wins one and dealer wins one.")
                            print(f"Purse: ${purse}")
                        elif split_sum1 == dealer_sum:
                            push += 1
                            d_score += 1
                            p_wins = False
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player and dealer push one. Dealer wins one.")
                            print(f"Purse: ${purse}")
                        elif split_sum1 > dealer_sum:
                            p_score += 1
                            d_score += 1
                            p_wins = "push"
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player wins one and dealer wins one.")
                            print(f"Purse: ${purse}")
                        else:
                            d_score += 2
                            purse -= wager*2
                            p_wins = False
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Dealer wins!")
                            print(f"Purse: ${purse}")

                    elif split_sum2 <= 21:
                        #Dealer must hit at < 17
                        while dealer_sum < 17:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                                            
                            while dealer_sum >21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))
                                
                        #Dealer must hit at Soft 17
                        while dealer_sum == 17 and 11 in dealer_hand:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                        
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                    
                            while dealer_sum > 21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))
                        
                        #Compare sums if no BJ's and player doesn't bust with hand2.
                        if dealer_sum > 21:
                            p_score += 1
                            d_score += 1
                            p_wins = "push"
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player wins one and dealer wins one.")
                            print(f"Purse: ${purse}")
                        elif split_sum2 == dealer_sum:
                            push += 1
                            d_score += 1
                            p_wins = False
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player and dealer push one. Dealer wins one.")
                            print(f"Purse: ${purse}")
                        elif split_sum2 > dealer_sum:
                            p_score += 1
                            d_score += 1
                            p_wins = "push"
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Player wins one and dealer wins one.")
                            print(f"Purse: ${purse}")
                        else:
                            d_score += 2
                            purse -= wager*2
                            p_wins = False
                            print(f"Player splits and has {split_sum1} and {split_sum2}. Dealer has {dealer_sum}. Dealer wins!")

                #Player doubles down.
                elif (purse >= wager*2) and ((player_sum == 8 and (dealer_hand[0] == 5 or dealer_hand[0] == 6)) or (player_sum == 9 and (dealer_hand[0] >= 2 or dealer_hand[0] <= 6)) or (player_sum == 10 and (dealer_hand[0] >= 2 or dealer_hand[0] <= 9)) or (player_sum == 11 and (dealer_hand[0] >= 2 or dealer_hand[0] <= 11)) or (((player_sum >= 13 and player_sum <= 16) and 11 in player_hand) and (dealer_hand[0] >= 4 or dealer_hand[0] <= 6)) or ((player_sum == 17 and 11 in player_hand) and (dealer_hand[0] >= 2 or dealer_hand[0] <= 6)) or ((player_sum == 18 and 11 in player_hand) and (dealer_hand[0] >= 3 or dealer_hand[0] <= 6)) or ((player_sum == 19 and 11 in player_hand) and (dealer_hand[0] == 6))):                    
                    player_card = random.choice(game_deck)
                    game_deck.remove(player_card)
                    player_hand.append(player_card)
                    player_sum = int(sum(player_hand))
                    while player_sum > 21 and 11 in player_hand:
                            player_hand.remove(11)
                            player_hand.append(1)
                            player_sum = int(sum(player_hand))                    
                    
                    if player_sum > 21:
                            d_score += 1
                            purse -= wager*2
                            p_wins = False
                            print(f"Player doubles down. Player has {player_sum}, and dealer has {dealer_sum}. Dealer wins!")
                            print(f"Purse: ${purse}")
                    else:
                        #Dealer must hit at < 17
                        while dealer_sum < 17:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                                            
                            while dealer_sum >21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))
                                
                        #Dealer must hit at Soft 17
                        while dealer_sum == 17 and 11 in dealer_hand:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                        
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                    
                            while dealer_sum > 21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))

                    if dealer_sum > 21:
                        p_score += 1
                        purse += wager*2
                        p_wins = True
                        print(f"Player doubles down. Player has {player_sum}, and dealer has {dealer_sum}. Player wins!")
                        print(f"Purse: ${purse}")
                    elif player_sum == dealer_sum:
                        push += 1
                        p_wins = "push"
                        print(f"Player doubles down. Player has {player_sum}, and dealer has {dealer_sum}. Push!")
                        print(f"Purse: ${purse}")
                    elif player_sum > dealer_sum:
                        p_score += 1
                        purse += wager*2
                        p_wins = True
                        print(f"Player doubles down. Player has {player_sum}, and dealer has {dealer_sum}. Player wins!")
                        print(f"Purse: ${purse}")
                    else:
                        d_score += 1
                        purse -= wager*2
                        p_wins = False
                        print(f"Player doubles down. Player has {player_sum}, and dealer has {dealer_sum}. Dealer wins!")
                        print(f"Purse: ${purse}")    
                #Player doesn't split and doesn't double down.
                else:
                    
                    while player_sum <= 11:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        player_hand.append(player_card)
                        player_sum = int(sum(player_hand))
                        while player_sum > 21 and 11 in player_hand:
                            player_hand.remove(11)
                            player_hand.append(1)
                            player_sum = int(sum(player_hand))
                    
                    while player_sum == 12 and (dealer_hand[0] < 4 or dealer_hand[0] > 6):
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        player_hand.append(player_card)
                        player_sum = int(sum(player_hand))
                        while player_sum > 21 and 11 in player_hand:
                            player_hand.remove(11)
                            player_hand.append(1)
                            player_sum = int(sum(player_hand))
                    
                    while (player_sum >= 13 and player_sum <= 16) and 11 not in player_hand and dealer_hand[0] > 6:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        player_hand.append(player_card)
                        player_sum = int(sum(player_hand))
                        while player_sum > 21 and 11 in player_hand:
                            player_hand.remove(11)
                            player_hand.append(1)
                            player_sum = int(sum(player_hand))
                    
                    while (player_sum >= 13 and player_sum <= 17) and 11 in player_hand:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        player_hand.append(player_card)
                        player_sum = int(sum(player_hand))
                        while player_sum > 21 and 11 in player_hand:
                            player_hand.remove(11)
                            player_hand.append(1)
                            player_sum = int(sum(player_hand))
                    
                    while player_sum == 18 and 11 in player_hand and dealer_hand[0] >= 9:
                        player_card = random.choice(game_deck)
                        game_deck.remove(player_card)
                        player_hand.append(player_card)
                        player_sum = int(sum(player_hand))
                        while player_sum > 21 and 11 in player_hand:
                            player_hand.remove(11)
                            player_hand.append(1)
                            player_sum = int(sum(player_hand))
                    
                    if player_sum > 21:
                        d_score += 1
                        purse -= wager
                        p_wins = False
                        print(f"Player has {player_sum}, and dealer has {dealer_sum}. Dealer wins!")
                        print(f"Purse: ${purse}")
                    else:
                        #Dealer must hit at < 17
                        while dealer_sum < 17:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                                                            
                            while dealer_sum >21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))
                                
                        #Dealer must hit at Soft 17
                        while dealer_sum == 17 and 11 in dealer_hand:
                            while dealer_sum < 17:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                        
                            while dealer_sum == 17 and 11 in dealer_hand:
                                dealer_card = random.choice(game_deck)
                                game_deck.remove(dealer_card)
                                dealer_hand.append(dealer_card)
                                dealer_sum = int(sum(dealer_hand))
                    
                            while dealer_sum > 21 and 11 in dealer_hand:
                                dealer_hand.remove(11)
                                dealer_hand.append(1)
                                dealer_sum = int(sum(dealer_hand))

                        #Compare sums if no BJ's and player doesn't bust.
                        if dealer_sum > 21:
                            p_score += 1
                            purse += wager
                            p_wins = True
                            print(f"Player has {player_sum}, and dealer has {dealer_sum}. Player wins!")
                            print(f"Purse: ${purse}")
                        elif player_sum == dealer_sum:
                            push += 1
                            p_wins = "push"
                            print(f"Player has {player_sum}, and dealer has {dealer_sum}. Push!")
                            print(f"Purse: ${purse}")
                        elif player_sum > dealer_sum:
                            p_score += 1
                            purse += wager
                            p_wins = True
                            print(f"Player has {player_sum}, and dealer has {dealer_sum}. Player wins!")
                            print(f"Purse: ${purse}")
                        else:
                            d_score += 1
                            purse -= wager
                            p_wins = False
                            print(f"Player has {player_sum}, and dealer has {dealer_sum}. Dealer wins!")
                            print(f"Purse: ${purse}")


print("\nHere are the results:")
print(f"Sets played: {set_num}")
print(f"Total games played: {p_score + d_score + push}")
print(f"Player Wins: {p_score}")
print(f"Dealer Wins: {d_score}")
print(f"Push: {push}")
print(f"P/L: ${PandL}")