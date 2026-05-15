import requests

API_KEY = "LA_API_KEY"

def check_hash_vt(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": API_KEY}
    
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            positives = data["data"]["attributes"]["last_analysis_stats"]["malicious"]
            return {"malicious": positives}
        else:
            return {"error": "Hash non trovato"}
    except:
        return {"error": "Errore nella richiesta a VirusTotal"}
