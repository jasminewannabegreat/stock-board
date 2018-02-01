import httplib, urllib, base64
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = '7d938264d905464f82b1b3e32c4c123b'

uri = 'westus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
    }
    try:
        conn = httplib.HTTPSConnection (uri)
        body = json.dumps(documents)
        conn.request ("POST", path, body, headers)
        response = conn.getresponse ()
        return response.read ()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': 'I really enjoy the new XBox One S. It has a clean look, it has 4K/HDR resolution and it is affordable.' },
    { 'id': '2', 'language': 'es', 'text': 'Este ha sido un dia terrible, llegué tarde al trabajo debido a un accidente automobilistico.' }
]}

print 'Please wait a moment for the results to appear.\n'

result = GetSentiment (documents)
print (json.dumps(json.loads(result), indent=4))