import streamlit as st

def main():
    """main function"""
    st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    

    st.sidebar.success("Select a project demo on the left side.")
if __name__ == "__main__":
    main()