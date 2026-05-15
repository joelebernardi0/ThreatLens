import sys
from vt_api import check_hash_vt
from abuseip_api import check_ip_abuse
from risk_engine import classify_risk
from report_generator import generate_report

def load_iocs(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

def main():
    print("=== ThreatLens — IOC Analyzer ===")

    iocs = load_iocs("data/sample_iocs.txt")
    results = []

    for ioc in iocs:
        print(f"\nAnalizzo: {ioc}")

        # Se contiene un punto, lo trattiamo come IP
        if "." in ioc and not ioc.isdigit():
            abuse_data = check_ip_abuse(ioc)
            risk = classify_risk(abuse_data)
            results.append({
                "ioc": ioc,
                "type": "ip",
                "data": abuse_data,
                "risk": risk
            })

        # Altrimenti lo trattiamo come hash
        else:
            vt_data = check_hash_vt(ioc)
            risk = classify_risk(vt_data)
            results.append({
                "ioc": ioc,
                "type": "hash",
                "data": vt_data,
                "risk": risk
            })

    generate_report(results)
    print("\nReport generato in /output/report.html")

if __name__ == "__main__":
    main()
