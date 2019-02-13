##Elizabeth Koch
##Cs 461
##program 1
import random
import copy


'''creates a card which has a rank and a suit'''
class Card(object):
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit
        

    def __str__(self):
        if self.rank==14:
            return "{}{}".format('A',self.suit)
        elif self.rank==11:
            return "{}{}".format('J',self.suit)
        elif self.rank==12:
            return "{}{}".format('Q',self.suit)
        elif self.rank==13:
            return "{}{}".format('K',self.suit)
        else:
            return "{}{}".format(self.rank,self.suit)

'''creates a hand class that holds 5 cards'''
class Hand(object):
    def __init__(self, c1: Card, c2: Card, c3: Card, c4: Card, c5: Card):
        self.c1=c1
        self.c2=c2
        self.c3=c3
        self.c4=c4
        self.c5=c5
        self.high_card=0


    def __str__(self):
        return "{},{},{},{},{}".format(self.c1,self.c2,self.c3,self.c4,self.c5)

    '''returns a false if not straight, high card if straight'''
    def is_straight(self):
        r_lst=[self.c1.rank,self.c2.rank,self.c3.rank,self.c4.rank,self.c5.rank]
        r_lst.sort()
        if len(set(r_lst)) == len(r_lst):
            pass
        else:
            return False
        if r_lst[0]+1==r_lst[1] and r_lst[1]+1==r_lst[2] and \
        r_lst[2]+1==r_lst[3] and r_lst[3]+1==r_lst[4]:
            return r_lst[4]
        elif r_lst[4]==14 and r_lst[0]==2 and r_lst[0]+1==r_lst[1] and \
        r_lst[1]+1==r_lst[2] and r_lst[2]+1==r_lst[3]:
            return r_lst[3]
        else:
            return False

    '''returns false if not flush, high card if flush'''
    def is_flush(self):
        if(self.c1.suit==self.c2.suit and self.c2.suit==self.c3.suit \
                and self.c3.suit==self.c4.suit and self.c4.suit==self.c5.suit):
            r_lst=[self.c1.rank,self.c2.rank,self.c3.rank,self.c4.rank,self.c5.rank]
            r_lst.sort()
            return r_lst[4]
        
        return False

    '''returns false if not straight flush, high card if straight flush'''       
    def is_straight_flush(self):
        if (self.is_flush()!= False and self.is_straight()!=False):
            return self.is_flush()
        
        return False
            
    '''returns false if not full house, value of the 3 cards if full house'''
    def is_full_house(self):
        r_lst=[self.c1.rank,self.c2.rank,self.c3.rank,self.c4.rank,self.c5.rank]
        r_lst.sort()
        if len(set(r_lst)) == len(r_lst):
            return False
        if r_lst[0]==r_lst[1]:
            if r_lst[1]==r_lst[2] and r_lst[3]==r_lst[4]:
                return r_lst[2]
            if r_lst[2]==r_lst[3] and r_lst[3]==r_lst[4]:
                return r_lst[4]
            else:
                return False
        return False

    '''returns false if not 4 of a kind, rank of matching cards if true'''
    def is_four_of_a_kind(self):
        r_lst=[self.c1.rank,self.c2.rank,self.c3.rank,self.c4.rank,self.c5.rank]
        r_lst.sort()
        if len(set(r_lst)) == len(r_lst):
            return False
        if r_lst[0]==r_lst[1] and r_lst[1]==r_lst[2] and r_lst[2]==r_lst[3]:
            return r_lst[0]
        elif r_lst[1]==r_lst[2] and r_lst[2]==r_lst[3] and r_lst[3]==r_lst[4]:
            return r_lst[1]
        return False


    '''returns false if not 3 of a kind, value of matching cards if true'''    
    def is_three_of_a_kind(self):
        r_lst=[self.c1.rank,self.c2.rank,self.c3.rank,self.c4.rank,self.c5.rank]
        r_lst.sort()
        if len(set(r_lst)) == len(r_lst):
            return False
        if r_lst[0]==r_lst[1] and r_lst[1]==r_lst[2]:
            return r_lst[0]
        elif r_lst[1]==r_lst[2] and r_lst[2]==r_lst[3]:
            return r_lst[1]
        elif r_lst[2]==r_lst[3] and r_lst[3]==r_lst[4]:
            return r_lst[2]
        return False

    '''returns false if not 2 pair, rank of higher pair if true'''
    def is_two_pair(self):
        r_lst=[self.c1.rank,self.c2.rank,self.c3.rank,self.c4.rank,self.c5.rank]
        r_lst.sort()
        if len(set(r_lst)) == len(r_lst):
            return False
        if r_lst[0]==r_lst[1]:
            if r_lst[2]==r_lst[3]:
                return r_lst[2]
            if r_lst[3]==r_lst[4]:
                return r_lst[3]
        if r_lst[1]==r_lst[2]:
            if r_lst[3]==r_lst[4]:
                return r_lst[4]
        return False

    '''returns rank of pair, false if no pair'''
    def is_pair(self):
        r_lst=[self.c1.rank,self.c2.rank,self.c3.rank,self.c4.rank,self.c5.rank]
        r_lst.sort()
        if len(set(r_lst)) == len(r_lst):
            return False
        if r_lst[0]==r_lst[1]:
            return r_lst[0]
        elif r_lst[1]==r_lst[2]:
            return r_lst[1]
        elif r_lst[2]==r_lst[3]:
            return r_lst[2]
        elif r_lst[3]==r_lst[4]:
            return r_lst[3]

    '''returns the rank of the highest card'''
    def get_high_card(self):
        r_lst=[self.c1.rank,self.c2.rank,self.c3.rank,self.c4.rank,self.c5.rank]
        r_lst.sort()
        return r_lst[4]

    '''gives each hand a value from most valuable to least'''
    def evaluate_hand(self):
        if self.is_straight_flush()!=False:
            self.high_card=self.is_straight_flush()
            return (120+self.high_card)
        elif self.is_four_of_a_kind()!=False:
            self.high_card=self.is_four_of_a_kind()
            return (105+self.high_card)
        elif self.is_full_house()!=False:
            self.high_card=self.is_full_house()
            return (90+self.high_card)
        elif self.is_flush()!=False:
            self.high_card=self.is_flush()
            return (75+self.high_card)
        elif self.is_straight()!=False:
            self.high_card=self.is_straight()
            return (60+self.high_card)
        elif self.is_three_of_a_kind()!=False:
            self.high_card=self.is_three_of_a_kind()
            return (45+self.high_card)
        elif self.is_two_pair()!=False:
            self.high_card=self.is_two_pair()
            return (30+self.high_card)
        elif self.is_pair()!=False:
            self.high_card=self.is_pair()
            return (15+self.high_card)
        else:
            return self.get_high_card()
            
        
        

