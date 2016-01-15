import numpy as np

class Article(object):
    """
    Article class.

    Attributes:
    id: unique integer ID
    features: numpy.array of article features
    M: matrix of user features in training set
    b: numpy.array of reward weighted user features
    """

    def __init__(self, id, features, user_dimension = 6, alpha = 0.1875):
        self.id = id
        self.features = np.array(features)
        self.M = np.eye(user_dimension)
        self.M_inv = self.M
        self.b = np.zeros(user_dimension)
        self.w = np.dot(self.M_inv, self.b)
        self.alpha = alpha

    def get_id(self):
        return self.id

    def get_features(self):
        return self.features

    def get_M(self):
        return self.M

    def get_M_inv(self):
        return self.M_inv

    def get_b(self):
        return self.b

    def get_w(self):
        return self.w

    def score(self, user_features):
        return np.dot(self.w, user_features)

    def score_ucb(self, user_features):
        return np.dot(self.w, user_features) + self.alpha * np.sqrt( np.dot(user_features, np.dot( self.M_inv, user_features ) ) )

    def update(self, user_features, reward):
        self.M += np.outer(user_features, user_features)
        self.M_inv = np.linalg.inv(self.M)
        self.b += reward * user_features
        self.w = np.dot(self.M_inv, self.b)

def set_articles(articles):
    global article_archive

    # iterate through articles
    for id in articles:
        # add this article to the dictionary
        features = articles[id]
        article_archive[id] = Article(id ,features)

def update(reward):
    if reward == -1:
        return
    # update last article
    global article_archive, last_article, last_user
    article_archive[last_article].update(last_user, reward)

def reccomend(time, user_features, articles):
    # turn user_features to numpy array
    user = np.array(user_features)
    
    # iterate through articles to keep the one
    # with highest UCB(upper confidence bound)
    best_id = None
    best_score = None

    global article_archive
    for id in articles:
        article = article_archive[id]

        # compute upper confidence bound
        score = article.score_ucb(user)

        # check if this is the best
        if best_score < score:
            best_id = id
            best_score = score

    # remember global variable of this article and user
    global last_article, last_user
    last_article = best_id
    last_user = user

    return best_id

# initialize global article dictionary
article_archive = {}
