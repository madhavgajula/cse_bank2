import streamlit as st
import pandas as pd
from supabase import create_client

#supabase config

SUPABASE_URL="https://qnzofivdmdvtyvohneom.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFuem9maXZkbWR2dHl2b2huZW9tIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDIyODUsImV4cCI6MjA4MTYxODI4NX0.pteLuRmWgl-wILg4oQ3BGtw_BJ4X_robL045NPlT63w"
supabase=create_client(SUPABASE_URL,SUPABASE_KEY)

#Streamlit UI

st.title("HDFC BANK (supabase)")
menu=["REGISTER","VIEW"]
choice=st.sidebar.selectbox("Menu",menu)

#Register

if choice == "REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("Age",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    balance=st.number_input("BALANCE",min_value=500)
    if st.button("SAVE"):
        supabase.table("users").insert({"name": name,"age": age,"account": account,
                                        "balance": balance}).execute()
        st.success("User added succesfully ")

#view students

if choice =="VIEW":
    st.subheader("view users")
    data=supabase.table("users").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)
