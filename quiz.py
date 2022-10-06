class Quiz:

    m_Questions = [
        'Vraag 1: Welke land heeft de grootste populatie in de wereld',
        'Vraag 2: Welke student staat bekend om zijn handigheid met shortcuts, extensions en andere webdeveloper-handigheden? ',
        'Vraag 3: Welke student heeft de meeste kennis van jQuery? ' 
    ]

    m_Answers = [
        'China',
        'julian',
        'nick'
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