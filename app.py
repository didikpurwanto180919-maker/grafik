import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Konfigurasi Halaman Dashboard
st.set_page_config(
    page_title="Marvel System - Dashboard Gangguan Konveyor",
    page_icon="⚙️",
    layout="wide",
)

# Custom CSS untuk memperindah tampilan dashboard industrial
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- HEADER SECTION ---
st.title("⚙️ Dashboard Monitoring & Tren Kejadian Gangguan")
st.markdown(
    "**Marvel System** - Modular Conveyor for Jellyfish Removal & Power Plant Maintenance"
)
st.markdown("---")

# Data Tren Berdasarkan Grafik (2021 - 2026)
data = {
    "Tahun": [2021, 2022, 2023, 2024, 2025, 2026],
    "Downtime": [685, 132, 97, 30, 672, 0],
    "Frekuensi": [1, 1, 1, 1, 1, 0],
}
df = pd.DataFrame(data)

# --- LAYOUT KOLOM UTAMA ---
col1, col2 = st.columns([1, 2])

with col1:
  st.subheader("🔧 Informasi Sistem")
  st.info(
      "**Komponen:** Modular Conveyor\n\n"
      "**Fungsi Utama:** Penanganan debris & kondensor pada "
      "pembangkit listrik.\n\n"
      "**Status Terkini (2026):** Implementasi *Marvel System* "
      "berhasil mereduksi downtime hingga **0 menit** (Tidak terjadi gangguan)."
  )

  st.metric(
      label="Total Downtime 2025", value="672 Menit", delta="-672 Menit (2026)"
  )
  st.metric(
      label="Status Operasional 2026",
      value="Optimal / Zero Failure",
      delta="Normal",
  )

with col2:
  st.subheader("📈 Grafik Tren Kejadian Gangguan (2021 - 2026)")

  # Membuat Dual-Axis Chart menggunakan Plotly
  fig = go.Figure()

  # Line Chart untuk Downtime (Menit) - Warna Oranye
  fig.add_trace(
      go.Scatter(
          x=df["Tahun"],
          y=df["Downtime"],
          name="Downtime (menit)",
          mode="lines+markers+text",
          text=df["Downtime"],
          textposition="top center",
          line=dict(color="#FF6600", width=3),
          marker=dict(size=8),
      )
  )

  # Bar Chart untuk Frekuensi (Kali) - Warna Biru
  fig.add_trace(
      go.Bar(
          x=df["Tahun"],
          y=df["Frekuensi"],
          name="Frekuensi (kali)",
          marker_color="#003366",
          yaxis="y2",
          opacity=0.7,
      )
  )

  # Layout Grafik
  fig.update_layout(
      title="<b>Trending Kejadian Gangguan & Downtime</b>",
      xaxis=dict(title="Tahun", tickmode="linear"),
      yaxis=dict(
          title="<b>Downtime (menit)</b>", titlefont=dict(color="#FF6600")
      ),
      yaxis2=dict(
          title="<b>Frekuensi (kali)</b>",
          titlefont=dict(color="#003366"),
          overlaying="y",
          side="right",
          range=[0, 5],
      ),
      legend=dict(x=0.01, y=0.99),
      template="plotly_white",
      hovermode="x unified",
      height=450,
  )

  # Menambahkan Anotasi Sorotan
  fig.add_annotation(
      x=2021,
      y=685,
      text="Gangguan Kondensor",
      showarrow=True,
      arrowhead=2,
      ax=-40,
      ay=-40,
  )

  fig.add_annotation(
      x=2025,
      y=672,
      text="Pemeliharaan Debris & Kondensor",
      showarrow=True,
      arrowhead=2,
      ax=50,
      ay=-40,
  )

  fig.add_annotation(
      x=2026,
      y=50,
      text="Implementasi Marvel System<br>(Zero Gangguan)",
      showarrow=True,
      arrowhead=2,
      ax=80,
      ay=-60,
      bgcolor="#FFD580",
      bordercolor="#FF6600",
  )

  st.plotly_chart(fig, use_container_width=True)

# --- TABEL DATA DETAIL ---
st.markdown("---")
st.subheader("📋 Tabel Data Historis Gangguan")
st.dataframe(df, use_container_width=True)
