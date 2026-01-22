import streamlit as st

st.set_page_config(page_title="💖 Valentine?", layout="centered")

# ----------------- STATE -----------------
if "yes_scale" not in st.session_state:
    st.session_state.yes_scale = 1.0

if "no_scale" not in st.session_state:
    st.session_state.no_scale = 1.0

if "accepted" not in st.session_state:
    st.session_state.accepted = False

# ----------------- CALLBACKS -----------------
def click_yes():
    st.session_state.accepted = True

def click_no():
    st.session_state.no_scale *= 0.7
    st.session_state.yes_scale += 0.25

# ----------------- MESSAGE -----------------
VALENTINE_MESSAGE = """
💘 Congratulations on being tied to me one more year. 💘  

You make my world brighter every day.  
I’m so lucky to have you.  
I love you ❤️
"""

# ----------------- CSS -----------------
st.markdown(
    """
    <style>
    body {
        background-color: #fff5f8;
    }

    .stApp {
        background-image:
            radial-gradient(circle at 20% 20%, rgba(255,192,203,0.15) 10%, transparent 11%),
            radial-gradient(circle at 80% 30%, rgba(255,192,203,0.15) 10%, transparent 11%),
            radial-gradient(circle at 50% 70%, rgba(255,192,203,0.15) 10%, transparent 11%);
        background-size: 200px 200px;
    }

    .center {
        text-align: center;
    }

    /* Floating hearts container */
    .hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
    }

    .heart {
        position: absolute;
        bottom: -10%;
        width: 20px;
        height: 20px;
        background-color: rgba(255, 105, 180, 0.6);
        transform: rotate(45deg);
        animation: floatUp 12s linear infinite;
    }

    .heart::before,
    .heart::after {
        content: "";
        position: absolute;
        width: 20px;
        height: 20px;
        background-color: rgba(255, 105, 180, 0.6);
        border-radius: 50%;
    }

    .heart::before {
        top: -10px;
        left: 0;
    }

    .heart::after {
        left: -10px;
        top: 0;
    }

    @keyframes floatUp {
        0% {
            transform: translateY(0) rotate(45deg);
            opacity: 0;
        }
        10% {
            opacity: 0.6;
        }
        100% {
            transform: translateY(-120vh) rotate(45deg);
            opacity: 0;
        }
    }

    button {
        transition: transform 0.2s ease;
    }

    <div class="hearts">
        <div class="heart" style="left:10%; animation-delay:0s;"></div>
        <div class="heart" style="left:25%; animation-delay:2s;"></div>
        <div class="heart" style="left:40%; animation-delay:4s;"></div>
        <div class="heart" style="left:55%; animation-delay:1s;"></div>
        <div class="heart" style="left:70%; animation-delay:3s;"></div>
        <div class="heart" style="left:85%; animation-delay:5s;"></div>
    </div>
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- UI -----------------
st.markdown("<div class='center'>", unsafe_allow_html=True)

if not st.session_state.accepted:
    st.markdown("## 💖 Will you be my Valentine? 💖")

    col1, col2 = st.columns(2)

    with col1:
        st.button("YES 💘", on_click=click_yes)

    with col2:
        st.button("No 🙃", on_click=click_no)

    # Apply scaling AFTER buttons exist
    st.markdown(
        f"""
        <style>
        button:has(span:contains("YES")) {{
            transform: scale({st.session_state.yes_scale});
        }}

        button:has(span:contains("No")) {{
            transform: scale({st.session_state.no_scale});
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

else:
    st.balloons()
    st.markdown("## 💕 YOU DIDN'T HAVE AN OPTION 💕")
    st.markdown(
        f"""
        <div style="
            background-color: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(255,105,180,0.3);
            font-size: 22px;
        ">
        {VALENTINE_MESSAGE}
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)