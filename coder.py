
print_C=[[" "for i in range(5)]for j in range(7)]
print_O=[[" "for i in range(5)]for j in range(7)]
print_D=[[" "for i in range(5)]for j in range(7)]
print_I=[[" "for i in range(5)]for j in range(7)]
print_N=[[" "for i in range(7)]for j in range(7)]
print_G=[[" "for i in range(6)]for j in range(7)]
print_X=[[" "for i in range(5)]for j in range(7)]


'''code to print X ie--> I'''
for r in range(7):
    for c in range(5):
        if c==2 or ((r==0 or r==6)and c!=2) :
            print_X[r][c]='*'

'''code to print X ie--> I'''
for i in range(7):
    for j in range(5):
        
        print(print_X[i][j],end=" ")
    print()
        
'''code for heart'''
for i in range(6):
    for j in range(7):
        if (i==0 and j%3!=0)or (i==1 and j%3==0 )or (i-j==2) or (i+j==8):
            print("*",end="")
        else:
            print(end=' ')
    print()
'''code for C'''
for r in range(7):
    for c in range(5):
        if (c==0) or ((r==0 or r==6) and (c>0))  :
            print_C[r][c]='*'
'''code for O'''
for r in range(7):
    for c in range(5):
        if ((c==0 or c==4)and (r!=0 and r!=6)) or (r==0 or r==6) and (c>0 and c<4):
            print_O[r][c]='*'
'''code for D'''
for r in range(7):
    for c in range(5):
        if (c==0) or (c==4 and (r!=0 and r!=6)) or ((r==0 or r==6) and (c>0 and c<4)):
            print_D[r][c]='*'
'''code for I'''
for r in range(7):
    for c in range(5):
        if c==2 or ((r==0 or r==6)and c!=2) :
            print_I[r][c]='*'
"""code for N"""
for r in range(7):
    for c in range(7):
        if (c==0 or c==6) or c==r:
            
            print_N[r][c]='*'
'''code for G'''
for r in range(7):
    for c in range(6):
        if c==0 or (c==4 and (r!=1 and r!=2)) or ((r==0 or r==6) and (c>0 and c<4)) or(r==3 and  (c==3 or c==5)):
            print_G[r][c]='*'
          
'''code for printing alphabets'''
for i in range(7):
    for j in range(5):
        print(print_C[i][j],end=" ")
    for j in range(5):
        print(print_O[i][j],end=" ")
    for j in range(5):
        print(print_D[i][j],end=" ")
    for j in range(5):
        print(print_I[i][j],end=" ")
    for j in range(7):
        print(print_N[i][j],end=" ")
    for j in range(6):
        print(print_G[i][j],end=" ")
    print()