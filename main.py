# Run het bestand om te spelen :)

from quiz import Quiz
from database import Database
m_Database = Database(0)
m_Database.getTotalQuestions()

#m_Quiz = Quiz()

# def main():
#     if len(m_Quiz.m_Questions) == len(m_Quiz.m_Answers):
#         m_Quiz.startQuiz()
#     else:
#         print("Er zijn een oneven vragen en antwoorden, vraag even aan de beheerder om het te corrigeren")

# if __name__ == "__main__":
#     main()