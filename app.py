# app.py
import streamlit as st
import os
import datetime
import textwrap
from src.summarizer import gpt4_completion, open_file, save_file

def main():
    st.title("AI-Driven Summaries")
    st.write("Paste your meeting text below to get a summarized version.")

    # Text area for user input
    user_input = st.text_area("Enter/Paste your text here:")

    # Button to trigger summarization
    if st.button("Summarize"):
        # Get the current date and time
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Rename the previous input file
        if os.path.exists("inputs/input.txt"):
            os.rename("inputs/input.txt", f"inputs/input_{current_datetime}.txt")

        # Save user input to input.txt
        save_file(user_input, "inputs/input.txt")

        # Chunk the user input
        chunks = textwrap.wrap(user_input, 5000)  # Adjust the number as needed
        summarized_chunks = []

        # Initialize the progress bar
        progress_bar = st.progress(0)
        for index, chunk in enumerate(chunks):
            # Read the prompt and replace placeholder with chunk
            prompt = open_file('prompts/prompt.txt').replace('<<SUMMARY>>', chunk)
            
            # Run the summarizer for the chunk
            summary = gpt4_completion(prompt)
            summarized_chunks.append(summary)

            # Update the progress bar
            progress_value = (index + 1) / len(chunks)
            progress_bar.progress(progress_value)

        # Combine the summarized chunks
        final_summary = '\n\n'.join(summarized_chunks)

        # Save the summarized output to output_<current_datetime>.txt
        save_file(final_summary, f"outputs/output_{current_datetime}.txt")

        # Display the summarized output
        st.subheader("Summarized Text:")
        st.write(final_summary)

        # Provide a download button for the output file
        output_filepath = f"outputs/output_{current_datetime}.txt"
        with open(output_filepath, 'r', encoding='utf-8') as file:
            file_data = file.read()
            st.download_button(
                label="Download Summarized Text",
                data=file_data,
                file_name=f"output_{current_datetime}.txt",
                mime="text/plain"
            )

    # Add personal branding and LinkedIn link at the bottom
    st.markdown("---")
    st.markdown(
        "Created by [@Lancerique](https://www.linkedin.com/in/nikhilmehta-coe/)"
    )

if __name__ == "__main__":
    main()
