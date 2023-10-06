import streamlit as st

# Function to summarize articles based on the provided URLs
def summarize_articles(urls):
    # Replace this with your actual text extraction and summarization logic
    summaries = []
    for url in urls:
        # Your text extraction and summarization code here
        summary = f"Summary of {url}"
        summaries.append(summary)
    return summaries

# Streamlit app
def main():
    st.title("Article Summarizer")

    # Input for the number of articles to summarize
    num_articles = st.number_input("How many articles do you want to summarize?", min_value=1, value=1)

    # Text boxes for entering article URLs
    article_urls = []
    for i in range(num_articles):
        article_url = st.text_input(f"Enter URL for Article {i + 1}")
        article_urls.append(article_url)

    # Submit button
    if st.button("Summarize"):
        if not all(article_urls):
            st.warning("Please enter URLs for all articles.")
        else:
            # Call the summarization function
            summaries = summarize_articles(article_urls)
            st.subheader("Summaries:")
            for i, summary in enumerate(summaries):
                st.write(f"Article {i + 1} Summary: {summary}")

if __name__ == "__main__":
    main()