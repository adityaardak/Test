# Displaying various forms of text
import streamlit as st
import Image

st.title("Streamlit Text and Media Display")
st.header("Header: Key Points")
st.subheader("Subheader: More Details")
st.text("This is a simple text.")
st.markdown("### Markdown: Streamlit supports _markdown_ formatting!")

# Displaying an image
image = Image.open("DALL·E 2024-12-17 09.40.06 - A highly realistic image of a busy Indian urban traffic intersection with heavy vehicle congestion. The scene includes cars, buses, mot")  # Ensure you have an image file named 'download.jpeg' in the same directory
st.image(image, caption='Sample Image', use_column_width=True)

# Displaying a video
st.video("https://www.youtube.com/watch?v=JwSS70SZdyM")
