import numpy as num
import pandas as pd
import streamlit as st
import os
import base64


# st.title("hello Visual studio")
# data=pd.read_csv("../dataFiles/retail_data.csv")
# st.dataframe(data)
# st.title(data.shape)
# print(data.info())

# Initialize session state if not already done
if 'selected_file' not in st.session_state:
    st.session_state.selected_file = None
if 'selected_column' not in st.session_state:
    st.session_state.selected_column = None
if 'selected_functionality' not in st.session_state:
    st.session_state.selected_functionality = None    
if 'dataframe' not in st.session_state:
    st.session_state.dataframe = None    

# Sidebar to select tab
selected_tab = st.sidebar.radio('Select Tab', ['Tab 1', 'Tab 2'])

if selected_tab == 'Tab 1':
        # Function to display PDF
        def show_pdf(file_path):
            with open(file_path, "rb") as f:
                file_path
                st.title(file_path)
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)

        st.title("PDF  Viewer")

        # Path to your PDF file
        pdf_file_path = "ADITYAKUMARRESUME.pdf"

        # Display PDF
        show_pdf(pdf_file_path)

if selected_tab == 'Tab 2':
    # Function to list all CSV files in a directory
    def list_csv_files(directory):
        return [f for f in os.listdir(directory) if f.endswith('.csv')]


    # Directory containing CSV files
    csv_directory = os.getcwd()  # Replace with your folder path

    # List all CSV files in the directory
    csv_files = list_csv_files(csv_directory)

    # Streamlit app
    st.title('CSV File Viewer')

    # Dropdown menu to select a CSV file
    selected_file = st.selectbox('Select a CSV file', csv_files)

    # Count function 
    def categoryCount(dataframe, column,selected_Function):
            return dataframe.groupby(column).agg( selected_Function=(column,selected_Function) ).reset_index()



    # Display the selected file content
    if st.button('Load CSV') or st.session_state.selected_file == selected_file:
        # Reset session state variables
        # st.session_state.selected_file = None
        # st.session_state.dataframe = None
        st.session_state.selected_column = None
        st.write(st.session_state.selected_file)
        st.write(selected_file)
        

        
        file_path = os.path.join(csv_directory, selected_file)
        if selected_file != st.session_state.selected_file or st.session_state.selected_file is None:
            st.write('Data loaded')
            st.session_state.dataframe = pd.read_csv(file_path)
        else:
            st.write('Data not loaded')   
    

        st.session_state.selected_file = selected_file  # Update session state

        st.write(f'### {selected_file}')
        # st.dataframe(df)
        st.dataframe(st.session_state.dataframe)
        if st.session_state.dataframe is not None:
            df = st.session_state.dataframe
            # Dropdown to select a column
            selected_column = st.selectbox('Select a column', df.columns.tolist(), index=df.columns.tolist().index(st.session_state.selected_column) if st.session_state.selected_column else 0)
            st.session_state.selected_column = selected_column  # Update session state
            st.write(f'You selected column: {selected_column}')
            
            selected_functionality=st.selectbox('Select a functionality',['sum','mean','count'])
            st.write(f'You selected column: {selected_functionality}')
            
            if st.button('Filter Data'):
                newDf=categoryCount(st.session_state.dataframe,selected_column,selected_functionality)
                st.dataframe(newDf)
    
