import os
import random
from datetime import datetime, timedelta

import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')