import json


def points():
    with open('Game/recorde.json','r') as file:
        return json.loads(file.read())
    

def registro(score):
    dic = points()
    dic['score_atual'] = score
    dic['recorde'].append(score)
    dic['recorde'].sort()
    if len(dic['recorde']) == 6:
        del(dic['recorde'][0])

    with open('Game/recorde.json',"w") as file:
        json.dump(dic,file)

    