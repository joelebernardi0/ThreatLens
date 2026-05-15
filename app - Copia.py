import streamlit as st
import pandas as pd
import plotly.express as px
from vt_api import check_hash_vt
from abuseip_api import check_ip_abuse
from risk_engine import classify_risk

st.set_page_config(
    page_title="ThreatLens Hacker Dashboard",
    page_icon="🕶️",
    layout="wide"
)

# ============================
#   4K VIDEO BACKGROUND
# ============================
st.markdown("""
<style>
video#bgvid {
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -2;
    filter: brightness(0.35) blur(2px);
}

.block-container {
    background: rgba(0, 0, 0, 0.55);
    padding: 2rem;
    border-radius: 12px;
    backdrop-filter: blur(6px);
}

h1, h2, h3, label, .stMarkdown {
    color: #00ff9d !important;
    text-shadow: 0px 0px 10px #00ff9d;
}

.dataframe {
    background-color: rgba(0,0,0,0.6) !important;
    color: #00ff9d !important;
}

.sidebar .sidebar-content {
    background-color: rgba(0,0,0,0.7) !important;
}
</style>

<video autoplay muted loop id="bgvid">
  <source src="https://cdn.coverr.co/videos/coverr-green-digital-code-rain-1080p?token=123" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# ============================
#   TITLE
# ============================
st.markdown("<h1>🕶️ ThreatLens — Hacker Intelligence Dashboard</h1>", unsafe_allow_html=True)
st.markdown("### Analisi dinamica di IP, Hash e DNS — stile cyber 🔥")

# ============================
#   FILE UPLOAD
# ============================
uploaded_file = st.file_uploader("Carica un file di IOC (.txt)", type=["txt"])

if uploaded_file:
    iocs = [line.decode("utf-8").strip() for line in uploaded_file.readlines()]
    results = []

    st.markdown("## 🚀 Analisi in corso...")

    for ioc in iocs:
        st.markdown(f"🔍 **Analizzo:** `{ioc}`")

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
    st.markdown("## 📋 Risultati")
    st.dataframe(df)

    # ============================
    #   GRAPH 1 — RISK PIE
    # ============================
    st.markdown("## 📈 Distribuzione dei rischi")

    fig1 = px.pie(
        df,
        names="risk",
        title="Threat Levels",
        color="risk",
        color_discrete_map={
            "High": "#ff0040",
            "Medium": "#ffae00",
            "Low": "#00ff9d",
            "Unknown": "#888888"
        }
    )
    fig1.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#00ff9d"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ============================
    #   GRAPH 2 — BAR CHART
    # ============================
    st.markdown("## 📊 IOC Risk Overview")

    fig2 = px.bar(
        df,
        x="ioc",
        y=[1]*len(df),
        color="risk",
        title="IOC Risk Overview",
        color_discrete_map={
            "High": "#ff0040",
            "Medium": "#ffae00",
            "Low": "#00ff9d",
            "Unknown": "#888888"
        }
    )
    fig2.update_layout(
        showlegend=True,
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#00ff9d"
    )
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.markdown("### 📄 Carica un file .txt con IP o hash per iniziare l’analisi.")
