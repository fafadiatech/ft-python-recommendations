# recommendations

The motivation of this project is to build a recommendation engine that is Easy to use. This python package has been implemented using **Python 3.6**

## Key Packages

1. `config`: Contains all files related to settings of the project
1. `dataset`: Contains code that will help download and pre-process datasets
1. `models`: Contains code that allow us to define our recommendation algorithm
1. `transforms`: Contains code that allow us to perform various transformations on dataset. E.g. Stopword removal

## Installlation

1. Create virutal environment `virtualenv recommenendations -p /usr/local/bin/python3.6` {Note: You may want to change path to your Python 3.6 binary}
2. Clone this repository
3. Install dependencies `pip install -r requirements`

## Sample Useage

```python
from models.content import CountBased
from datasets.content import NewsDataset

# Sample only first 200 records
dataset = NewsDataset(200)

# Create a recommendation engine, train it with our data
recommender = CountBased()
recommender.train(dataset.get_instances())
print("Total dimensions of features:", len(recommender.transform.vocabulary))

# Get recommendation for Document with ID 182
recommender.predict(182)
```
## Collection of Recommendation Algorithms implemented in Python.

1. [Collaborative Filtering](https://en.wikipedia.org/wiki/Collaborative_filtering)
2. Content Based
3. Graph Based

The code that has been written has been based off on the [MoveLens dataset](http://grouplens.org/datasets/movielens/). Few resources that we've used for building this include [Collaborative Filtering Recommendation System](http://files.grouplens.org/papers/FnT%20CF%20Recsys%20Survey.pdf) and [Programming Collective Intelligence](http://shop.oreilly.com/product/9780596529321.do)
