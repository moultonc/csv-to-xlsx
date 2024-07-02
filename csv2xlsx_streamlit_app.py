import os
import pandas as pd
import streamlit as st
from io import BytesIO

# Set up the Streamlit app
st.title("CSV to XLSX Converter")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv", help="Upload your CSV file here.")

# Process the uploaded file
if uploaded_file is not None:
    # Read the CSV file into a pandas DataFrame
    read_file = pd.read_csv(uploaded_file, sep=None, engine='python')
    st.success("CSV file uploaded and read successfully!")
    
    # Display the DataFrame (optional)
    st.write("Preview of the uploaded CSV file:")
    st.dataframe(read_file)
    
    # Save as Excel file and provide download link
    excel_buffer = BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
        read_file.to_excel(writer, index=False, header=True)
    excel_buffer.seek(0)
    st.success("File is ready for download.")

    # Present download button
    st.download_button(
        label="Download Excel file",
        data=excel_buffer,
        file_name='csv-to-xlsx.xlsx',
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
