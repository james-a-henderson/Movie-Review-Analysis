import codecs
import time
from textblob.classifiers import NaiveBayesClassifier as nbc

reviewsFile = codecs.open('movies.txt', encoding='utf-8', errors='ignore')
trainingSize = 100
checkNum = 1000 #number of lines to process before printing a status update

reviewCount = 0

train = []
test = []
errorTraining = 0
errorClassification = 0
uselessTraining = 0
uselessClassification = 0
correct = 0
incorrect = 0

start = time.time()

print "Begining Training\n"
while(reviewCount < trainingSize):
    try:
        line = reviewsFile.readline()
        if not line:
            break;
        productId = line[19:-1]

    
        userId = reviewsFile.readline()[15:-1]
        profileName = reviewsFile.readline()[20:-1]
    
        temp = reviewsFile.readline()[20:-1].split("/")
        helpfulRatings = int(temp[0])
        totalRatings = int(temp[1])
    
        score = reviewsFile.readline()[14:-1]
        reviewTime = reviewsFile.readline()[13:-1]
        summary = reviewsFile.readline()[16:-1]
        text = reviewsFile.readline()[13:-1]
    
        reviewsFile.readline() #deals with line in between reviews

        #enter training code here

        if totalRatings == 0:
            uselessTraining += 1
            continue
        elif float(helpfulRatings) / totalRatings >= 0.5:
            train.append((summary, 'helpful'))
        else:
            train.append((summary, 'unhelpful'))
        
    except Exception as ex:
        print type(ex)
        print ex.args
        print ex
        errorTraining += 1
        while not (reviewsFile.readline() in ["\n", '\r\n']):
            pass
    finally:
        reviewCount += 1
        if reviewCount % checkNum == 0:
            print "Still here at review", reviewCount        

print "starting textblob training"
cl = nbc(train)
print "\nTraining Done"
print "\nBeginning Classification\n"

while reviewCount <= 10000:
    try:
        line = reviewsFile.readline()
        if not line:
            break;
        productId = line[19:-1]

    
        userId = reviewsFile.readline()[15:-1]
        profileName = reviewsFile.readline()[20:-1]
    
        temp = reviewsFile.readline()[20:-1].split("/")
        helpfulRatings = int(temp[0])
        totalRatings = int(temp[1])
    
        score = reviewsFile.readline()[14:-1]
        reviewTime = reviewsFile.readline()[13:-1]
        summary = reviewsFile.readline()[16:-1]
        text = reviewsFile.readline()[13:-1]
    
        reviewsFile.readline() #deals with line in between reviews

        #enter clasification code here
        if totalRatings == 0:
            uselessClassification += 1
            continue

        classification = cl.classify(summary)
        helpfulness = float(helpfulRatings) / totalRatings

        if classification == 'helpful':
            if helpfulness >= 0.5:
                correct += 1
            else:
                incorrect += 1
        else:
            if helpfulness >= 0.5:
                incorrect += 1
            else:
                correct += 1
        
    except Exception as ex:
        print type(ex)
        print ex.args
        print ex
        errorClassification += 1
        while not (reviewsFile.readline() in ["\n", '\r\n']):
            pass
    finally:
        reviewCount += 1
        if reviewCount % checkNum == 0:
            print "Still here at review", reviewCount


reviewCount -= 1 #deal with extra count that occurs
print "\nClassification Done\n"

end = time.time()

print reviewCount , "entries were processed, with", (errorTraining + errorClassification),"invalid entries and", (uselessTraining + uselessClassification), "useless entries"
print "Training Size:", trainingSize, ", minus", errorTraining,"invalid entries and", uselessTraining,"uselsess entries"
print "Classification Size:", (reviewCount - trainingSize), ", minus", errorClassification,"invalid entries and", uselessClassification,"uselsess entries"
print "Correct Classifications:", correct
print "Incorrect Classifications:", incorrect
print "Acuracy:", (float(correct) / (correct + incorrect)) * 100, "percent"
print "Elapsed Time:", (end - start)

reviewsFile.close()
