import urllib.request

###MAKE AN EBAY GETCATEGORIES API CALL AND STORE CATEGORIES IN XML FILE####

##This function reads data from .sh file. Headers are provided in the array 'headers'.
##Then, it stores categories in a xml file.

def create_xml ():   
    sh=open('get_categories.sh')
    data = sh.read()
    binary_data = data.encode(encoding='utf-8')

    headers = {} 
    headers["X-EBAY-API-CALL-NAME"] = ""
    headers["X-EBAY-API-APP-NAME"] = ""
    headers["X-EBAY-API-CERT-NAME"] = ""
    headers["X-EBAY-API-DEV-NAME"] = ""
    headers["X-EBAY-API-SITEID"] = ""
    headers["X-EBAY-API-COMPATIBILITY-LEVEL"] = ''

try:
    url = "https://api.sandbox.ebay.com/ws/api.dll"
    req = urllib.request.Request(url,binary_data, headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()   
    saveFile = open('categories_tree.xml','w')
    saveFile.write(str(respData.decode('utf-8')))
    saveFile.close()
except urllib.error.HTTPError as e:
    print("ERROR: ", e.read())


create_xml()
print ('XML file created!')
