#Quiz Game
print("Welcome Here is a simple quiz for you")
print("Chaliye Shuru Krte hai")

totalQuestions = 4
Score = 0

ans = input('1. What is my name?')
if ans.lower() =='saksham':
    print('Correct')
    Score +=1
else:
    print('Incorrect')

ans = input('2. What is my favourite sports?')
if ans.lower() == 'cricket':
    print('Correct')
    Score+=1
else:
    print('Incorrect')

ans = input('3. What is my age?')
if ans == '21':
    print('Correct')
    Score+=1
else:
    print('Incorrect')

ans =  input('4. What is my Profession?')
if ans.lower()=='web developer':
    print('Correct')
    Score+=1
else:
    print('Incorrect')


print('Thank You for playing, You Got' + str(Score) + 'Questions Correct')
percent = (Score/totalQuestions)*100
print("Mark: "+  str(int(percent))+ '%')

if percent>=50:
    print('You Are passed')
else:
    print('Better luck next time')


