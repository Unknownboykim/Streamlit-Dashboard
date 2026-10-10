# =============================================================
# Ryan's Streamlit App  -  STARTER FILE
#
# 1. Run it:   streamlit run starter_app.py
# 2. Open Streamlit_Snippet_Menu.ipynb and pick your blocks.
# 3. Paste each block into the matching slot below, save, and
#    click "Rerun" (or press R) in the browser to see it appear.
#
# Order matters: Python runs top to bottom, so a block can only
# use variables (like `df` or `filtered`) created ABOVE it.
# =============================================================


# ---------- SLOT 1: Block A - Imports & page setup ----------
# (replace the two lines above with Block A)
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Penguin Explorer", layout="wide")

st.title("Palmer Penguins Explorer")
st.caption("An interactive look at 344 penguins from three islands in Antarctica.")

# ---------- SLOT 2: Block B - Load the data ----------
@st.cache_data
def load_data():
    df = pd.read_csv("data/penguins.csv")
    df = df.dropna()  # drop rows with missing measurements
    return df

df = load_data()

# ---------- SLOT 3: Block C - Sidebar filters ----------
# COPY → starter_app.py   (Block C: Sidebar filters)
st.sidebar.header("Filters")

species = st.sidebar.multiselect(
    "Species",
    options=sorted(df["species"].unique()),
    default=sorted(df["species"].unique()),
)
islands = st.sidebar.multiselect(
    "Island",
    options=sorted(df["island"].unique()),
    default=sorted(df["island"].unique()),
)
mass_min, mass_max = st.sidebar.slider(
    "Body mass (g)",
    min_value=int(df["body_mass_g"].min()),
    max_value=int(df["body_mass_g"].max()),
    value=(int(df["body_mass_g"].min()), int(df["body_mass_g"].max())),
    step=50,
)

filtered = df[
    df["species"].isin(species)
    & df["island"].isin(islands)
    & df["body_mass_g"].between(mass_min, mass_max)
]

if filtered.empty:
    st.warning("No penguins match those filters. Try widening them in the sidebar.")
    st.stop()

# ---------- SLOT 4: Block D - KPI metrics ----------
# COPY → starter_app.py   (Block D: KPI metrics row)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Penguins", len(filtered))
col2.metric("Avg body mass", f"{filtered['body_mass_g'].mean():,.0f} g")
col3.metric("Avg flipper", f"{filtered['flipper_length_mm'].mean():.1f} mm")
col4.metric("Species shown", filtered["species"].nunique())

st.divider()

# ---------- SLOT 5: Charts - pick from Blocks E, F, G, H ----------
px.scatter(df, x="flipper_length_mm", y="body_mass_g", color="species", hover_data=["island", "sex"])
st.subheader("Compare any two measurements")
numeric_cols = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
c1, c2 = st.columns(2)
x_axis = c1.selectbox("X axis", numeric_cols, index=0)
y_axis = c2.selectbox("Y axis", numeric_cols, index=1)

fig = px.scatter(filtered, x=x_axis, y=y_axis, color="species", hover_data=["island", "sex"])
st.plotly_chart(fig)

# ---------- SLOT 6: Extras - pick from Blocks I, J, K, L, M, N ----------
