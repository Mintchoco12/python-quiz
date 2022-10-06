class Quiz:

    m_Questions = [
        'Vraag 1: Welk land heeft de meeste inwoners? ',
        'Vraag 2: Wat is het dichtstbevolkte land van Azië? ',
        'Vraag 3: Wat is de hoogste berg in Azië? ' ,
        'Vraag 4: Welke stad is de hoofdstad van Noord-Korea, officieel bekend als de Democratische Volksrepubliek Korea? ',
        'Vraag 5: Welke boom staat op de nationale vlag van Libanon? ',
        'Vraag 6: Sake, de traditionele wijn van Japan, wordt gemaakt door welk ingrediënt te vergisten? ',
        'Vraag 7: Welke dieren eten bamboe en komen alleen voor in bergbossen in China? ', 
        'Vraag 8: Wat is het totale aantal tijdzones in China? ',
        'Vraag 9: Welk Aziatisch land heeft de grootste moslimbevolking ter wereld? ',
        'Vraag 10: Welke valuta word gebruikt in Thailand? '
    ]

    m_Answers = [
        'china',
        'singapore',
        'mount everest',
        'pyongyang',
        'ceder',
        'rijst',
        'panda',
        '1',
        'indonesië',
        'thai baht'
    ]

    def __init__(self):
        self.m_Points = 0
        self.m_TotalQuestions = len(self.m_Questions)
        self._correct = 'Goed!'
        self._incorrect = 'Fout :('

    def startQuiz(self):
        playerInput=input('Ben je klaar om de Quiz te spelen? (ja/nee) : ')
        if playerInput.lower() == "ja":
            self.askQuestion(0)
        elif playerInput.lower()=='nee':
            print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
        else:
            print('Dit antwoord ken ik niet!')

    def askQuestion(self, index):
        playerInput=input(self.m_Questions[index])
        if playerInput.lower() == self.m_Answers[index]:
            self.m_Points += 1
            print(self._correct)
            self.nextQuestion(index)
        else:
            print(self._incorrect)
            self.nextQuestion(index)

    def nextQuestion(self, index):
        self._index = index
        if self._index < self.m_TotalQuestions - 1:
            self._index += 1
            self.askQuestion(self._index)
        else:
            self.endQuiz()

    def endQuiz(self):
        print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(self.m_Points)+' van de '+str(self.m_TotalQuestions)+' vragen juist beantwoord!')
        grade = round(float(10/self.m_TotalQuestions*self.m_Points), 1)
        print('Je cijfer voor project komt daarmee op een voorlopige '+str(grade)+'.')
        if self.m_Points >= 2: 
            print('Goed bezig!')
        else:           
            print('Hmmm, kan beter... nog even oefenen chef.\n\n')