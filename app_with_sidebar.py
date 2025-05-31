
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail Dashboard", layout="wide")
st.title("🛍️ Retail Product Analysis Dashboard")

# Load and clean data
df = pd.read_csv("Test-Set.csv")
df['FatContent'] = df['FatContent'].replace({
    'low fat': 'Low Fat',
    'LF': 'Low Fat',
    'reg': 'Regular'
})
df['Weight'] = df['Weight'].fillna(df['Weight'].mean())
df['OutletSize'] = df['OutletSize'].fillna(df['OutletSize'].mode()[0])

# ======================
# 🔲 Sidebar - Filters
# ======================
st.sidebar.header("🧪 Filter Options")

selected_fat = st.sidebar.selectbox("Select Fat Content:", df['FatContent'].unique())
selected_outlet = st.sidebar.selectbox("Select Outlet Type:", df['OutletType'].unique())

# 🔍 Apply Filters
filtered_df = df[
    (df["FatContent"] == selected_fat) &
    (df["OutletType"] == selected_outlet)
]

# Section 1: FatContent vs MRP
st.header(f"📈 Average MRP for {selected_fat} in {selected_outlet}")
avg_price = filtered_df.groupby("FatContent")["MRP"].agg(['count', 'mean', 'std', 'min', 'max']).reset_index()
st.dataframe(avg_price)

# Numeric summary
for _, row in avg_price.iterrows():
    st.markdown(f"🔸 **{row['FatContent']}** → Average Price: **{row['mean']:.2f} €** | Count: {int(row['count'])}")

# Bar chart
fig1 = px.bar(avg_price, x="FatContent", y="mean", color="FatContent", title="Average MRP by FatContent")
st.plotly_chart(fig1, use_container_width=True)

# Section 2: OutletType vs MRP
st.header("🛒 Average MRP by OutletType")
outlet_price = filtered_df.groupby("OutletType")["MRP"].agg(['count', 'mean', 'std', 'min', 'max']).reset_index()
st.dataframe(outlet_price)

for _, row in outlet_price.iterrows():
    st.markdown(f"🏪 **{row['OutletType']}** → Average Price: **{row['mean']:.2f} €** | Products: {int(row['count'])}")

fig2 = px.bar(outlet_price, x="OutletType", y="mean", color="OutletType", title="Average MRP by OutletType")
st.plotly_chart(fig2, use_container_width=True)

# Section 3: Rare Product Types
st.header("🎯 Rare Product Types ( < 100 items )")
rare_products = df["ProductType"].value_counts()[df["ProductType"].value_counts() < 100].reset_index()
rare_products.columns = ["ProductType", "Count"]
st.dataframe(rare_products)

fig3 = px.bar(rare_products, x="ProductType", y="Count", color="ProductType", title="Rare Product Types")
st.plotly_chart(fig3, use_container_width=True)
