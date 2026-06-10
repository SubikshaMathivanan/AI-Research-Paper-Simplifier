import streamlit as st

from utils.pdf_reader import read_pdf
from utils.summarizer import generate_summary
from utils.keywords import extract_keywords
from utils.viva import generate_viva_questions
from utils.beginner_explainer import explain_for_beginner
from utils.difficulty import difficulty_analysis
from utils.paper_chat import chat_with_paper

st.set_page_config(
    page_title="AI Research Paper Simplifier",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Research Paper Simplifier")
st.write("Upload a research paper and get AI-powered insights.")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    with st.spinner("Reading PDF..."):
        text = read_pdf(uploaded_file)

    st.success("PDF Uploaded Successfully!")

    st.write("Characters in PDF:", len(text))

    with st.spinner("Generating Summary..."):
        summary = generate_summary(text)

    with st.spinner("Extracting Keywords..."):
        keywords = extract_keywords(text)

    with st.spinner("Generating Viva Questions..."):
        viva_questions = generate_viva_questions(text)

    with st.spinner("Generating Beginner Explanation..."):
        beginner_explanation = explain_for_beginner(text)

    with st.spinner("Analyzing Difficulty..."):
        difficulty = difficulty_analysis(text)

    st.divider()

    st.subheader("📌 Summary")
    st.write(summary)

    st.divider()

    st.subheader("🔑 Keywords")

    keyword_list = [keyword for keyword, score in keywords]

    st.write(", ".join(keyword_list))

    st.divider()

    st.subheader("🎓 Viva Questions")

    if isinstance(viva_questions, list):
        for q in viva_questions:
            st.markdown(f"- {q}")
    else:
        st.write(viva_questions)

    st.divider()

    st.subheader("📖 Beginner Explanation")
    st.write(beginner_explanation)

    st.divider()

    st.subheader("📊 Difficulty Analysis")
    st.write(difficulty)

    st.divider()

    st.subheader("💬 Chat With Research Paper")

    user_question = st.text_input(
        "Ask anything about the paper"
    )

    if user_question:

        with st.spinner("Thinking..."):

            answer = chat_with_paper(
                text,
                user_question
            )

        st.write(answer)