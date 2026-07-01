import streamlit as st
import plotly.graph_objects as go


def render_trend(city_df):

    st.markdown("## 📈 AQI Trend Analysis")

    df = city_df.copy()

    # Make sure Date column exists
    if "Date" not in df.columns:
        st.error("Date column not found.")
        return

    # Last 30 records
    df = df.tail(30)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["AQI"],
            mode="lines+markers",
            name="AQI",
            line=dict(
                color="#3B82F6",
                width=4
            ),
            marker=dict(
                size=7,
                color="#60A5FA"
            ),
            fill="tozeroy",
            fillcolor="rgba(59,130,246,0.15)"
        )
    )

    fig.update_layout(

        paper_bgcolor="#172338",
        plot_bgcolor="#172338",

        height=420,

        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        ),

        font=dict(
            color="white",
            size=14
        ),

        hovermode="x unified",

        xaxis=dict(
            title="Date",
            showgrid=False,
            zeroline=False
        ),

        yaxis=dict(
            title="AQI",
            showgrid=True,
            gridcolor="rgba(255,255,255,0.08)",
            zeroline=False
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )