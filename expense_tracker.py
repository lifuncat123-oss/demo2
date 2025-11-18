import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Persoanl Expense Tracker")

if 'expenses' not in st.session_state:
  st.session_state.expenses = pd.DataFrame(cloumns=['Date','Catrgory','Amount','Description'])
  
with st.form("expenses_form"):
  st.subheader("Add New Expense")
  date = st.data_input("Date")
  category = st.selectbox("Category", ["Food", "Transport", "Environment", "Bills" ,"Others"])
  amount = st.nuber_input("Amount", min_value=0.1, step=0.01)
  description = st.text_input("Description")

submitted = st.form_submit_button("Add Expense")
if submitted:
  new_expense = pd.DataFrame({
    'Date' : [date],
    'Category' : [category],
    'Amount' : [amount],
    'Description: [description]
  })
  st.session_state.expesnes = pd.concat([st.sessiom_state.expenses, new_expesne], ignore_index=True)
  st.success("Expenses add successfully!')
if not st.session_date.expenses.empty
    st.subheader("Your Expenses")
    st.dataframe(st.session_state.expenses)
    st.subheader("Summary")
    total_spent = st.session_state.expenses['Amount'].sum()
    st.write(f"Total Spent: ${total_spent:.2f}")
category_totals=st.session_state.expenses.groupby('Category')['Amount'].sum()
               
    fig, ax= plt.subplots(figsize=(10,6))
    ax.pie(category_total.values, labels=catergory_totals.index, autopct='%1.1f%%')
    ax.set_titlle("Expenses by Category")
    st.pyplot(fig)

  
