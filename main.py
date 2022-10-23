import requests 

ip = input("Enter IP: ")

response = requests.get(f"https://proxycheck.io/v2/{ip}?vpn=1&asn=1")
if response.status_code == 200:
    data = response.json()
    print("proxy check result return",  data.get(ip).get("proxy"))
