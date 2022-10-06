punten=0
aantal_vragen=10

print('\n\n\nWelkom bij de gigantische Webdevelopers Quiz 2022')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')

if antwoord.lower()=='ja':
    antwoord=input('Vraag 1: Welke student heeft in het eerste leerjaar wel eens een raycaster geprogrammeerd? ')
    if antwoord.lower()=='tygo' or antwoord.lower()=='tycho':
        punten += 1
        print('goed!')
    else:
        print('fout!')

    antwoord=input('Vraag 2: Welke student staat bekend om zijn handigheid met shortcuts, extensions en andere webdeveloper-handigheden? ')
    if antwoord.lower()=='julian':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 3: Welke student heeft de meeste kennis van jQuery? ')
    if antwoord.lower()=='nick':
        punten += 1
        print('goed')
    else:
        print('fout')

    print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 2: print('Goed bezig!')
    else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')


elif antwoord.lower()=='nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')
    
print('\n\nMooi. Dan gaat de gigantische Webdevelopers Quiz 2022 beginnen!!\nGeef bij iedere vraag als antwoord de voornaam van een student uit de klas op.\n\n')