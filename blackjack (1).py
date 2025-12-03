import random
import math
cards=[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
count=0
wins=0
losses=0
pushes=0
while True:
    while len(cards)>20:     
        first_card=random.choice(cards)
        cards.remove(first_card)
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
        second_card=random.choice(cards)
        cards.remove(second_card)
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
        dealer_first=random.choice(cards)
        cards.remove(dealer_first)
        print("dealer's first card:")
        print(dealer_first)
        count=first_card+second_card
        while count<21:
            choice=input("hit(h) or stand(s)or quit(q)\n>")
            if choice=="h":
                card=random.choice(cards)
                cards.remove(card)
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
            elif choice=="s":
                dealer_count=dealer_first
                while dealer_count<17:
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
                if dealer_count>21:
                    print("Dealer busted, you win!")
                    wins=wins+1
                elif dealer_count<count:
                    print("you win!")
                    wins=wins+1
                elif dealer_count>count:
                    print("you lose!")
                    losses=losses+1
                elif dealer_count==count:
                    print("push, no winner")
                    pushes=pushes+1
                break
            elif choice=="q":
                exit()
            else:
                print("error, please enter h or s")
        if count==21:
            print("Blackjack!")
            wins=wins+1
        if count>21:
            print("you bust!")
            losses=losses+1
        print("wins:")
        print(wins)
        print("losses:")
        print(losses)
        print("pushes:")
        print(pushes)
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


