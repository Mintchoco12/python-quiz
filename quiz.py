import json
from datetime import datetime
from database import PlayerData, QuestionData, GameData

class Quiz:

    m_Qa = QuestionData()
    m_Stats = GameData()

    m_Correct = 'Goed!'
    m_Incorrect = 'Fout :('

    def __init__(self):
        self.m_Points = 0
        self.m_TotalQuestions = int(self.m_Qa.m_TotalQuestions)
        
    def askPlayerData(self):
        self._name = input('Voer uw naam in: ')
        self._age = input('Voer uw leeftijd in: ')
        if self._age.isnumeric():         
            self.startQuiz()
        else:
            print('Graag alleen cijfers gebruiken. ')
            self.askPlayerData()

    def startQuiz(self):
        _playerInput=input('Ben je klaar om de Quiz te spelen? (ja/nee) : ')
        if _playerInput.lower() == "ja":
            self.m_Stats.updateStats(1)
            self.askQuestion(0)
        elif _playerInput.lower()=='nee':
            print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
        else:
            print('Dit antwoord ken ik niet!')

    def askQuestion(self, index):
        _playerInput=input(self.m_Qa.getQuestion(index))
        if _playerInput.lower() == self.m_Qa.getAnswer(index):
            self.m_Points += 1
            self.m_Stats.updateStats(3)
            print(self.m_Correct)
            self.nextQuestion(index)
        else:
            self.m_Stats.updateStats(4)
            print(self.m_Incorrect)
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
        self._grade = round(float(10/self.m_TotalQuestions*self.m_Points), 1)
        print('Je cijfer voor project komt daarmee op een voorlopige '+str(self._grade)+'.')
        self.sendData()
        if self.m_Points >= 2: 
            print('Goed bezig!')
        else:           
            print('Hmmm, kan beter... nog even oefenen chef.\n\n')
        self.m_Stats.updateStats(2)

    def sendData(self):
        _now = datetime.now()
        _currentDateTime = json.dumps(_now, default=str)
        PlayerData(self._name, self._age, self.m_Points, self._grade, _currentDateTime)