🛡️ ThreatLens — Cyber Threat Intelligence Dashboard

https://dummyimage.com/1200x250/000/00ff9d\&text=ThreatLens+Cyber+Intelligence+Dashboard



🔰 Badge del Progetto

https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python

https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge\&logo=streamlit

https://img.shields.io/badge/Threat%20Intelligence-IOC%20Analysis-green?style=for-the-badge

https://img.shields.io/badge/Status-Active-success?style=for-the-badge



🧭 Panoramica del Progetto

ThreatLens è una dashboard interattiva progettata per analizzare Indicatori di Compromissione (IOC) come indirizzi IP e hash di file.

Integra fonti di Threat Intelligence esterne (VirusTotal e AbuseIPDB) e fornisce una classificazione del rischio con visualizzazioni chiare e orientate al lavoro di un SOC Analyst.



Il progetto è pensato per:



studenti di cybersecurity



SOC Analyst junior



attività di triage rapido



portfolio tecnico professionale



🎯 Obiettivi del Progetto

Automatizzare l’analisi di IP e hash



Fornire una classificazione del rischio affidabile



Visualizzare i risultati con grafici interattivi



Offrire un’interfaccia moderna in stile cyber



Rendere il progetto modulare ed estendibile



🏗️ Architettura Tecnica

Frontend

Framework: Streamlit



Funzionalità:



Upload file IOC



Visualizzazioni interattive



Tema grafico personalizzato



Backend

Linguaggio: Python



Moduli principali:



vt\_api.py → integrazione VirusTotal



abuseip\_api.py → integrazione AbuseIPDB



risk\_engine.py → classificazione del rischio



app.py → orchestrazione dashboard



API Esterne

VirusTotal → reputazione hash



AbuseIPDB → reputazione IP



🔄 Flusso di Funzionamento

L’utente carica un file .txt con IP o hash



Il sistema identifica automaticamente il tipo di IOC



Vengono interrogate le API esterne



I dati vengono normalizzati e classificati



La dashboard mostra:



tabella dei risultati



grafico a torta dei rischi



grafico a barre degli IOC



radar chart del profilo di rischio



🧪 Classificazione del Rischio

Il motore di rischio assegna uno dei seguenti livelli:



High



Medium



Low



Unknown



Basandosi su:



detection ratio



confidence score



categorie di abuso



reputazione globale



🖥️ Screenshots

(Sostituisci questi link con screenshot reali del tuo progetto)



https://dummyimage.com/1200x700/000/00ff9d\&text=Dashboard+Screenshot

https://dummyimage.com/1200x700/000/00ff9d\&text=Risk+Visualization



⚙️ Requisiti

Python 3.10+



Moduli Python:



streamlit



pandas



plotly



requests



🚀 Avvio del Progetto

Se il file è in /src:

bash

python -m streamlit run src/app.py

Se il file è nella root:

bash

streamlit run app.py

📌 Struttura del Progetto

Codice

ThreatLens/

│── src/

│     └── app.py

│── vt\_api.py

│── abuseip\_api.py

│── risk\_engine.py

│── requirements.txt

│── README.md

🔮 Possibili Estensioni Future

Integrazione con Shodan, GreyNoise, OTX



Supporto per domini e URL



Esportazione PDF/CSV



Modalità SOC Analyst



Dashboard multi‑pagina



🏁 Conclusioni

ThreatLens è un progetto completo e professionale per l’analisi di IOC, ideale per portfolio, laboratori di cybersecurity e attività di Threat Intelligence.

La sua struttura modulare permette di estenderlo facilmente con nuove fonti e funzionalità.

