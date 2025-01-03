import streamlit as st


### --- HEADER SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/109504358.jpeg")

with col2:
    st.title("Minh Pham (Sparrowium)", anchor=False)
    st.write(
        "A student, trying to learn about Software, Firmware, and Hardware. So he can do some cool projects."
    )

# --- CONTACT SECTION ---
st.write("\n")
st.subheader("Contact", anchor=False)
st.write(
    """
    LinkedIn: www.linkedin.com/in/minh-pham-37b47b28b\n
    Github: https://github.com/Sparrowium
    """
)

# --- EDUCATION SECTION ---
st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    Associate of Science in Computer Science (Currently Studying)\n
    Houston Community College, Houston, Texas\n
    August 2023 - November 2024
    """
)

# --- SKILL SECTION ---
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Programming: Python, SQL, Go
    - Data Visualization: MS Excel
    - Databases: MySQL
    - Frameworks: Streamlit, Django
    - Tools: Git, VsCode, NeoVim
    """
)
