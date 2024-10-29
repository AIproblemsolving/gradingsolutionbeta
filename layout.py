import streamlit as st

def create_header():
    st.markdown("""
        <style>
        .header {
            background-color: #0D1824;
            padding: 20px;
            text-align: center;
            color: white;
            font-size: 64px;
            font-weight: bold;
            width: 100vw;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-top: 15px; /* Tiny space above the text */
        }
        .stApp {
            padding-top: 80px;
        }
        </style>
        <div class="header">
            Grading Assistant (Beta)
        </div>
        """, unsafe_allow_html=True)

def set_background():
    st.markdown("""
        <style>
        .stApp {
            background-color: #1D2B3A;
        }
        </style>
        """, unsafe_allow_html=True)


def emptylines():
    st.write("")
    st.write("")
    st.write("")

def hide_st():
    hide_st = """
    <style>
        #MainMenu {visibility: hidden;}
        #stDecoration {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_st, unsafe_allow_html=True)

def hide_elements():
    hide_elements_script = """
    <style>
        #MainMenu {display: none;}
        #stDecoration {display: none;}
        footer {display: none;}
        header {display: none;}
        img {display: none;}
        a {
            pointer-events: none;
            cursor: default;
            color: inherit;
        }
    </style>
    <script>
        // Use a MutationObserver to detect and hide specific elements dynamically
        const targetNode = document.body;
        const observerOptions = {
            childList: true,
            subtree: true
        };
        
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                const profileContainer = document.querySelectorAll('div[class*="profileContainer"], div[class*="profilePreview"]');
                profileContainer.forEach((element) => {
                    element.style.display = 'none';
                });
            });
        });

        observer.observe(targetNode, observerOptions);
    </script>
    """
    st.markdown(hide_elements_script, unsafe_allow_html=True)

hide_elements()

