import gspread

class Database:

    def __init__(self):
        self.m_ServiceAccount = gspread.service_account(filename='credentials.json')
        self.m_Sheet = self.m_ServiceAccount.open_by_key('1_DSlea_fomaZ4M5_AW7oyw1f7Y5ryMoaAbqRy85zwLo')

class QuestionData(Database):

    def __init__(self):
        super().__init__()
        try:
            self.m_Worksheet = self.m_Sheet.worksheet('Q&A')
        except:
            self.m_Worksheet = self.m_Sheet.get_worksheet(0)
        self.m_TotalQuestions = self.m_Worksheet.acell('C2').value
        self.m_TotalAnswers = self.m_Worksheet.acell('D2').value

    def getQuestion(self, index):
        index += 2
        self.m_Question = self.m_Worksheet.acell(f'A{index}').value
        return self.m_Question

    def getAnswer(self, index):
        index += 2
        self.m_Answer = self.m_Worksheet.acell(f'B{index}').value
        return self.m_Answer

class PlayerData(Database):
    
    def __init__(self, name, age, points, grade, datetime):
        super().__init__()
        try:
            self.m_Worksheet = self.m_Sheet.worksheet('UserInfo')
        except:
            self.m_Worksheet = self.m_Sheet.get_worksheet(1)
        self.m_PlayerData = [name, age, points, grade, datetime]
        self.storeData(self.m_PlayerData)

    def storeData(self, data):
        self.m_Worksheet.append_row(data)

class GameData(Database):

    def __init__(self):
        super().__init__()
        try:
            self.m_Worksheet = self.m_Sheet.worksheet('Stats')
        except:
            self.m_Worksheet = self.m_Sheet.get_worksheet(2)

    def updateStats(self, index):
        _stat = int(self.m_Worksheet.acell(f'B{index}').value) + 1
        self.m_Worksheet.update(f'B{index}', _stat)