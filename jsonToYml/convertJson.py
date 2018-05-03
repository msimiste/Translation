
import json
import yaml

def main(args):
    
    f = open('test1.json', 'r')
    jsonData = json.load(f)
    #print(jsonData)
    ff = open('output.yaml', 'w+')
    #yaml.dump(jsonData, ff, allow_unicode=True)
    #json.dump(jsonData, ff, ensure_ascii=False)
    yaml.dump(yaml.load(json.dumps(jsonData)), ff, default_flow_style=False, allow_unicode=True)
    f.close()

    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
