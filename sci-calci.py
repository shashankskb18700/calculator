def calcu():
    count=1
    while count<2:
        '''you can do additon ,subtraction,multiplication,division,factorial findings'''
        import math
        #RunOrStop=input('run or stop')
        
        
        first_no=input('first no.=')
        second_no=input('second no.=')
        operator=input('what do you want add(+),subtract(-),multiply(*),divide(/),factorial,sin,cos,tan,log=')
        if first_no=='stop': #or second_no=='stop'or operator=='stop':
            break
        
        elif operator =='+':
            print(int(first_no)+int(second_no))
        elif operator=='-':
            print(int(first_no)-int(second_no))
        elif operator=='*':
            print(int(first_no)*int(second_no))
        elif operator=='/':
            print(int(first_no)/int(second_no))
        elif operator=='sin':
            print('first no. ={},second no.={}'.format(math.sin(int(first_no)),math.sin(int(second_no))))
        elif operator=='cos':
            print('first no. ={},second no.={}'.format(math.cos(int(first_no)),math.cos(int(second_no))))
        elif operator=='tan':
            print('first no. ={},second no.={}'.format(math.tan(int(first_no)),math.tan(int(second_no))))
        elif operator=='log':
            print('first no. ={},second no.={}'.format(math.log(int(first_no)),math.log(int(second_no))))
        elif operator=='factorial':
            which_no=input('which one first second or both sir')
            if which_no=='first':
                print('fatorial for {} is {}'.format(first_no,math.factorial(int(first_no))))
            elif which_no=='second':
                print('factorial for {} is {}'.format(second_no,math.factorial(int(second_no))))
            elif which_no=='both':
                print('factorial for {} is {},and {} is {}'.format(first_no,math.factorial(int(first_no),second_no,math.factorial(int(second_no)))))
        else:
            print('not valid operator')
            
        count+=1
