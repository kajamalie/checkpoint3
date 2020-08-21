#The company SuperSale3000 want to rank its sales team at the end of every week. 
#Each call gives the seller 10 points, each meeting 30 points and each sale 100 points.
# There is also a 100-point bonus for each, if you make more than 150 calls, or 20 meetings or 5 sales.
#Create a new file called “question_3.py”.
#They already have the data for each employee saved in a dictionary.
#At the top of the file set the following example dictionary for Jodan Belfort:
#Jordan_belfort = {‘calls’: 178, ‘meetings’:17,  ‘sales’:6}
#Add the following logic to calculate the total score from the dictionary and add it to the same dictionary 
#using the key ‘score’

Jordan_belfort = {'calls': 178, 'meetings':17,  'sales':6}
kaja_end = {'calls': 140, 'meetings':22,  'sales': 9}


def rank_sale(dic):
    bonus = {'points': 0}
    for calls in dic:
        bonus['points'] = + dic['calls'] * 10
        if dic['calls'] > 150:
            bonus['points'] = (bonus['points']) + 100
        else:
            pass
        for meetings in dic:
            bonus['points'] = (bonus['points']) + dic['meetings'] * 30
            if dic['meetings'] > 20:
                bonus['points'] = (bonus['points']) + 100
            else:
                pass
            for sales in dic:
                bonus['points'] = (bonus['points']) + dic['sales'] * 100
                if dic['sales'] > 5:
                    bonus['points'] = (bonus['points']) + 100
    
                    
            
    print(bonus) 
    
    
#%%
    
   #levert etter checkpoint var ferdig!!  
# Ny verson som inkluderer rank i samme dictionary 
    
Jordan_belfort = {'calls': 178, 'meetings':17,  'sales':6}
kaja_end = {'calls': 140, 'meetings':22,  'sales': 9}


def rank_sale(dic):
    dic['rank'] = 0
    for calls in dic:
        dic['rank'] = + dic['calls'] * 10
        if dic['calls'] > 150:
            dic['rank'] = (dic['rank']) + 100
        else:
            pass
        for meetings in dic:
            dic['rank'] = (dic['rank']) + dic['meetings'] * 30
            if dic['meetings'] > 20:
                dic['rank'] = (dic['rank']) + 100
            else:
                pass
            for sales in dic:
                dic['rank'] = (dic['rank']) + dic['sales'] * 100
                if dic['sales'] > 5:
                    dic['rank'] = (dic['rank']) + 100
                else:
                    pass
    
                    
            
    print(dic) 
    print(dic['rank'])
  