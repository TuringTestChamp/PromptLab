# database_handling.py code:

import sqlite3

class FinalDatabase:
    def __init__(self, db_name=":memory:"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback_history (
                id INTEGER PRIMARY KEY,
                iteration INTEGER NOT NULL,
                feedback TEXT NOT NULL,
                selected_prompt TEXT NOT NULL,
                added TEXT,
                removed TEXT,
                retained TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS prompt_versions (
                id INTEGER PRIMARY KEY,
                iteration INTEGER NOT NULL,
                prompt TEXT NOT NULL
            )
        ''')

    def store_feedback(self, iteration, feedback, selected_prompt):
        self.cursor.execute("INSERT INTO feedback_history (iteration, feedback, selected_prompt) VALUES (?, ?, ?)", 
                            (iteration, feedback, selected_prompt))
        self.conn.commit()

    def store_detailed_feedback(self, iteration, feedback, selected_prompt, added, removed, retained):
        self.cursor.execute(
            "INSERT INTO feedback_history (iteration, feedback, selected_prompt, added, removed, retained) VALUES (?, ?, ?, ?, ?, ?)", 
            (iteration, feedback, selected_prompt, added, removed, retained))
        self.conn.commit()

    def retrieve_word_scores(self):
        self.cursor.execute("SELECT added, removed, retained FROM feedback_history")
        data = self.cursor.fetchall()
        
        word_scores = {}
        for added, removed, retained in data:
            for word in added.split(','):
                word_scores[word] = word_scores.get(word, 0) + 1
            for word in removed.split(','):
                word_scores[word] = word_scores.get(word, 0) - 1
            # Retained words can also have their scores modified if needed
        
        return word_scores

