
import streamlit as st

# Title
st.title("Audit Issue 1 – Estimated Liabilities (Cell Phone Warranties)")

# Critical Thinking Steps Refresher
st.header("Critical Thinking Steps Refresher")
st.write("List the 3 critical thinking steps you will be applying (in the appropriate order).")

# Numbered short text areas (two lines each)
for i in range(1, 4):
    st.text_area(f"Step {i}", height=50)

# Audit Issue
st.header("Audit Assignment")
st.write("Verify the accuracy and completeness of the recorded liability for cell phone warranties.")

# Step 1 prompt with 4 response boxes (2 lines each)
st.subheader("Step 1")
st.write("Ask yourself: What is the specific issue I need to resolve? "
         "Do not list audit procedures yet.")

for j in range(1, 5):
    st.text_area(f"Response {j}", height=50)
