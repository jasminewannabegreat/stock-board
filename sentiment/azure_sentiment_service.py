import httplib, urllib
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = '7d938264d905464f82b1b3e32c4c123b'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your access keys.
# For example, if you obtained your access keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial access keys are generated in the westcentralus region, so if you are using
# a free trial access key, you should not need to change this region.
uri = 'westus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (text):
    "Gets the sentiments for a set of documents and returns the information."
    documents = { 'documents': [
        { 'id': '1', 'text': text },
    ]}
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    result =  response.read ()
    score = json.loads(result)["documents"][0]['score']
    if score >= 0.7:
        return "Positive"
    elif score < 0.7 and score >=0.4:
        return "Netural"
    else:
        return "Negative"
    # print(json.loads(response.read()).keys())
    # return json.loads(response.read())["documents"][0]["score"]

if __name__ == "__main__":
    print 'Please wait a moment for the results to appear.\n'

    result = GetSentiment('Apple!')
    print(result)
    # print (json.dumps(json.loads(result), indent=4))