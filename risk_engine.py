def classify_risk(data):
    if "error" in data:
        return "Unknown"

    # VirusTotal
    if "malicious" in data:
        if data["malicious"] > 5:
            return "High"
        elif data["malicious"] > 0:
            return "Medium"
        else:
            return "Low"

    # AbuseIPDB
    if "abuseConfidenceScore" in data:
        score = data["abuseConfidenceScore"]
        if score > 50:
            return "High"
        elif score > 10:
            return "Medium"
        else:
            return "Low"

    return "Unknown"
