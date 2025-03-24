import streamlit as st
import pandas as pd
from num2words import num2words


st.set_page_config(page_title="Customer Invoice", layout="centered")




total_value=0
item_count=0

# Check if customer details are in session_state
if 'invoice_data' in st.session_state and st.session_state.invoice_data:
        customer_details = st.session_state.invoice_data
else:
        #st.write("No customer details found.")
        customer_details = {
            "Invoice ID": "",
            "Payment": "",
            "Date": "",
            "Item Count": "",
            "Name": "",
            "Mobile": "",
        }


if 'item_info' in st.session_state and st.session_state.item_info:
    # Access item_info from session state
    item_infos = st.session_state.item_info
    total_value = sum(item.get("Total (BDT)", 0) for item in st.session_state.item_info)
    item_count = sum(item.get("Quantity", 0) for item in st.session_state.item_info)
    item_info = item_infos if isinstance(item_infos, list) else [item_infos]
else:
    #st.write("No items submitted yet.")
    item_info ={
        "Title": "",
        "Type": "",
        "Size": "",
        "Colour": "",
        "Price (BDT)":"",
        "Quantity":"",
        "Offer (BDT)":"",
        "Total (BDT)":"",
    }
    






# Set page configuration
# Add logo (Replace 'logo.png' with your actual file path or URL)

col1, col2 = st.columns([1, 3])  # Adjust ratio as needed

with col1:
    st.image("logo.png", width=150)  # Change width as needed
with col2:
    st.markdown("""
        <style>
        .contact-info {
            
            font-size: 16px;
            margin-top:10px;
            color: #B7A053; /* Change color */
            padding: 10px;
            margin-left:300px;
        }
        </style>
        <div class="contact-info">
             <b>MAIL:</b> info@bobbin.com.bd <br>
             <b>HOTLINE:</b> 09647469626 <br>
            <b>PHONE:</b> 01326892752
        </div>
    """, unsafe_allow_html=True)

# Title
st.markdown(
    "<h3 style='text-align: center; color:#B7A053; margin-top:-10px'>Invoice</h3>",
    unsafe_allow_html=True,
)

# Customer Details Section
st.markdown("<h5 style='color: #003366;'>Customer Details</h5>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    for key, value in list(customer_details.items())[:2]:  # First two items
        st.write(f"**{key}:** {value}")

with col2:
    for key, value in list(customer_details.items())[2:4]:  # Middle two items
        st.write(f"**{key}:** {value}")

with col3:
    for key, value in list(customer_details.items())[4:-1]:  # Last two items
        st.write(f"**{key}:** {value}")
    st.write(f"Item Count :{item_count}")
        

# Invoice Items Section
#st.markdown("<h3 style='color: #003366;'>Invoice Items</h3>", unsafe_allow_html=True)
if isinstance(item_info, list) and len(item_info) > 0:
    df = pd.DataFrame(item_info)
else:
    df = pd.DataFrame([item_info])  # Ensure it becomes a DataFrame

#df = pd.DataFrame([item_info])
#df = df.reset_index(drop=True)
#html_table = df.to_html(index=False, escape=False)
st.markdown(
    """
    <style>
        table {
            width: 100%;
            text-align: center !important;
        }
        th, td {
            text-align: center !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.table(df)  # Display items as a well-formatted table
#st.markdown(html_table, unsafe_allow_html=True)
# Pricing and Total
#st.markdown("<h3 style='color: #003366;'>Payment Summary</h3>", unsafe_allow_html=True)
shipping_fee = 0
in_words=num2words(total_value)

st.markdown(
    f"""
    <div style="padding: 2px; margin-top: 30px;">
        <p><strong>Shipping Fee:</strong> BDT {shipping_fee}</p>
        <p><strong>Total:</strong> BDT {total_value}</p>
        <p><strong>In Words:</strong> {in_words.capitalize()}<span> Taka Only</span></p>
    </div>
    """,
    unsafe_allow_html=True
)


# Return Policy
st.markdown("<h6>Return Policy</h6>", unsafe_allow_html=True)

return_policy = """
1 If any defect is found (damaged/defective/wrong product) after opening the box, inform BOBBIN (through inbox or calling 0964769666) immediately with a picture/video proof.
2 Return process must be initiated within 3 days of receiving the proof.
3 Product quality must be in original condition (unused & unwashed).
4 The Bobbin Box, product hand tags, polybag, and the original invoice must be returned.
5 Exchange delivery cost may be applicable.
6 Proportional offers are not applicable for returned products.
"""
st.markdown(f"<p style='font-size:15px;margin-top:-5px;'>{return_policy}</p>", unsafe_allow_html=True)

# Footer
# Footer: Social Links
st.markdown(
    """
    <head>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
    </head>
    """, 
    unsafe_allow_html=True
)
col1, col2, col3, col4 = st.columns([4, 6, 6, 6])  # Adjust column widths

with col1:
    st.markdown("<h5 style='color:#B7A053; margin-top: 2px;'>Find Us:</h5>", unsafe_allow_html=True)

# Add custom icons with FontAwesome in each column
# Add custom icons with FontAwesome in each column
with col2:
    st.markdown(
        """
        <a href="https://www.bobbin.com.bd" target="_blank" style="text-decoration: none;color:#B7A053">
            <i class="fas fa-globe" style="font-size: 24px; color:#000000;"></i><span style="padding-left: 10px;">www.bobbin.com.bd</span>
        </a>
        """, 
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <a href="https://www.facebook.com/bobbin.bd" target="_blank" style="text-decoration: none;color:#B7A053">
            <i class="fab fa-facebook" style="font-size: 24px; color: #000000;"></i><span style="padding-left: 10px;">Bobbin.bd</span>
        </a>
        """, 
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        """
        <a href="https://www.instagram.com/bobbin.bd" target="_blank" style="text-decoration: none;color:#B7A053">
            <i class="fab fa-instagram" style="font-size: 24px; color: #000000;"></i><span style="padding-left: 10px;">Bobbin.bd</span>
        </a>
        """, 
        unsafe_allow_html=True
    )
#st.write("📧 Email: support@bobbin.com.bd")
#st.write("☎ Phone: 0964769666")


st.markdown(
    """
    <div style="color: #B7A053; text-align: center;">
       HQ & DISPLAY CENTER- 13 & 52, 1st Floor, B-Block(Bipani Bitan-2) New Market, Chittagong.
    </div>
    <div style="color: #B7A053; text-align: center;">
    THANKS FOR CHOOSING BOBBIN
    </div>
    """, 
    unsafe_allow_html=True
)

# Signature Section
#st.markdown("<h3 style='color: #003366;'>Signatures</h3>", unsafe_allow_html=True)


st.markdown(
    """
    <div style="display: flex; justify-content: space-between;padding-top:5px;">
        <span>Customer Signature ____________________</span>
        <span>Authorized Signature ____________________</span>
    </div>
    """, 
    unsafe_allow_html=True
)

st.session_state.clear()