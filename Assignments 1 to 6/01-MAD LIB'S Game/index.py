import streamlit as st

# Set up the Streamlit app
st.set_page_config(
    page_title="Mad Libs Game 🎮",
    page_icon="✨",
    layout="centered"
)

# Custom CSS for a beautiful design
st.markdown("""
<style>
    .stTextInput input {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("✨ Mad Libs Game 🎮")
st.write("Welcome to the **Mad Libs** game! Fill in the blanks below, and we'll generate a **funny and creative** story for you. Let's get started!")

# Input fields for the Mad Libs
st.subheader("📝 Fill in the Blanks")
col1, col2 = st.columns(2)

with col1:
    adjective1 = st.text_input("Enter an adjective (e.g., silly, shiny):")
    noun1 = st.text_input("Enter a noun (e.g., dragon, pizza):")
    verb1 = st.text_input("Enter a verb (past tense, e.g., danced, jumped):")

with col2:
    adverb1 = st.text_input("Enter an adverb (e.g., quickly, happily):")
    place = st.text_input("Enter a place (e.g., Paris, the moon):")
    animal = st.text_input("Enter an animal (e.g., cat, unicorn):")

emotion = st.text_input("Enter an emotion (e.g., excited, confused):")

# Generate the story when the button is clicked
if st.button("✨ Generate Story ✨"):
    if adjective1 and noun1 and verb1 and adverb1 and place and animal and emotion:
        story = f"""
        Once upon a time, in a **{adjective1}** land, there was a **{noun1}** who loved to **{verb1} {adverb1}**. 
        One day, they decided to visit **{place}**. On their way, they encountered a **{animal}** who was feeling **{emotion}**. 
        The **{noun1}** and the **{animal}** became best friends and lived happily ever after! 🎉
        """
        st.subheader("📖 Your Mad Libs Story:")
        st.success(story)
        st.balloons()  # Add some fun animations!
    else:
        st.error("Please fill in all the fields to generate the story! 🚨")

# Add a footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Enjoy the game! 🎮")