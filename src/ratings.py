class Rating():
    def __init__(self, score, user_id):
        self.score = score
        self.user_id = user_id
    
    def update_score(self, new_score):
        self.score = new_score
    
    def to_tuple(self):
        return (self.score, self.user_id)

    def __repr__(self):
        return f"Score: {self.score}, User: {self.user_id}"

class Ratings():
    def __init__(self, ratings=None):
        self.ratings = []
        if ratings:
            self.ratings = ratings
        
    def add_rating(self, rating):
        if rating not in self.ratings:
            self.ratings.append(rating)
    
    def get_sorted_scores(self):
        scores_dict = {}
        for rating in self.ratings:
            if rating.score not in scores_dict:
                scores_dict[rating.score] = 0
            scores_dict[rating.score] += 1
        sorted_scores_list = []
        for i in range(1, 6):
            if i in scores_dict:
                sorted_scores_list.append(scores_dict[i])
            else:
                sorted_scores_list.append(0)
        return sorted_scores_list
    
    def remove_user_rating(self, user_id):
        self.ratings = list(filter(lambda rating: rating.user_id != user_id, self.ratings))
    
    def to_list(self):
        return list(map(lambda r: r.to_tuple(), self.ratings))