import requests
def uploadImage(url, token, payload):
    '''
    url : IoT.own Server Address
    token : IoT.own API Token
    payload : Image + Annotation Json Data (check format in README.md)
    '''
    apiaddr = url + "/api/v1.0/nn/image"
    header = {'Content-Type': 'application/json', 'Token': token}
    r = requests.post(apiaddr, data=payload, headers=header)
    if r.status_code == 200:
        return True
    else:
        print(r)
        return False
        
def downloadAnnotations(url, token, classname):
    ''' 
    url : IoT.own Server Address
    token : IoT.own API Token
    classname : Image Class ex) car, person, airplain
    '''
    apiaddr = url + "/api/v1.0/nn/images?labels=" + classname
    header = {'Accept':'application/json', 'token':token}
    r = requests.get(apiaddr, headers=header)
    if r.status_code == 200:
        return r.json()
    else:
        print(r)
        return None

def downloadImage(url, token, imageID):
    ''' 
    url : IoT.own Server Address
    token : IoT.own API Token
    imageID : IoT.own imageID ( using annotation's 'id' not '_id' ) 
    '''
    apiaddr = url + "/nn/dataset/img/" + imageID
    header = {'Accept':'application/json', 'token':token}
    r = requests.get(apiaddr, headers=header)
    if r.status_code == 200:
        return r.content
    else:
        print(r)
        return None
