# AI-Driven Summaries: Never Miss a Meeting Detail Again

This application uses OpenAI's GPT-4 to generate summaries of team meeting recordings, helping you capture the essential points without having to go through the entire recording.

## Prerequisites

### OpenAI API Key

To run this application, you'll need an API key from OpenAI. If you don't have one, you can obtain it by signing up on the [OpenAI platform](https://beta.openai.com/signup/).

Once you have your API key:

1. Create a directory named `apikeys` in the root of the project.
2. Inside the `apikeys` directory, create a file named `openaiapikey.txt`.
3. Paste your OpenAI API key into the `openaiapikey.txt` file and save it.

**Note**: Please ensure you keep your API key confidential. Do not share, publish, or expose it in any public repositories or platforms. The provided setup ensures that the API key remains local and is not pushed to the GitHub repository.

## Installation

1. Clone the repository:

    git clone https://github.com/lancerique/AIDrivenSummaries.git

2. Navigate to the project directory:
  ```
  source myenv/bin/activate
  ```

3. Create a virtual environment:
   
  ```
  python -m venv myenv

  ```
   

   
4. Activate the virtual environment:
- On Windows:
  ```
  .\myenv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source myenv/bin/activate
  ```
5. Install the required packages:
   
  ```
  pip install -r requirements.txt
  ```


## Running the Application

1. Start the Streamlit app:
  ```
  streamlit run app.py
  ```
2. Open your web browser and go to the following URL:
  ```
  http://localhost:8501
  ```

  
## Contributing

If you have any suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Created by [@Lancerique](https://github.com/lancerique)
- [LinkedIn Profile](https://www.linkedin.com/in/nikhilmehta-coe/)

