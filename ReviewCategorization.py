import codecs

reviewsFile = codecs.open('movies.txt', encoding='utf-8', errors='ignore')
trainingSize = 10
checkNum = 10000 #number of lines to process before printing a status update

reviewCount = 0

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
        time = reviewsFile.readline()[13:-1]
        summary = reviewsFile.readline()[16:-1]
        text = reviewsFile.readline()[13:-1]
    
        reviewsFile.readline() #deals with line in between reviews
        #enter training code here
    except Exception as ex:
        print type(ex)
        print ex.args
        print ex
        while reviewsFile.readline() != "\n":
            pass
    finally:
        reviewCount += 1
        if reviewCount % checkNum == 0:
            print "Still here at review", reviewCount        


print "training done"

while True:
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
        time = reviewsFile.readline()[13:-1]
        summary = reviewsFile.readline()[16:-1]
        text = reviewsFile.readline()[13:-1]
    
        reviewsFile.readline() #deals with line in between reviews

        #enter clasification code here
        
    except Exception as ex:
        print type(ex)
        print ex.args
        print ex
        while reviewsFile.readline() != "\n":
            pass
    finally:
        reviewCount += 1
        if reviewCount % checkNum == 0:
            print "Still here at review", reviewCount


print "classification done"

reviewsFile.close()
