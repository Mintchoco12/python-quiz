import gspread

class Database:
    
    m_ServiceAccount = gspread.service_account(filename='credentials.json')
    m_Sheet = m_ServiceAccount.open_by_key('1_DSlea_fomaZ4M5_AW7oyw1f7Y5ryMoaAbqRy85zwLo')
    
    def __init__(self, sheet):
        self._worksheet = self.m_Sheet.get_worksheet(sheet)


class Player(Database):

    def __init__(self, sheet):
        super().__init__(sheet)