'''creates a deck of 52 cards '''
def create_deck():
    deck_lst=[]
    rank_lst=[2,3,4,5,6,7,8,9,10,11,12,13,14]
    suit_lst=['H','D','S','C']
    for rank in rank_lst:
        for suit in suit_lst:
            c=Card(rank,suit)
            deck_lst.append(c)
    return deck_lst

'''shuffles deck'''
def shuffle_deck(lst):
    x=int(0)
    i=int(0)
    temp=Card(0,0)
    while i<len(lst):
        x=random.randint(0,len(lst)-1)
        temp=lst[i]
        lst[i]=lst[x]
        lst[x]=temp
        i+=1
    return lst

'''goes through the community cards and compares
hands to find the best one'''
def find_best_hand(lst1,lst2):
    value=int(0)
    x=int(0)
    y=int(1)
    while x<4:
        while y<5:
            h=Hand(lst1[0],lst1[1],lst1[2],lst2[x], \
                   lst2[y])
            if h.evaluate_hand()>value:
                value=h.evaluate_hand()
                best_hand=h
            y+=1
        x+=1
        y=x+1
    
    return value


main_counter=int(0)
z =int(20)
loop_number=int(0)
while main_counter<3:
##3 main loops each of 500 iterations
    outer_counter=int(0)
    ##variables to keep track of number of wins
    ##for random and best ai hands
    my_wins=int(0)
    my_wins2=int(0)
    
    while outer_counter<500:
        deck=create_deck()
        deck=shuffle_deck(deck)
        my_cards=[]
        ai1_cards=[]
        ai2_cards=[]
        ai3_cards=[]
        ai4_cards=[]
        table_cards=[]

        counter=int(0)
        while counter<3:
            ##deals 3 cards, these don't change each time
            my_cards.append(deck.pop(0))
            counter+=1

        counter=0
        while counter<5:
            table_cards.append(deck.pop(0))
            counter+=1

        
        my_score=int(find_best_hand(my_cards,table_cards))
        inner_counter=int(0)
        if loop_number==1:
            z=100
        elif loop_number==2:
            z=200
        while inner_counter<z:
            temp_deck=copy.copy(deck)
            ##copy the deck so the remaining cards can be dealt to ai
            temp_deck=shuffle_deck(temp_deck)
            counter=0
            while counter<3:
                ##deal ai cards
                ai1_cards.append(temp_deck.pop(0))
                ai2_cards.append(temp_deck.pop(0))
                ai3_cards.append(temp_deck.pop(0))
                ai4_cards.append(temp_deck.pop(0))
                counter+=1
            counter=0
            while counter<4:
                ##make random ai hands with table cards
                x=int(random.randint(0,4))
                y=int(random.randint(0,4))
                while x==y:
                    y=int(random.randint(0,4))
                if counter==0:
                    h=Hand(ai1_cards[0],ai1_cards[1],ai1_cards[2],table_cards[x],table_cards[y])
                    ai1_score=int(h.evaluate_hand())
                elif counter==1:
                    h=Hand(ai2_cards[0],ai2_cards[1],ai2_cards[2],table_cards[x],table_cards[y])
                    ai2_score=int(h.evaluate_hand())
                if counter==2:
                    h=Hand(ai3_cards[0],ai3_cards[1],ai3_cards[2],table_cards[x],table_cards[y])
                    ai3_score=int(h.evaluate_hand())
                if counter==0:
                    h=Hand(ai4_cards[0],ai4_cards[1],ai4_cards[2],table_cards[x],table_cards[y])
                    ai4_score=int(h.evaluate_hand())
                counter+=1


            score_lst=[my_score,ai1_score,ai2_score,ai3_score,ai4_score]
            score_lst.sort()
            if my_score==score_lst[4]:
                ##if its a tie, only half a win
                if score_lst[4]==score_lst[3]:
                    my_wins+=0.5
                else:
                    my_wins+=1



            ##now for the ai selecting best hands
            ai1_best_score=int(find_best_hand(ai1_cards,table_cards))
            ai2_best_score=int(find_best_hand(ai2_cards,table_cards))
            ai3_best_score=int(find_best_hand(ai3_cards,table_cards))
            ai4_best_score=int(find_best_hand(ai4_cards,table_cards))
            score_lst2=[my_score,ai1_best_score,ai2_best_score, \
                        ai3_best_score,ai4_best_score]
            score_lst2.sort()
            if my_score==score_lst2[4]:
                ##if its a tie, only half a win
                if score_lst2[4]==score_lst2[3]:
                    my_wins2+=0.5
                else:
                    my_wins2+=1
            inner_counter+=1
        outer_counter+=1
    ##print results
    if loop_number==0:
        print("Win % for 10,000 hands w/ random ai hands: ",(my_wins/100),"%" )
        print("Win % for 10,000 hands w/ best ai hands: ",(my_wins2/100),"%")
    elif loop_number==1:
        print("Win % for 50,000 hands w/ random ai hands: ", (my_wins/500),"%" )
        print("Win % for 50,000 hands w/ best ai hands: ",(my_wins2/500),"%")
    elif loop_number==2:
        print("Win % for 100,000 hands w/ random ai hands: ", (my_wins/1000),"%" )
        print("Win % for 100,000 hands w/ best ai hands: ",(my_wins2/1000),"%")
    loop_number+=1
    main_counter+=1
























