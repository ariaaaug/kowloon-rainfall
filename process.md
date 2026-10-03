## Tools Used
- **AI Assistant**: Used to help scaffold the script logic for parsing Open-Meteo JSON structure and styling the Matplotlib bar chart layout.
## One Thing Kept
- **The data caching mechanism in
'fetch.py **: Keeping the raw JSON file locally
in "datal
allowed the script to
run seamlessly offline without re-fetching from the API every time.
## One Thing Rejected
- **AI-generated pandas dataframe**:
The
AI initially suggested using 'pandas to read the JSON file. Since the structure is a simple list from a dictionary, I rejected pandas to keep dependencies lightweight and stripped down to
standard libraries plus
'requests and
'matplotlib.