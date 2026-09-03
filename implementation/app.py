import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Crop Disease Diagnosis",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #173b2c;
        margin-top: 30px;
    }

    .subtitle {
        text-align: center;
        font-size: 19px;
        color: #667085;
        margin-bottom: 40px;
    }

    .feature {
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        background: #f8fafc;
        min-height: 180px;
    }

    .footer {
        text-align: center;
        color: #667085;
        margin-top: 50px;
        padding: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 🌿 CropDiseaseAI"
    )

    st.markdown("---")

    st.write(
        """
        AI-powered crop disease diagnosis
        using multimodal image analysis.
        """
    )

    st.markdown("---")

    st.info(
        "Select **Diagnosis** from the sidebar "
        "to upload and analyze a crop image."
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🌿 AI Crop Disease Diagnosis'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Multimodal AI-based crop disease detection '
    'and localized treatment recommendation'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.markdown(
    "## 🌱 Intelligent Crop Health Analysis"
)

st.write(
    """
    CropDiseaseAI is an AI-powered agricultural
    assistance system that analyzes uploaded crop
    images and provides possible disease identification,
    visual symptom analysis, severity assessment,
    treatment guidance and preventive recommendations.
    """
)


# ============================================================
# FEATURES
# ============================================================

st.markdown(
    "## 🚀 Key Features"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="feature">

        ### 📷 Image Analysis

        Upload crop leaf, fruit or plant images
        directly through the application.

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="feature">

        ### 🧠 Multimodal AI

        Analyze the actual uploaded image
        using Gemini multimodal AI.

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="feature">

        ### 💊 Management Guidance

        Receive treatment, prevention and
        monitoring recommendations.

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SUPPORTED CROPS
# ============================================================

st.markdown(
    "## 🌾 Supported Crops"
)

st.write(
    """
    Tomato • Potato • Apple • Corn • Grape • Rice •
    Wheat • Cotton • Mango • Banana • Chilli •
    Pepper • Brinjal • Other crops
    """
)


# ============================================================
# SYSTEM WORKFLOW
# ============================================================

st.markdown(
    "## ⚙️ System Workflow"
)

st.markdown(
    """
    **1. Select Crop** →  
    **2. Enter Location and Season** →  
    **3. Enter Farmer Query** →  
    **4. Upload Crop Image** →  
    **5. Start AI Disease Detection** →  
    **6. View Diagnosis and Treatment**
    """
)


# ============================================================
# START MESSAGE
# ============================================================

st.markdown(
    "## 🔬 Start Diagnosis"
)

st.success(
    "Go to **Diagnosis** in the sidebar to begin."
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🌿 <b>CropDiseaseAI</b><br>
    AI-Based Crop Disease Diagnosis and
    Localized Treatment Recommendation

    </div>
    """,
    unsafe_allow_html=True
)