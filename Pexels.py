import streamlit as st
import requests

# Pexels API endpoint for searching for images
PEXELS_API_URL = "https://api.pexels.com/v1/search"

# Pexels API key
PEXELS_API_KEY = "YOUR_API_KEY"

# Create a function to search for images using the Pexels API
def search_images(query):
    headers = {
        "Authorization": f"Bearer {PEXELS_API_KEY}"
    }
    params = {
        "query": query,
        "per_page": 10
    }
    response = requests.get(PEXELS_API_URL, headers=headers, params=params)
    return response.json()

# Create a function to display the images in the app
def display_images(images):
    for image in images:
        st.image(image["src"]["large"], width=600)

# Create the main function for the app
def main():
    st.set_page_config(page_title="Pexels Image Search", page_icon=":camera:", layout="wide")
    st.title("Pexels Image Search")

    # Add a text input for the search query
    query = st.text_input("Enter a search query:")

    # Add a search button
    if st.button("Search"):
        images = search_images(query)["photos"]
        display_images(images)

# Run the app
if __name__ == "__main__":
    main()
