import requests

API_KEY = "LA_API_KEY"

def check_ip_abuse(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            data = r.json()["data"]
            return {"abuseConfidenceScore": data["abuseConfidenceScore"]}
        else:
            return {"error": "IP non trovato"}
    except:
        return {"error": "Errore nella richiesta a AbuseIPDB"}
