import sys
import policy
import time as tm

if __name__ == "__main__":

    if (len(sys.argv) != 3):
        raise Exception("Usage: ./evaluator.py articles_file log_file")


    t = tm.time()

    with file(sys.argv[1]) as inf:
        articles = {}
        for line in inf:
            features = line.strip().split(" ")
            id = int(features[0])
            article = []
            article.extend(float(x) for x in features[1:])
            articles[id] = article
        policy.set_articles(articles)

    print "Time to read articles: %f" %(tm.time() - t)

    score = 0
    total_evaluated = 0
    n_lines = 0

    recommend_time = 0

    with file(sys.argv[2]) as inf:
        for line in inf:
            n_lines += 1
            logline = line.strip().split()
            chosen = int(logline.pop(7))
            reward = int(logline.pop(7))
            time = int(logline[0])
            user_features = [float(x) for x in logline[1:7]]
            articles = [int(x) for x in logline[7:]]

            t_rec = tm.time()
            calculated = policy.reccomend(time, user_features, articles)
            recommend_time += tm.time() - t_rec

            if calculated == chosen:
                policy.update(reward)
                score += reward
                total_evaluated += 1
            else:
                policy.update(-1)

        print "Time user for reccomendation: %f" %(recommend_time)
        print "Time to finish: %f" %(tm.time() - t)
        
        print "Evaluated %d/%d lines." % (total_evaluated, n_lines)
        print "CTR=%f" % (float(score) / total_evaluated)


