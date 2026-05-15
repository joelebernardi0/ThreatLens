import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from vt_api import check_hash_vt
from abuseip_api import check_ip_abuse
from risk_engine import classify_risk

st.set_page_config(
    page_title="ThreatLens Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# ============================
#   BACKGROUND FIX (FUNZIONA)
# ============================
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapercave.com/wp/wp2757874.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* OVERLAY */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.65);
    z-index: 0;
}

/* CONTENT */
.block-container {
    position: relative;
    z-index: 1;
    background: rgba(0,0,0,0.55);
    padding: 2rem;
    border-radius: 12px;
    backdrop-filter: blur(6px);
}

/* TEXT */
h1, h2, h3, label, .stMarkdown {
    color: #00ff9d !important;
    font-family: "Courier New", monospace;
    text-shadow: 0px 0px 8px #00ff9d;
}

/* TABLE */
.dataframe {
    background-color: rgba(0,0,0,0.6) !important;
    color: #00ff9d !important;
    border: 1px solid #00ff9d !important;
}

/* SIDEBAR */
.sidebar .sidebar-content {
    background-color: rgba(0,0,0,0.7) !important;
    color: #00ff9d !important;
}

/* BUTTON */
.stButton>button {
    background-color: #00ff9d !important;
    color: black !important;
    border-radius: 6px;
    border: none;
    font-weight: bold;
    box-shadow: 0px 0px 10px #00ff9d;
}
.stButton>button:hover {
    background-color: #00cc7a !important;
    box-shadow: 0px 0px 20px #00ff9d;
}

</style>
""", unsafe_allow_html=True)

# ============================
#   TITLE
# ============================
st.markdown('<h1>ThreatLens — Intelligence Dashboard</h1>', unsafe_allow_html=True)
st.markdown("### Analisi di IP, Hash e Indicatori di Compromissione")

# ============================
#   FILE UPLOAD
# ============================
uploaded_file = st.file_uploader("Carica un file di IOC (.txt)", type=["txt"])

if uploaded_file:
    iocs = [line.decode("utf-8").strip() for line in uploaded_file.readlines()]
    results = []

    st.markdown("## Analisi in corso...")

    for ioc in iocs:
        st.markdown(f"**Analizzo:** `{ioc}`")

        if "." in ioc and not ioc.isdigit():
            data = check_ip_abuse(ioc)
            risk = classify_risk(data)
            results.append({"ioc": ioc, "type": "IP", "risk": risk, "data": data})
        else:
            data = check_hash_vt(ioc)
            risk = classify_risk(data)
            results.append({"ioc": ioc, "type": "HASH", "risk": risk, "data": data})

    df = pd.DataFrame(results)

    # ============================
    #   TABLE
    # ============================
    st.markdown("## Risultati")
    st.dataframe(df)

    # ============================
    #   GRAPH 1 — CYBER PIE
    # ============================
    st.markdown("## Distribuzione dei rischi")

    fig1 = px.pie(
        df,
        names="risk",
        hole=0.5,
        color="risk",
        color_discrete_map={
            "High": "#ff0033",
            "Medium": "#ffae00",
            "Low": "#00ff9d",
            "Unknown": "#888888"
        }
    )
    fig1.update_traces(textinfo="label+percent", pull=[0.05]*len(df))
    fig1.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#00ff9d",
        title_font_color="#00ff9d"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ============================
    #   GRAPH 2 — CYBER BAR
    # ============================
    st.markdown("## IOC Risk Overview")

    fig2 = px.bar(
        df,
        x="ioc",
        y=[1]*len(df),
        color="risk",
        color_discrete_map={
            "High": "#ff0033",
            "Medium": "#ffae00",
            "Low": "#00ff9d",
            "Unknown": "#888888"
        }
    )
    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#00ff9d",
        title_font_color="#00ff9d",
        xaxis_title="IOC",
        yaxis_title="Severity"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # ============================
    #   GRAPH 3 — CYBER RADAR
    # ============================
    st.markdown("## Threat Radar")

    risk_counts = df["risk"].value_counts()

    fig3 = go.Figure()
    fig3.add_trace(go.Scatterpolar(
        r=risk_counts.values,
        theta=risk_counts.index,
        fill='toself',
        line_color="#00ff9d",
        line_width=3
    ))
    fig3.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0.4)",
            radialaxis=dict(visible=True, range=[0, max(risk_counts.values)])
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#00ff9d"
    )
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.markdown("### Carica un file .txt con IP o hash per iniziare l’analisi.")
