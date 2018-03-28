import requests
import json
import re
import os

def chineseTranslate(url, target, inputArray,source,midOptions,inFile, key):
    
    
    url = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,target,midOptions,key)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url)
    data = response.json()
    
    temp = (data["outputs"][0]["output"]).replace(u'\uff0c',',')
    result = re.split('[\[,\]]',temp)
    source = re.split('[\[,\]]',data["outputs"][0]["source"])
    print(source)
    resultFile = open("chinese_translations.txt",'w')
    writeToFile(resultFile, source, result)
    
def japaneseTranslate(url, target, inputArray,source,midOptions,inFile, key):
    
    
    url = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,target,midOptions,key)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url)
    data = response.json()
    temp = (data["outputs"][0]["output"]).replace(u'\u300d\u3001\u300c',',')
    temp = temp.replace(u'\u300d\u300c',',')
    temp = temp.replace(u'\u300c','')
    temp = temp.replace(u'\u300d','')
    result = re.split('[\[,\]]',temp)
    source = re.split("[\[,\]]",data["outputs"][0]["source"])
    resultFile = open("japanese_translations.txt",'w')
    writeToFile(resultFile, source, result)



def writeToFile(resultFile, source, result):
    print("Result {}:{}".format(os.path.basename(resultFile.name),len(result)))
    print("Source {}:{}".format(os.path.basename(resultFile.name),len(source)))
    
    for x in range(1, len(result)-1):
        resultFile.write("{}:{}\n".format(source[x].encode("utf-8").strip(),result[x].encode("utf-8").strip()))
    resultFile.close()
    
def germanTranslate(url, target, inputArray,source,midOptions,inFile, key):
    
    url = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,target,midOptions,key)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url)
    data = response.json()
    result = re.split('[\[,\]]',data["outputs"][0]["output"])
    source = re.split("[\[,\]]",data["outputs"][0]["source"])
    resultFile = open("german_translations.txt",'w')
    writeToFile(resultFile, source, result)
    
def dutchTranslate(url, target, inputArray,source,midOptions,inFile, key):
    
    url = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,target,midOptions,key)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url)
    data = response.json()
    result = re.split('[\[,\]]',data["outputs"][0]["output"])
    source = re.split("[\[,\]]",data["outputs"][0]["source"])
    resultFile = open("dutch_translations.txt",'w')
    writeToFile(resultFile, source, result)
    
    
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
    #print(inputArray)
    chineseTranslate(url, targetChinese, inputArray, source, midOptions, inFile, key)
    #germanTranslate(url, targetGerman, inputArray,source,midOptions,inFile,key)
    #dutchTranslate(url, targetDutch, inputArray,source,midOptions,inFile,key)
    #japaneseTranslate(url, targetJapanese, inputArray,source,midOptions,inFile,key)

    #urlJapanese = "{}{}&{}&{}&{}&{}".format(url,inputArray,source,targetJapanese,midOptions,key)
    inFile.close()
    
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    #response = requests.get(urlJapanese)
    #data = response.json()
    #temp = (data["outputs"][0]["output"]).replace(u'\uff0c',',')
    #result = re.split('[[\[\,\]]',temp)
    #result = re.split("[u'\uff0c']",data["outputs"][0]["output"])
    #result = re.split('[[\[\,\]]',data["outputs"][0]["output"])
    #result = result[0].split(u'\uff0c')
    #result = re.compile("[\su'\uff0c']").split(data["outputs"][0]["output"])
    #result = (data["outputs"][0]["output"]).split(u'\uff0c')
    #source = re.split("[\[,\u'\uff0c'\]]",data["outputs"][0]["source"])
    #print("result {}".format(result))
    #print(len(result))
    #print("source {}".format(source))
    #print(len(source))
    #resultFile = open("japanese_translations.txt",'w')
    #
    #for x in range(1, len(result)-1):
    #    resultFile.write("{}:{}\n".format(source[x].encode("utf-8").strip(),result[x].encode("utf-8").strip()))
    #resultFile.close()
    
    
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
