# Baıandaý

Baıandaý is a creative project that blends the power of machine learning with the art of storytelling. This project utilizes two models: one for detecting objects in an image and another, a Large Language Model (LLM), for generating a story based on the detected scenario. It offers a unique way to transform simple images into engaging narratives.

## Features

- **Image to Text Conversion**: Converts uploaded images into descriptive text using a state-of-the-art image captioning model.
- **Text to Story Transformation**: Transforms the descriptive text into a concise, imaginative story with a limit of 20 words.
- **Streamlit Interface**: Provides an easy-to-use web interface for uploading images and displaying the generated stories.

## How It Works

1. Upload an image through the Streamlit interface.
2. The image is processed by the `image-to-text` pipeline to generate a descriptive text of the scene.
3. This text is then used as input for a Large Language Model, which crafts a short story based on the given context.

## Setup

### Prerequisites

- Python 3.x
- Pip

### Installation

Clone the repository and install the required packages:
```bash
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
```

### Environment Variables
Create a .env file at the root of your project directory and populate it with the necessary API keys and model names. For example:
```bash
.env content
API_KEY=<your_api_key_here>
```
### Running the Application
To run the application, execute the following command in your terminal:
streamlit run app.py

### Usage
After launching the application, follow these steps:

1. Click the "Choose an image..." button to upload your image.
2. Wait for the image to be processed and the story to be generated.
3. Expand the "scenario" and "story" sections to view the results.
### Dependencies
 - dotenv: For managing environment variables.
 - transformers: Provides access to the image-to-text model.
 - langchain: Utilized for creating and managing the LLM chain for story generation.
 - streamlit: For creating the web interface.
### Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

### License
This project is open-source and available under the MIT License.

### Acknowledgments
- Salesforce BLIP model for image captioning.
- Hugging Face for the LLM model and infrastructure.
- Streamlit for the web interface framework.
Transform your images into stories with Baıandaý and explore the limitless possibilities of AI-driven storytelling.
