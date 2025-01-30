# Displaying various forms of text
import streamlit as st


st.title("Streamlit Text and Media Display")
st.header("Header: Key Points")
st.subheader("Subheader: More Details")
st.text("This is a simple text.")
st.markdown("### Markdown: Streamlit supports _markdown_ formatting!")

# Displaying an image
image = Image.open("https://images.app.goo.gl/AC4UFsvU4Y9nNRc99")  # Ensure you have an image file named 'download.jpeg' in the same directory
st.image(image, caption='Sample Image', use_column_width=True)

# Displaying a video
st.video("https://www.youtube.com/watch?v=JwSS70SZdyM")
