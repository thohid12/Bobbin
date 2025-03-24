import streamlit as st
import pandas as pd
from datetime import date

today = date.today()  # Get current date
def main():
    st.title("Customer Information Form")
    
    if 'item_info' not in st.session_state:
        st.session_state.item_info = []
    
    if 'invoice_data' not in st.session_state:
        st.session_state.invoice_data = {}
    
    with st.form("customer_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
        with col2:
            #payment = st.text_input("Payment")
            payment = st.selectbox("Payment", ["Cash","Bkash","Nagad"])
        
        col3, col4 = st.columns(2)
        
        with col3:
            mobile = st.text_input("Mobile")
        with col4:
            title = st.selectbox("Title", ["MENS PANJABI"])
        
        col5, col6 = st.columns(2)
        
        with col5:
            type_option = st.selectbox("Type", ["PANJABI"])
        with col6:
            size = st.selectbox("Size", ["S", "M", "L", "XL","XXL"])
        
        col7, col8 = st.columns(2)
        
        with col7:
            color = st.selectbox("Color", ["CREAM", "WINE", "BOTTLE GREEN", "GREEN", "BROWN","CREAM1","LIGHT BROWN","DEEP BROWN","WHITE MAROON","WHITE GOLD","WHITE ASH","WHITE","OFF WHITE","BLACK GOLD","ASH","BLACK",
                                           "BLACK WHITE","TEAL","TEAL BLACK","LIGHT PERROT","ORANGE","PERROT","OLIVE",
                                           "CHOCOLATE","OFF WHITE-GOLD"])
        with col8:
            quantity = st.number_input("Quantity", min_value=1, step=1)
        
        col9, col10 = st.columns(2)
        
        with col9:
            price = st.text_input("Price")
            price = int(price) if price.strip().isdigit() else 0  # Handle empty input
        with col10:
            offer = st.text_input("Offer")
            offer = int(offer) if offer.strip().isdigit() else 0  # Handle empty input
        
        Invoice = st.text_input("Invoice ID")
        
        col11, col12 = st.columns(2)
        
        with col11:
            submit_button = st.form_submit_button("Submit")
        with col12:
            preview_button = st.form_submit_button("Preview")
        
        # Default empty dictionary for item_details
        total=price*quantity- offer*quantity
       

        # Add the quantity to the item count
        
        
        item_details = {}
        customer_details = {}

        # Check if the submit button was clicked
        if submit_button:
            # Create item_details only when the form is submitted
            item_details = {
                "Title": title,
                "Type": type_option,
                "Size": size,
                "Color": color,
                "Quantity": quantity,
                "Offer (BDT)": offer,
                "Price (BDT)":price,
                "Total (BDT)":total
            }
            
            # Create customer details (only once)
            customer_details = {
                "Name": name,
                "Payment": payment,
                "Mobile": mobile,
                "Invoice ID": Invoice,
                "Date": today,
                "Item Count":"01"
            }
    
            # Optionally, store customer details in session state
            st.session_state.invoice_data = customer_details

            # Append the item details to session state
            st.session_state.item_info.append(item_details)
        
        # If preview button is pressed, switch to another page
        if preview_button:
            #st.session_state.item_info.append(item_details)  # Store the item details on preview
            st.switch_page("pages/Invoice.py")

if __name__ == "__main__":
    main()

