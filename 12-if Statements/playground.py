
# Mini voters program
age = int(input('Enter age: '))
Mani = 0
Kali = 0
Kryst = 0

if age >= 18:
    print('You are eligble to vote')

    print('Mani\nKali\nKryst')
    vote = input('Who do you want to vote: ')
    if vote == 'Mani':
        print('You voted for Mani!')
        Mani+=1
    elif vote == 'Kali':
        print('You voted for Kali!')
        Kali+=1
    else:
        print('You voted for Kryst!')
        Kryst+=1
    print('Thank you for your participation')
    print('Mani\'s Total Vote: ', Mani)
    print('Kali\'s Total Vote: ',Kali)
    print('Kryst\' Total Vote:: ',Kryst)
else:
    print('You are not eligble to vote')
