import logging
import os 
<<<<<<< HEAD
import requests
import time
=======
>>>>>>> 167ff169 (Initial commit)

import streamlit as st  

# Suppress verbose DEBUG logs from external libraries
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.DEBUG,  # Set logging level to show only critical errors
    format="{asctime} | {levelname} | {name} | {message}",  # Define the format for log messages
    style="{",  # Use the new style format with curly braces
    datefmt="%Y-%m-%d %H:%M:%S",  # Set the date format for log messages
    force=True,  # Override any previous logging configuration
)

class MainView():
    def __init__(self):
        pass

    def main(self):
<<<<<<< HEAD
        st.cache_data.clear()  # Clear Streamlit's cache explicitly
        timestamp = int(time.time())  # Current timestamp
        file_url = f"https://raw.githubusercontent.com/agentggg/ComputerScienceNotes/main/notes.txt?{timestamp}"
        response = requests.get(file_url)
        file_content = response.text
        for each_line in file_content.splitlines():
            st.write(each_line)
=======
        
>>>>>>> 167ff169 (Initial commit)
        



if __name__ == "__main__":
    instantiate = MainView()
    response = instantiate.main()
