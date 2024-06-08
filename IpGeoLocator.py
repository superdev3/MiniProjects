import requests
import json

while (True):
    ip_address = input("Ip Address to trace: ")
    request = requests.get(f"https://ipinfo.io/{ip_address}/json")

    match (request.status_code):
        case (200):
            request_json = json.loads(request.content)
            print(f"City: {request_json['city']}")
            print(f"Region: {request_json['region']}")
            print(f"Country: {request_json['country']}")
            print(f"Location: {request_json['loc']}")
            print(f"Timezone: {request_json['timezone']}")
            print(f"ASN: {request_json['org']}")
            print(f"Google Maps: https://google.com/maps/?q={request_json['loc']}")
            
        case _:
            print("[Error] Could not get Ip Information")
            continue
