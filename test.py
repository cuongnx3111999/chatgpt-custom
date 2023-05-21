import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
def main():
    api_key=os.getenv("api_key")
    print(api_key)


if __name__ == '__main__':
    main()