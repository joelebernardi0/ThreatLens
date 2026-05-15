from jinja2 import Template
import plotly.express as px
import pandas as pd

def generate_report(results):
    # Convertiamo i risultati in DataFrame
    df = pd.DataFrame(results)

    # Creiamo un grafico a torta dei rischi
    fig = px.pie(df, names="risk", title="Distribuzione dei livelli di rischio")
    fig_html = fig.to_html(full_html=False)

    # Template HTML migliorato
    template = """
    <html>
    <head>
        <title>ThreatLens Report</title>
        <style>
            body { font-family: Arial; background: #f4f4f4; padding: 20px; }
            h1 { color: #333; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px; border-bottom: 1px solid #ccc; text-align: left; }
            th { background: #333; color: white; }
            .low { background: #c8f7c5; }
            .medium { background: #f9f7a1; }
            .high { background: #f7c5c5; }
            .unknown { background: #e0e0e0; }
        </style>
    </head>
    <body>
        <h1>ThreatLens — IOC Analysis Report</h1>

        <h2>Grafico dei rischi</h2>
        {{ graph }}

        <h2>Dettaglio IOC</h2>
        <table>
            <tr>
                <th>IOC</th>
                <th>Tipo</th>
                <th>Rischio</th>
                <th>Dati</th>
            </tr>

            {% for r in results %}
            <tr class="{{ r.risk|lower }}">
                <td>{{ r.ioc }}</td>
                <td>{{ r.type }}</td>
                <td>{{ r.risk }}</td>
                <td><pre>{{ r.data }}</pre></td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    html = Template(template).render(results=results, graph=fig_html)

    with open("output/report.html", "w") as f:
        f.write(html)
