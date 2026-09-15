import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Konfigurasi Halaman Dashboard (Layout Wide)
st.set_page_config(
    page_title="Marvel System - Neon Dashboard", page_icon="⚡", layout="wide"
)

# Custom CSS untuk Efek Neon Box & Tampilan Industrial Modern (Dark Theme)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    
    /* Neon Box Container */
    .neon-box {
        background: rgba(17, 24, 39, 0.9);
        border: 2px solid #00f3ff;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.4), inset 0 0 15px rgba(0, 243, 255, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- HEADER SECTION ---
st.title("⚡ MARVEL SYSTEM - INDUSTRIAL MONITORING DASHBOARD")
st.markdown(
    "<p style='color: #00f3ff; font-size: 1.1rem;'>Real-time Debris & Condenser Removal System Analytics</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Data Tren Gangguan (2021 - 2026)
data = {
    "Tahun": [2021, 2022, 2023, 2024, 2025, 2026],
    "Downtime": [685, 132, 97, 30, 672, 0],
    "Frekuensi": [1, 1, 1, 1, 1, 0],
}
df = pd.DataFrame(data)

# --- LAYOUT KOLOM UTAMA ---
col1, col2 = st.columns([1, 2.2])

with col1:
  # Kotak Neon Biru untuk Informasi Sistem
  st.markdown(
      """
        <div class="neon-box">
            <h3 style='color: #00f3ff; margin-top: 0;'>🔧 Informasi Sistem</h3>
            <p><b>Komponen:</b> Modular Conveyor</p>
            <p><b>Fungsi Utama:</b> Penanganan debris & kondensor otomatis pada pembangkit listrik.</p>
            <hr style='border-color: rgba(0,243,255,0.3);'>
            <p style='color: #39ff14; font-weight: bold;'>Status 2026: Optimal / Zero Failure (Implementasi Berhasil!)</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # Metrik Kartu
  st.metric(
      label="Total Downtime 2025",
      value="672 Menit",
      delta="-672 Menit (Normal 2026)",
  )
  st.metric(
      label="Efisiensi Sistem Terkini", value="100% Optimal", delta="+100%"
  )

with col2:
  # --- GRAFIK NEON STYLE ---
  fig = go.Figure()

  # 1. Bar Chart untuk Frekuensi (Kali) - Tanpa teks angka di batangnya agar bersih dari tumpukan
  fig.add_trace(
      go.Bar(
          x=df["Tahun"],
          y=df["Frekuensi"],
          name="Frekuensi (kali)",
          marker_color="#00f3ff",
          yaxis="y2",
          opacity=0.55,
      )
  )

  # 2. Line Chart untuk Downtime (Menit) - Dilengkapi angka nilai di atas titik garis
  fig.add_trace(
      go.Scatter(
          x=df["Tahun"],
          y=df["Downtime"],
          name="Downtime (menit)",
          mode="lines+markers+text",
          text=df["Downtime"],
          textposition="top center",
          textfont=dict(color="#ffffff", size=13, family="Arial Black"),
          line=dict(color="#ff6600", width=4),
          marker=dict(
              size=11,
              color="#ff6600",
              line=dict(color="#ffffff", width=2),
          ),
      )
  )

  # Layout Grafik dengan Rentang Sumbu Y yang Lega & Bersih
  fig.update_layout(
      title="<b>Trending Kejadian Gangguan & Downtime (Neon Theme)</b>",
      xaxis=dict(
          title="Tahun",
          dtick=1,
          gridcolor="rgba(255,255,255,0.15)",
          range=[2020.5, 2026.5],
      ),
      yaxis=dict(
          title=dict(text="<b>Downtime (menit)</b>", font=dict(color="#ff6600")),
          gridcolor="rgba(255,255,255,0.15)",
          range=[-50, 850],  # Ruang atas & bawah dibuat lega
      ),
      yaxis2=dict(
          title=dict(text="<b>Frekuensi (kali)</b>", font=dict(color="#00f3ff")),
          overlaying="y",
          side="right",
          range=[0, 6],
          showgrid=False,
      ),
      legend=dict(
          orientation="h",
          yanchor="bottom",
          y=-0.28,
          xanchor="center",
          x=0.5,
          bgcolor="rgba(17, 24, 39, 0.95)",
          bordercolor="#00f3ff",
          borderwidth=1.5,
          font=dict(color="white"),
      ),
      template="plotly_dark",
      paper_bgcolor="rgba(0,0,0,0)",
      plot_bgcolor="rgba(17, 24, 39, 0.7)",
      hovermode="x unified",
      height=520,
      margin=dict(t=70, b=90, l=60, r=60),
  )

  # Menambahkan Anotasi Interaktif dengan Latar Belakang Solid Kontras Tinggi
  fig.add_annotation(
      x=2021,
      y=740,
      text="<b>Gangguan Kondensor</b>",
      showarrow=True,
      arrowhead=2,
      arrowcolor="#ff6600",
      ax=0,
      ay=-35,
      bgcolor="rgba(17, 24, 39, 0.95)",
      bordercolor="#ff6600",
      borderwidth=1.5,
      font=dict(color="#ff6600", size=12),
  )

  fig.add_annotation(
      x=2025,
      y=740,
      text="<b>Pemeliharaan Debris</b>",
      showarrow=True,
      arrowhead=2,
      arrowcolor="#ff6600",
      ax=0,
      ay=-35,
      bgcolor="rgba(17, 24, 39, 0.95)",
      bordercolor="#ff6600",
      borderwidth=1.5,
      font=dict(color="#ff6600", size=12),
  )

  fig.add_annotation(
      x=2026,
      y=180,
      text="<b>Implementasi Marvel System</b><br>(Zero Gangguan)",
      showarrow=True,
      arrowhead=2,
      arrowcolor="#00f3ff",
      ax=0,
      ay=-45,
      bgcolor="rgba(17, 24, 39, 0.95)",
      bordercolor="#00f3ff",
      borderwidth=1.5,
      font=dict(color="#00f3ff", size=12),
  )

  st.plotly_chart(fig, use_container_width=True)

# --- TABEL DATA DETAIL ---
st.markdown("---")
st.markdown(
    "<h3 style='color: #00f3ff;'>📋 Tabel Data Historis Gangguan</h3>",
    unsafe_allow_html=True,
)
st.dataframe(df, use_container_width=True)
