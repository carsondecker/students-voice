class Question():
    def __init__(self, question, user_id):
        self.question = question
        self.user_id = user_id
        self.likes = []
    
    def like_question(self, user_id):
        if user_id != self.user_id and user_id not in self.likes:
            self.likes.append(user_id)
    
    def get_like_count(self):
        return len(self.likes)

    def __repr__(self):
        return f"Question: {self.question}, Likes: {self.likes}, User: {self.user_id}"

class Questions():
    def __init__(self):
        self.questions = []
    
    def add_question(self, question):
        if question not in self.questions:
            self.questions.append(question)
            
    def remove_question(self, question):
        self.questions.remove(question)
    
    def get_questions_sorted(self):
        return sorted(self.questions, key=lambda q: q.get_like_count(), reverse=True)