# Run dit bestand om te spelen :)

from database import QuestionData
from quiz import Quiz

m_Database = QuestionData()

m_Quiz = Quiz()

def main():

    if m_Quiz.m_Qa.m_TotalQuestions == m_Quiz.m_Qa.m_TotalAnswers:
        m_Quiz.askPlayerData()
    else:
        print("Er zijn een oneven vragen en antwoorden, vraag even aan de beheerder om het te corrigeren")

if __name__ == "__main__":
    main()