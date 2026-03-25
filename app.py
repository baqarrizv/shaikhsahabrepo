import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Production Detail Viewer", layout="wide")

# 1. Load the Data
@st.cache_data
def load_data():
    # Load raw data
    df = pd.read_csv('Excel.xlsx - Main Sheet.csv', header=None)
    
    # Extract Row 2 for sub-headings (Column names)
    col_names = df.iloc[1].values
    
    # Main data starts from Row 3
    data = df.iloc[2:].reset_index(drop=True)
    data.columns = col_names
    return data

df = load_data()

# 2. Sidebar Filter (Detail Section Selection)
st.sidebar.header("Filter Details")
order_list = df['ORDER NO'].unique().tolist()
selected_order = st.sidebar.selectbox("Select ORDER NO", order_list)

# Filter the data for the selected Order
record = df[df['ORDER NO'] == selected_order].iloc[0]

# 3. Main App Title
st.title(f"Production Details: {selected_order}")

# 4. "Detail Section" (Columns A to N)
st.subheader("General Details")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("FPR TYPE", record['FPR TYPE'])
    st.write(f"*Date:* {record['FPR DATE']}")
with col2:
    st.write(f"*Customer:* {record['CUSTOMER']}")
    st.write(f"*Blend:* {record['BLEND']}")
with col3:
    st.write(f"*Process:* {record['PROCESS']}")
    st.write(f"*Loom:* {record['LOOM']}")
with col4:
    st.write(f"*Fabric Type:* {record['FABRIC TYPE']}")
    st.write(f"*Lot Size:* {record['LOT SIZE']}")

st.divider()

# 5. Main Headings Section (Columns O to AH)
# We divide these into the 4 groups identified in Row 1 of your sheet
tab1, tab2, tab3, tab4 = st.tabs([
    "Quality Assurance Deptt", 
    "Processing Instructions", 
    "Quality & Lab", 
    "Packing Instructions"
])

# Define the column mappings based on your sheet structure
with tab1:
    st.header("Quality Assurance Deptt")
    st.info(f"*Instruction:* {record['Instruction:']}")

with tab2:
    st.header("Processing Instructions")
    c1, c2 = st.columns(2)
    c1.write(f"*Shade:* {record['Shade:']}")
    c1.write(f"*Finish & Handle:* {record['Finish & Handle:']}")
    c1.write(f"*Special Process:* {record['Special Process:']}")
    c2.write(f"*Singeing:* {record['Singeing:']}")
    c2.write(f"*Sample Test:* {record['Sample Test:']}")
    c2.write(f"*Quality:* {record['Quality:']}")

with tab3:
    st.header("Quality & Lab")
    c1, c2 = st.columns(2)
    c1.write(f"*GSM:* {record['GSM:']}")
    c1.write(f"*Air Permeability:* {record['Air Permeability:']}")
    c1.write(f"*Ph Value:* {record['Ph Value:']}")
    c2.write(f"*Bowing & Skewing:* {record['Bowing & Skewing:']}")
    c2.write(f"*Shrinkage:* {record['Shrinkage:']}")

with tab4:
    st.header("Packing Instructions")
    c1, c2 = st.columns(2)
    c1.write(f"*Quantity / Roll:* {record['Quantity / Roll:']}")
    c1.write(f"*Minimum Piece Length:* {record['Minimum Piece Length:']}")
    c1.write(f"*Allowed Defect:* {record['Allowed Defect:']}")
    c1.write(f"*Seams / Roll:* {record['Seams / Roll:']}")
    c2.write(f"*Shiny Side:* {record['Shiny Side:']}")
    c2.write(f"*Polypropylene:* {record['Polypropylene:']}")
    c2.write(f"*Paper Tubes:* {record['Paper Tubes:']}")
    c2.write(f"*Shipping Marks:* {record['Shipping Marks:']}")