# 🛡️ **ThreatLens — Cyber Threat Intelligence Dashboard**  
### *Analisi, correlazione e visualizzazione di Indicatori di Compromissione (IOC)*

---

## 🚀 **Introduzione**

**ThreatLens** è una dashboard di Cyber Threat Intelligence progettata per automatizzare l’analisi di IP e hash, integrando fonti TI affidabili come **VirusTotal** e **AbuseIPDB**.  
L’obiettivo è fornire uno strumento leggero, modulare e immediato per attività di:

- triage rapido  
- investigazioni SOC  
- threat hunting  
- formazione e portfolio tecnico  

Il progetto nasce per offrire una soluzione moderna, intuitiva e facilmente estendibile, pensata per analisti junior e studenti di cybersecurity che vogliono lavorare con dati reali.

---

## 🧠 **Funzionalità Principali**

### 🔍 **Analisi automatica degli IOC**
- Riconoscimento automatico del tipo di IOC (IP vs hash)  
- Query verso API esterne  
- Normalizzazione dei dati  
- Classificazione del rischio tramite motore interno  

### 📊 **Dashboard interattiva**
- Grafico a torta della distribuzione dei rischi  
- Grafico a barre degli IOC analizzati  
- Radar chart del profilo di rischio  
- Tabella dettagliata con tutti i risultati  

### 🧩 **Architettura modulare**
- `vt_api.py` → integrazione VirusTotal  
- `abuseip_api.py` → integrazione AbuseIPDB  
- `risk_engine.py` → motore di scoring  
- `app.py` → orchestrazione Streamlit  

### 🎨 **Interfaccia moderna**
- Tema scuro stile SOC  
- Palette cyber (verde, rosso, arancione)  
- Layout responsive  

---

## 🏗️ **Architettura Tecnica**

```
ThreatLens/
│── src/
│     └── app.py
│── vt_api.py
│── abuseip_api.py
│── risk_engine.py
│── requirements.txt
│── README.md
```

### **Tecnologie utilizzate**
- Python 3.10+  
- Streamlit  
- Pandas  
- Plotly  
- Requests  

---

## 🧪 **Motore di Classificazione del Rischio**

Il modulo `risk_engine.py` assegna un livello di rischio basato su:

- detection ratio (VirusTotal)  
- confidence score (AbuseIPDB)  
- categorie di abuso  
- reputazione globale  
- presenza in blacklist  

Livelli disponibili:

- **High**  
- **Medium**  
- **Low**  
- **Unknown**

---

## 📁 **Input Supportati**

- File `.txt` contenenti:
  - indirizzi IP  
  - hash MD5/SHA1/SHA256  

Il sistema riconosce automaticamente il tipo di IOC.

---

## ⚙️ **Avvio del Progetto**

### Se il file è in `/src`:
```bash
python -m streamlit run src/app.py
```

### Se è nella root:
```bash
streamlit run app.py
```

---

## 🔮 **Roadmap**

- [ ] Integrazione con Shodan  
- [ ] Supporto per domini e URL  
- [ ] Esportazione PDF/CSV  
- [ ] Modalità “SOC Analyst” con timeline  
- [ ] Dashboard multi‑pagina  
- [ ] Integrazione con OTX e GreyNoise  

---

## 🧩 **Perché ThreatLens?**

- È leggero  
- È modulare  
- È estendibile  
- È pensato per analisti reali  
- È perfetto per un portfolio professionale  

ThreatLens dimostra capacità di:

- progettazione software  
- integrazione API  
- analisi dati  
- visualizzazione  
- threat intelligence  
- sviluppo di strumenti SOC  

---
