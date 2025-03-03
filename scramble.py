import streamlit as st
import random

# Word list
WORDS = ["python", "streamlit", "machine", "learning", "developer", "keyboard", "internet", "science", "programming", "engineer"]

def scramble_word(word):
    return "".join(random.sample(word, len(word)))

if "score" not in st.session_state:
    st.session_state.score = 0
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)
    st.session_state.scrambled = scramble_word(st.session_state.word)
if "message" not in st.session_state:
    st.session_state.message = ""

def check_answer():
    if st.session_state.guess.lower() == st.session_state.word:
        st.session_state.score += 1
        st.session_state.message = "🎉 Correct! Next word..."
        st.session_state.word = random.choice(WORDS)
        st.session_state.scrambled = scramble_word(st.session_state.word)
    else:
        st.session_state.message = "❌ Incorrect! Try again."

def skip_word():
    st.session_state.message = f"😅 Skipped! The word was: {st.session_state.word}"  
    st.session_state.word = random.choice(WORDS)
    st.session_state.scrambled = scramble_word(st.session_state.word)

st.title("🔠 Word Scramble Game!")
st.write(f"**Score:** {st.session_state.score}")
st.write(f"Unscramble this word: **{st.session_state.scrambled}**")

guess = st.text_input("Your Guess:", key="guess")
col1, col2 = st.columns(2)
with col1:
    st.button("Submit", on_click=check_answer)
with col2:
    st.button("Skip", on_click=skip_word)

st.write(st.session_state.message)
