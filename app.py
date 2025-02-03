import streamlit as st

from datetime import datetime

from cal import PataphysicalDate

d = st.date_input("Enter a vulgate date", value=datetime.now().date())
pd = PataphysicalDate.from_vulgate(d)
st.write("Pataphysical date: `", str(pd), "`")


pd_in = st.text_input("Enter a Pataphysical date", value=str(pd))
d_in = PataphysicalDate.from_str(pd_in).date_vulg
st.write(f"Vulgate date: `{d_in.strftime('%A %d %B %Y')} ({str(d_in)})`")
