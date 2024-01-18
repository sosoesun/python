from random import randint
import functools as f
def chuchom(select_numbers):
    one,two,three,four,five,cost,win=(0,0,0,0,0,0,0)
    while(1):
        numbers=[i+1 for i in range(45)]
        random_numbers=[numbers.pop(randint(0,44-i)) for i in range(6)]
        bonus=numbers.pop(randint(0,38))
        correct=[]
        bonus_numbers=False
        for i in range(6):
            temp=list(filter(lambda x:x == select_numbers[i],random_numbers))
            if temp!=[]:
                correct.append(temp[0])
            if select_numbers==bonus:
                bonus_numbers=True

        if len(correct)==3:
            five+=1
            win+=0.5
        if len(correct)==4:
            four+=1
            win+=5
        if len(correct)==5 and bonus_numbers==False:
            three+=1
            win+=500
        if len(correct)==5 and bonus_numbers==True:
            two+=5000
        if len(correct)==6:
            one+=250000
        #print(select_numbers,random_numbers,correct)
        cost+=0.1
        print("\r1등:{},2등:{},3등:{},4등:{},5등:{},총비용 {:0.0f}만원에 비해 당첨금 {:0.0f}만원...".format(one,two,three,four,five,cost,win), end=' ')
    
    

if __name__ == "__main__":
    select_numbers=list(map(int,input().split()))
    chuchom(select_numbers)
