from models.base import RecommendationAlgorithm

class CountBased(RecommendationAlgorithm):
    """
    CountBased is a simple recommendation algorithm that is based on
    simple counting feature {1-gram}
    """

    def train(self):
        raise NotImplemented
    
    def predict(self):
        raise NotImplemented
