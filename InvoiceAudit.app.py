import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# 1. Sample Invoice Data
# -----------------------------
data = {
    "Amount": [5000, 7000, 4500, 12000, 6500, 8000, 4500, 3000, 15000, 4500],
    "GST": [18, 18, 18, 12, 18, 5, 18, 12, 28, 18],
    "Duplicate": [0, 0, 1, 0, 1, 0, 1, 0, 0, 1]
}
df = pd.DataFrame(data)

# -----------------------------
# 2. Machine Learning Model
# -----------------------------
X = df[["Amount", "GST"]]
y = df["Duplicate"]

model = RandomForestClassifier(n_estimators=10)
model.fit(X.values, y)

# -----------------------------
# 3. Streamlit UI
# -----------------------------
st.title("Audit System: Invoice Verification")
st.write("This system checks invoice duplication patterns using machine learning.")
st.text("-----------------------------------")

# User Input
amt = st.number_input("Enter Invoice Amount", min_value=0, value=4500)
gst = st.selectbox("Select GST Percentage", [5, 12, 18, 28], index=2)

# -----------------------------
# 4. Prediction
# -----------------------------
if st.button("Verify Invoice"):
    prediction = model.predict([[amt, gst]])
    st.write("### Analysis Result")
    
    if prediction[0] == 1:
        st.markdown(":red[**STATUS: DUPLICATE PATTERN DETECTED**]")
        st.write("Warning: This invoice matches previous duplicate records.")
    else:
        st.markdown(":green[**STATUS: INVOICE IS ORIGINAL**]")
        st.write("No suspicious duplicate pattern detected.")

# -----------------------------
# 5. Reference Data
# -----------------------------
if st.checkbox("Show Training Data"):
    st.table(df)
