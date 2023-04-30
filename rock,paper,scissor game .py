import random
print('welcome to the game:rock paper,scissor!!!')
print("""
winning rules are as follows:
1)rock vs paper-->paper wins
2)rock vs scissor-->rock wins
3)paper vs scissor-->scissor wins
""")
ls=['rock','paper','scissor']
comp_choice=random.choice(ls)

user_choice=input("choose:rock,paper or scissor!!")
dct={'rock':1,'paper':2,"scissor":3}
if user_choice=='rock'and comp_choice=="scissor":
    print("users wins")
elif user_choice=='scissor'and comp_choice=="rock":
    print("computer wins")

elif dct[comp_choice]==dct[user_choice]:
    print('draw!!')
elif dct[comp_choice]>dct[user_choice]:  
    print('computer wins')
elif dct[comp_choice]<dct[user_choice]:  
    print('user wins')


    
    
    
    
    
    
    


