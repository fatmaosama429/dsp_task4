
from math import ceil
from imagehash import hex_to_hash

import logging 
logging.basicConfig(filename="logging_similarity.py.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 

logger=logging.getLogger() 
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

logger.info("file similarity.py attached succesfully")

spect_hashes_differences  = []       
feature1_hashes_difference = []       
feature2_hashes_differences = []       
feature3_hashes_differences = []       
hash_differences_list =[spect_hashes_differences,feature1_hashes_difference,\
    feature2_hashes_differences,feature3_hashes_differences]
Similarity_indexes_list  = []        


       
def getHammingDistance(hash1: str, hash2: str, index : int) -> int:
    try:
        return hex_to_hash(hash1) - hex_to_hash(hash2)
    except:
        logger.info(str(index+3)+" is bad")
        return 255
    # return hex_to_hash(hash1) - hex_to_hash(hash2)

  
def similarity_indexes(list_of_songs: list,list_of_song_hashes: list):
    logger.info("similarity_indexes function is called")
    for i in range(len(list_of_songs)): #compare between my song and all songs in my data base 
        
        for j in range(len(hash_differences_list)): # getting the hash difference of all features between my song and the song of index i in my list 
            
            hash_differences_list[j].append(getHammingDistance(hash1=list_of_songs[i][j+1], hash2=list_of_song_hashes[j], index=i ))

            # hash_difference= hex_to_hash(list_of_songs[i][j+1]) - hex_to_hash(list_of_song_hashes[j]) # change the value of hash to hex to be compared easily 2^8 (1 byte)
            # hash_differences_list[j].append(hash_difference)
        sum=0
        for j in range(len(hash_differences_list)):
            sum =sum + hash_differences_list[j][i]

        avg_=sum/4
        scaled_averag = (1/255)* avg_ 
        similarity_ = (1 - scaled_averag) * 100

        Similarity_indexes_list.append(similarity_) # list of similarity index have the same index of he song
        logger.info("song of index "+str(i)+" is compared")
    logger.info("similarity function done successfully")
    return Similarity_indexes_list
 
# from math import ceil
# from imagehash import hex_to_hash

# hammingDifferences  = []       # List contains the hamming distance of spectrogram hashes of all the songs and the mix
# feature1Differences = []       # List contains the hamming distance of feature 1 hashes of all the songs and the mix
# feature2Differences = []       # List contains the hamming distance of feature 2 hashes of all the songs and the mix
# feature3Differences = []       # List contains the hamming distance of feature 3 hashes of all the songs and the mix
# differences_list =[hammingDifferences,feature1Differences,feature2Differences,feature3Differences]
# avgSimilaritiesAll  = []        # List contains the similarity percentage of all the songs and the mix (Using average hash of Spectrogram and all the features)

  
# def similarity_indexes(songs: list,feature_hash: list):
#     for i in range(len(songs)):
#         sum=0
#         for j in range(len(differences_list)):
#             print(songs[i][j+1])
#             differences_list[j].append(getHammingDistance(hash1=songs[i][j+1], hash2=feature_hash[j]))
        
#         for j in range(len(differences_list)):
#             sum =sum + differences_list[j][i]
#         avg=sum/4
#         avgMap = mapRanges(avg, 0, 255, 0, 1)  
#         result = (1 - avgMap) * 100
#         avgSimilaritiesAll.append(result) # list of similarity index have the same index of he song
#     print("averg similarity = ",avgSimilaritiesAll)
#     return avgSimilaritiesAll
        
# def getHammingDistance(hash1: str, hash2: str) -> int:
#     return hex_to_hash(hash1) - hex_to_hash(hash2)

# def mapRanges(inputValue: float, inMin: float, inMax: float, outMin: float, outMax: float):
#     slope = (outMax-outMin) / (inMax-inMin)
#     return outMin + slope*(inputValue-inMin)
