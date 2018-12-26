print('''Hi. Welcome to MyMood, a personalized reccomendation service for all your troubles...
We work with ANY mood that you may be experiencing.
Let's begin.''')

x = input("What is your name?: ")
print("Thanks ", x)
print('''Now, let's talk about your mood. What best describes your current state?
(1) IN LOVE (KIKI, DO YOU LOVE ME?)
(2) A BIT HORNY (AND SEXUALLY FRUSTRATED)
(3) SAD AND LONELY (IT'S OK, IT HAPPENS)
(4) HAPPY AS A CLAM (YOU EARNED IT!)''')

import random

y = input("Input the corresponding number: ")
y_1 = int(y)
print("Thanks for sharing ", x)
if y_1 == 1:
    print('You chose In Love')
    love = ["Folk", "Easy Listening Christian rock", "Chill electronic beats"]
    print("You should be listening to", random.choice(love))
elif y_1 == 2:
    print('You chose A Bit Horny')
    horny = ["Funk", "Porn", "Your gf's last voice message"]
    print("You should be listening to", random.choice(horny))
elif y_1 == 3:
    print("You chose Sad and Lonely")
    sad = ["Nothing: just the sound of your tears", "Acoustic guitar", "90s Rap classics"]
    print("You should be listening to", random.choice(sad))
elif y_1 == 4:
    print("You chose Happy as a Clam")
    happy = ["Chill electronic beats", "Rock n' Roll", "PARTY MUSIC"]
    print("You should be listening to", random.choice(happy))
else:
    print("You didn't press the right button. Goodbye.")
    quit()
