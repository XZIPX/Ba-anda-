from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from langchain.chains import LLMChain
import streamlit as st

load_dotenv(find_dotenv())


def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)[0]["generated_text"]
    print(text)
    return text


def text2story(scenario):
    template = f"""
    You are story teller;
    You can generate a short story based on a simple narrative, the story should be no more than 20 words;
    CONTEXT: {scenario}
    STORY:
    """

    prompt = PromptTemplate(template=template, input_variables=["question"])

    story_llm = LLMChain(prompt=prompt,
                         llm=HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta",
                                            model_kwargs={"temperature": 0.8,
                                                          "max_length": 64}), verbose=True)

    story = story_llm.predict(scenario=scenario,
                              temperature=0.8,
                              max_length=64,
                              end_sequence="END OF STORY")
    clean_story = story.strip(" END OF STORY")
    print(clean_story)
    return clean_story


def main():
    st.set_page_config(page_title="Baıandaý", page_icon="✨")

    st.header("✨Baıandaý✨: create your story")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        scenario = img2text(uploaded_file.name)
        story = text2story(scenario)
        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)


if __name__ == '__main__':
    main()
