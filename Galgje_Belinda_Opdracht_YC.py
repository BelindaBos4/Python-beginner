spelerGalgje = input('Vul hier je naam in:')
print('Welkom bij het spelletje galgje,'+ ' ' + spelerGalgje +'!')

import random

woorden_lijst = ['huis','duikboot','taart','circus','kluis','nintendo']
random.shuffle(woorden_lijst)

antwoord = list(woorden_lijst[0])

display = []
lettersGeraden = {}

display.extend(antwoord)
for letter in range (len(display)):
    display[letter] = '_'

print (' '.join(display))
print()

correctCount = 0
errorCount = 0
maxErrorCount = 11

while correctCount < len(antwoord) and errorCount < maxErrorCount:
    beurtCorrect = False
    raadLetter = input("Raad een letter:")
    raadLetter = raadLetter.lower()
    print(correctCount + errorCount)
    
    if raadLetter in lettersGeraden:
        print("Oops, al geraden!!! Reeds geraden letters: ")
        for geradenLetter, geradenValue in lettersGeraden.items():
            print(geradenLetter)
        continue

    for letter in range(len(antwoord)):
        if antwoord [letter] == raadLetter :
            display[letter] = raadLetter 
            print('Goed geraden!')
            correctCount = correctCount+1
            beurtCorrect = True
    
    if not beurtCorrect:
        errorCount = errorCount + 1
            
    lettersGeraden[raadLetter] = True

    print (" ".join(display))
    print()

if errorCount < maxErrorCount and correctCount == len(antwoord): 
    print("Goed gedaan" + ' ' + spelerGalgje + ', je hebt het woord geraden!')
else : 
    print("GAME OVER" + ' ' + spelerGalgje)
