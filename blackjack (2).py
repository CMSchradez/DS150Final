import random
import math
cards=[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
count=0
wins=0
losses=0
pushes=0
while True:
    while len(cards)>20:     
        #pick a card from the deck
        first_card=random.choice(cards)
        cards.remove(first_card)
        #if the first card is an 11 let the player choose if they want a 1 or an 11
        while first_card==11:
                    ace=input("do you want your ace to be a '1' or '11'")
                    if ace=="1":
                        first_card=1
                        break
                    elif ace=="11":
                        first_card=11
                        if count+11>21:
                            print("ace must be a 1")
                            first_card =1   
                        else:
                            break
                    else: 
                        print("please enter 1 or 11")
        print("first card:")
        print(first_card)
        count=first_card
        #pick another card from the deck
        second_card=random.choice(cards)
        cards.remove(second_card)
        #if the second card is an 11 let the player choose if they want a 1 or an 11
        while second_card==11:
                    ace=input("do you want your ace to be a '1' or '11'")
                    if ace=="1":
                        second_card=1
                        break
                    elif ace=="11":
                        second_card=11
                        if count+11>21:
                            print("ace must be a 1")
                            second_card =1   
                        else:
                            break
                    else: 
                        print("please enter 1 or 11")
        print("second card:")
        print(second_card)
        print("your total:")
        print(first_card+second_card)
        #Dealer draws a card
        dealer_first=random.choice(cards)
        cards.remove(dealer_first)
        print("dealer's first card:")
        print(dealer_first)
        #players card total
        count=first_card+second_card
        while count<21:
            #ask player hit or stand
            choice=input("hit(h) or stand(s)or quit(q)\n>")
            #when player hits
            if choice=="h":
                #draw a card and add it to total
                card=random.choice(cards)
                cards.remove(card)
                #let player chose what they want their 11 to be
                while card==11:
                    ace=input("do you want your ace to be a '1' or '11'")
                    if ace=="1":
                        card=1
                        break
                    elif ace=="11":
                        card=11
                        if count+11>21:
                            print("ace must be a 1")
                            card =1   
                        else:
                            break
                    else: 
                        print("please enter 1 or 11")    
                print(card)
                count=count+card
                print("total:")
                print(count)
            #when the player stands
            elif choice=="s":
                dealer_count=dealer_first
                #standard dealer logic(hit until 17 or higher)
                while dealer_count<17:
                    #draw a card and add it to dealer total
                    next_card=random.choice(cards)
                    cards.remove(next_card)
                    if next_card==11:
                        if dealer_count<=10:
                            next_card=11
                        else:
                            next_card=1
                    print("dealer's card:")
                    print(next_card)
                    dealer_count=dealer_count+next_card           
                print("dealer total:")
                print(dealer_count)
                #player wins if dealer goes over 21
                if dealer_count>21:
                    print("Dealer busted, you win!")
                    wins=wins+1
                #player wins if player total is larger than dealer total
                elif dealer_count<count:
                    print("you win!")
                    wins=wins+1
                #player loses if player total is smaller than dealer total
                elif dealer_count>count:
                    print("you lose!")
                    losses=losses+1
                #it is a tie if player total is equal to dealer total
                elif dealer_count==count:
                    print("push, no winner")
                    pushes=pushes+1
                break
            #if the player chooses quit the code stops
            elif choice=="q":
                exit()
            else:
                print("error, please enter h or s")
        #if player gets 21 it is blackjack and they win
        if count==21:
            print("Blackjack!")
            wins=wins+1
        #if player goes over 21 the bust and lose
        if count>21:
            print("you bust!")
            losses=losses+1
        #show wins and losses
        print("wins:")
        print(wins)
        print("losses:")
        print(losses)
        print("pushes:")
        print(pushes)
        #asks the player if the want to play again
        while True:
            play_again=input("do you want to play again? yes(y)or no(n)")
            if play_again=="y":
                print("next deal\ncards left:")
                print(len(cards))
                count=0
                break
            elif play_again=="n":
                exit()
            else:
                print("please enter y or n")
    cards=[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]