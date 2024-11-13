import logging
import os 
import requests

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
        with open('notes.txt', 'r') as file:
            for each_line in file:
                print(each_line)

        



if __name__ == "__main__":
    instantiate = MainView()
    response = instantiate.main()
