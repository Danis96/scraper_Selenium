import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extracr_body_content
from parse import parse_with_ollama


st.title("AI Web Scraper")
url = st.text_input("Enter the URL of the website you want to scrape:")

if st.button("Scrape site"):
    st.write(f"Scraping data from {url} ...")
    html_result = scrape_website(url)
    body_content = extracr_body_content(html_result)
    cleaned_content = clean_body_content(body_content)
    
    # save the cleaned content to the session state
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM content", cleaned_content, height=300)



if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse from the DOM content")
    if st.button("Parse content"):
      if parse_description:
        st.write(f"Parsing DOM content for {parse_description} ...")
        
        dom_chunks = split_dom_content(st.session_state.dom_content)
        parsed_results = parse_with_ollama(dom_chunks, parse_description)
        st.write(parsed_results)



