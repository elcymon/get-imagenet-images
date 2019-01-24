import wget
import os

def getImages(destFolder,urlTxt):
    
    if not os.path.exists(destFolder):
        os.makedirs(destFolder)
    with open(urlTxt, 'r') as f:
        data = f.read().strip().split('\n')
        for d in data:
            print(d)
            imgName = destFolder + d.split('/')[-1]
            try:
                wget.download(d,imgName)
            except:
                print('broken link')
                continue
            
if __name__ == "__main__":
    getImages('./images/','../imagenet.synset.txt')    