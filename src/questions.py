class Question():
    def __init__(self, question, user_id, likes=None, id=None):
        self.question = question
        self.user_id = user_id
        self.likes = []
        if likes:
            self.likes = likes
        self.id = None
    
    def like_question(self, user_id):
        if user_id != self.user_id and user_id not in self.likes:
            self.likes.append(user_id)
    
    def get_like_count(self):
        return len(self.likes)

    def to_tuple(self):
        return (self.question, self.user_id, self.likes)

    def __repr__(self):
        return f"Question: {self.question}, Likes: {self.likes}, ID: {self.id}, User: {self.user_id}"

class Questions():
    def __init__(self, questions=None, current_id=1):
        self.current_id = current_id
        self.questions = []
        if questions:
            self.questions = questions
    
    def add_question(self, question):
        if question not in self.questions:
            question.id = self.current_id
            self.current_id += 1
            self.questions.append(question)
            
    def remove_question(self, question_id):
        self.questions = list(filter(lambda q: q.id != question_id, self.questions))
    
    def get_questions_sorted(self):
        return sorted(self.questions, key=lambda q: q.get_like_count(), reverse=True)
    
    def like_question(self, id, user_id):
        for question in self.questions:
            if question.id == id:
                question.like_question(user_id)
                return

    def to_list(self):
        sorted_questions = self.get_questions_sorted()
        return list(map(lambda q: q.to_tuple(), sorted_questions))