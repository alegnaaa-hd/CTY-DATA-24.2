from urllib.request import urlopen
import json

startDate = "2024-01-01"
endDate = "2024-07-19"
format = "json"
base_url = "https://www.treasurydirect.gov/TA_WS/securities/auctioned"
def get_treasury_securities(startDate="2024-01-01",endDate="2024-07-19"):

    url = f"{base_url}?format={format}&startDate={startDate}&endDate={endDate}"

    with urlopen(url) as server_response:
        server_gibberish_data = server_response.read()
        server_encoding = server_response.info().get_content_charset('utf-8')
        # This is an array of securities auctioned formatted
        # in json
        jsonlist = json.loads(server_gibberish_data.decode(server_encoding))
                
    # jsonlist is an array of json objects
    return jsonlist




jsonlist = get_treasury_securities()
for each_security_json in jsonlist:
    print("--------------------------------------------------------")
    print("CUSIP: ", each_security_json["cusip"])
    print("Security Type", each_security_json["securityType"])
    print("Issued Date", each_security_json["issueDate"])
    print("PricePer100", each_security_json["pricePer100"])
    print("--------------------------------------------------------")

