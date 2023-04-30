import random
win_number=random.randint(1,100)

user_choice=int(input('enter number between 1-100: '))

No_of_guess=1
end_game=True
while end_game:
    if win_number==user_choice:
        print('HURRAH!! YOU WIN')
        
        print(f'you guessed the no in {No_of_guess}')
        end_game=False
    else:
        if user_choice<win_number:
            print('too low')
            No_of_guess+=1
            user_choice=int(input('enter number again: '))
        else:
            print('too high')
            No_of_guess+=1
            user_choice=int(input('enter number again: '))
            
        

            

                
            
            
