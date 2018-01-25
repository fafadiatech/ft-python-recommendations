"""
collaborative module consists of Collaborative Filtering model for generating
recommendations
"""

from models.base import RecommendationAlgorithm

class ItemToItemAlgorithm(RecommendationAlgorithm):
    """
    ItemToItemAlgorithm is implementation of algorithm
    more details can be found on following URL

    https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf
    """
    def __init__(self):
        pass
    
    def train(self, dataset, min_sim_score=0.30, top_n=10, metric="jaccard"):
        """
        train method is used to build item similarity table, this in turn
        is used to generate recommendations given an item id
        """
        # The algorithms would be as follows
        # 1. Generate inverted index of {item: [user_id..]}
        # 2. Compute similarity between item_1 and item_2
        #    and store in similarity
        pass

    def predict(self, user_id):
        """
        predict method is used to get a sorted list of
        recommendations
        """
        results = []
        return results 