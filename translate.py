import requests
import json
import re
#from BeautifulSoup import *
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
   

def testTranslate():
    
    url = 'https://api-platform.systran.net/translation/text/translate'
    inputArray = '?input='
    source = 'source=en'
    targetChinese = 'target=zh-Hans'
    targetDutch = 'target=nl'
    targetGerman = 'target=de'
    targetJapanese = 'target=ja'       
    midOptions = 'withSource=true&withAnnotations=false&backTranslation=false&encoding=utf-8'
    key = 'key=c00a0b4f-e62e-432a-9e16-15c1ef2bab09'
    
    inFile = open("sourceIn.txt",'r')
    source1 = inFile.readlines()
    source1 = '[{}]'.format(','.join(source1).replace("\n",""))
    
    inputArray = inputArray + source1
    urlChinese = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,targetChinese,midOptions,key)
    #urlDutch = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,targetDutch,midOptions,key)
    urlGerman = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,targetGerman,midOptions,key)
    urlJapanese = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,targetJapanese,midOptions,key)
    inFile.close()
    #print(url.encode('utf=8'))
   
    #%5B%22hello%20world%22%2C%20%22goodbye%22%5D&source=en&target=de&withSource=true&withAnnotations=false&backTranslation=false&encoding=utf-8&key=c00a0b4f-e62e-432a-9e16-15c1ef2bab09'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(urlJapanese)
    data = response.json()
    
    #result = re.split("[u'\uff0c']",data["outputs"][0]["output"])
    #result = re.split("[\[,u'\uff0c'\]]",data["outputs"][0]["output"])
    result = re.compile("[\su'\uff0c']").split(data["outputs"][0]["output"])
    source = re.split("[\[,\]]",data["outputs"][0]["source"])
    #print("result {}".format(result))
    print(len(result))
    print("source {}".format(source))
    #print(len(source))
    resultFile = open("translations.txt",'w')
    
    for x in range(1, len(result)-1):
        resultFile.write("{}:{}\n".format(source[x].encode("utf-8").strip(),result[x].encode("utf-8").strip()))
    resultFile.close()
    
    
    ###**********************#
    #print(data[2].encode("ascii","ignore").strip())
    #outArray = data["outputs"][0]["output"].split("'")
    #sourceArray = data["outputs"][0]["source"]
    #temp = data["outputs"][0].json()
    #print temp
    #for x in range(0, len(outArray)):
    #    out = outArray[x].encode('ascii','ignore')
    #    src = sourceArray[x].encode('ascii','ignore')
    #    print("{}:{}".format(out,src))
        
    #print(data[1][0])
    #print(data['outputs']['output'])
    #data = response.json()
    #soup = BeautifulSoup(response.text)
    #j = json.loads(response.text)
    #print(response.text)
    #print(json.dumps(j))
    #print(response.outputs)
   

if __name__ == '__main__':
    testTranslate()
