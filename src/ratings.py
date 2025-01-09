class Rating():
    def __init__(self, score, user_id):
        self.score = score
        self.user_id = user_id
    
    def update_score(self, new_score):
        self.score = new_score

    def __repr__(self):
        return f"Score: {self.score}, User: {self.user_id}"

class Ratings():
    def __init__(self):
        self.ratings = []
        
    def add_rating(self, rating):
        if rating not in self.ratings:
            self.ratings.append(rating)
    
    def get_scores_dict(self):
        scores_dict = {}
        for rating in self.ratings:
            if rating.score not in scores_dict:
                scores_dict[rating.score] = 0
            scores_dict[rating.score] += 1
        return scores_dict
    
    def remove_user_rating(self, user_id):
        self.scores = list(filter(lambda rating: rating.user_id != user_id, self.ratings))