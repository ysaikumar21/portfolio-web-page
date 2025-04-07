import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Saikumar Yaramala | Data Scientist",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Custom CSS styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Function for image handling
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


# Main layout
def main():
    # Header Section
    col1, col2 = st.columns([1, 3], gap="large")

    with col1:
        # Profile picture - replace with your actual image
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{img_to_bytes('profile.png')}" 
                alt="Saikumar Yaramala" width="200" style="border-radius: 50%; border: 4px solid #2E86AB; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.title("Saikumar Yaramala")
        st.markdown("""
        <div style="background-color: #2E86AB; padding: 10px; border-radius: 5px;">
            <h3 style="color: white; margin: 0;">Data Scientist | AI/ML Engineer | Data Analyst</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
        <div style="margin-top: 10px;">
            <span style="font-size: 16px;">📧 saikumar76y@gmail.com</span><br>
            <span style="font-size: 16px;">📱 +91 6302158985</span><br>
            <span style="font-size: 16px;">📍 Ongole, Andhra Pradesh</span>
        </div>
        """, unsafe_allow_html=True)

        # Social links with icons
        st.markdown("""
        <div style="margin-top: 15px;">
            <a href="https://www.linkedin.com/in/saikumar-y-853666317/" target="_blank" style="margin-right: 15px;"><img src="https://img.icons8.com/color/48/000000/linkedin.png" width="30" title="LinkedIn"/></a>
            <a href="https://github.com/ysaikumar21" target="_blank" style="margin-right: 15px;"><img src="https://img.icons8.com/fluent/48/000000/github.png" width="30" title="GitHub"/></a>
            <a href="mailto:saikumar76y@gmail.com" style="margin-right: 15px;"><img src="https://img.icons8.com/color/48/000000/gmail-new.png" width="30" title="Email"/></a>
        </div>
        """, unsafe_allow_html=True)

    # Profile Summary Section
    st.markdown("---")
    st.header("👨‍💻 Professional Profile")
    st.markdown("""
    <div style="background-color: #F8F9FA; padding: 15px; border-radius: 5px; border-left: 4px solid #2E86AB;">
        Results-driven Data Science professional with expertise in machine learning, deep learning, and data analysis. Skilled in developing end-to-end AI solutions and transforming complex datasets into actionable insights. Proficient in Python, SQL, TensorFlow, and data visualization tools with experience in both predictive modeling and business intelligence.
    </div>
    """, unsafe_allow_html=True)

    # Work Experience Section
    st.markdown("---")
    st.header("💼 Professional Experience")

    with st.expander("**Data Science with AI Intern** at Social Tek, Hyderabad (Aug 2024 - Present)", expanded=True):
        st.markdown("""
        <div style="padding-left: 20px;">
            <ul style="list-style-type: disc;">
                <li>Applied machine learning and statistical modelling techniques using Python and SQL to extract actionable insights from complex datasets</li>
                <li>Gained hands-on experience in ETL processes, predictive analytics, and feature engineering to enhance model performance and data quality</li>
                <li>Created interactive dashboards and visualizations using Power BI and Tableau to support data-driven decision-making</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Skills Section with tabs
    st.markdown("---")
    st.header("🛠️ Technical Skills")

    tab1, tab2, tab3 = st.tabs(["Programming & Tools", "Machine Learning", "Data Management"])

    with tab1:
        st.subheader("Programming Languages")
        st.markdown("""
        - **Python**: Pandas, NumPy, Scikit-learn, Streamlit
        - **SQL**: MySQL, Query optimization
        - **Version Control**: Git, GitHub
        """)

    with tab2:
        st.subheader("Machine Learning & AI")
        st.markdown("""
        - Predictive & classification algorithms
        - Deep Learning (ANN, CNN)
        - TensorFlow, Keras
        - Model evaluation & optimization
        """)

    with tab3:
        st.subheader("Data Management & Analysis")
        st.markdown("""
        - ETL processes
        - Feature Engineering
        - Exploratory Data Analysis
        - Data Visualization (Power BI, Tableau, Matplotlib)
        """)

    # Projects Section - Data Science
    st.markdown("---")
    st.header("🚀 Data Science Projects")

    st.markdown("""
    <style>
        .project-card {
            background-color: #F8F9FA;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            border-left: 4px solid #2E86AB;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .project-title {
            color: #2E86AB;
            margin-top: 0;
        }
        .project-links a {
            margin-right: 15px;
            color: #2E86AB;
            text-decoration: none;
            font-weight: 500;
        }
        .project-links a:hover {
            text-decoration: underline;
        }
        .tech-badge {
            display: inline-block;
            background-color: #e0f2fe;
            color: #0369a1;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
        }
        .section-badge {
            display: inline-block;
            background-color: #2E86AB;
            color: white;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 14px;
            margin-bottom: 15px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Data Science Project 1
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3 class="project-title">AI-Powered Weapons Classification (Custom CNN & VGG19)</h3>
            <div class="project-links">
                <a href="https://ai-powered-weapons-classification-with-custom-cnn-vgg19-hmfjcf.streamlit.app/" target="_blank">🌐 Live Demo</a>
                <a href="https://github.com/ysaikumar21/AI-Powered-Weapons-Classification-with-Custom-CNN-VGG19" target="_blank">💻 GitHub Repo</a>
            </div>
            <p>Deep learning system to classify weapon types from images with comparison between custom CNN and VGG19 transfer learning.</p>
            <div>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">TensorFlow</span>
                <span class="tech-badge">Keras</span>
                <span class="tech-badge">OpenCV</span>
                <span class="tech-badge">Streamlit</span>
            </div>
            <ul style="margin-bottom: 0;">
                <li>Developed custom CNN architecture from scratch</li>
                <li>Implemented transfer learning with VGG19</li>
                <li>Achieved 94.5% accuracy on test dataset</li>
                <li>Created GradCAM visualizations for model interpretability</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Data Science Project 2
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3 class="project-title">Financial Risk Prediction (Credit Card Default)</h3>
            <div class="project-links">
                <a href="https://financial-risk-prediction-credit-card-default-classification.streamlit.app/" target="_blank">🌐 Live Demo</a>
                <a href="https://github.com/ysaikumar21/Financial-Risk-Prediction-Credit-Card-Default-Classification" target="_blank">💻 GitHub Repo</a>
            </div>
            <p>Machine learning system to predict credit card payment defaults with feature importance analysis.</p>
            <div>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">Scikit-learn</span>
                <span class="tech-badge">XGBoost</span>
                <span class="tech-badge">Pandas</span>
                <span class="tech-badge">SHAP</span>
            </div>
            <ul style="margin-bottom: 0;">
                <li>Handled class imbalance using SMOTE and class weights</li>
                <li>Optimized XGBoost model with 89% recall score</li>
                <li>Created SHAP visualizations for explainable AI</li>
                <li>Developed risk score calculator for business use</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Data Science Project 3
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3 class="project-title">Diamond Price Prediction (Machine Learning)</h3>
            <div class="project-links">
                <a href="https://predicting-diamond-prices-using-machine-learning.streamlit.app/" target="_blank">🌐 Live Demo</a>
                <a href="https://github.com/ysaikumar21/Predicting-Diamond-Prices-Using-Machine-Learning" target="_blank">💻 GitHub Repo</a>
            </div>
            <p>Regression models to predict diamond prices based on features with comprehensive EDA.</p>
            <div>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">Scikit-learn</span>
                <span class="tech-badge">Seaborn</span>
                <span class="tech-badge">Plotly</span>
                <span class="tech-badge">Streamlit</span>
            </div>
            <ul style="margin-bottom: 0;">
                <li>Analyzed 50,000+ diamonds dataset with 10+ features</li>
                <li>Developed ensemble model with 97% R-squared score</li>
                <li>Created interactive price calculator with sliders</li>
                <li>Visualized price distributions and correlations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Data Science Project 4
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3 class="project-title">NLP Chatbot for Educational Services</h3>
            <div class="project-links">
                <a href="https://ai-chatbot-app-saikumar.streamlit.app/" target="_blank">🌐 Live Demo</a>
                <a href="https://github.com/ysaikumar21/ai-chatbot-streamlit" target="_blank">💻 GitHub Repo</a>
            </div>
            <p>Natural Language Processing chatbot for answering educational queries with context awareness.</p>
            <div>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">NLTK</span>
                <span class="tech-badge">Transformers</span>
                <span class="tech-badge">Streamlit</span>
                <span class="tech-badge">HuggingFace</span>
            </div>
            <ul style="margin-bottom: 0;">
                <li>Implemented intent recognition and entity extraction</li>
                <li>Integrated with educational knowledge base</li>
                <li>Designed conversational flow with fallback mechanisms</li>
                <li>Deployed as interactive web application</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Projects Section - Data Analysis
    st.markdown("---")
    st.header("📊 Data Analysis Projects")
    st.markdown('<div class="section-badge">Business Intelligence & Analytics</div>', unsafe_allow_html=True)

    # Data Analysis Project 1
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3 class="project-title">Retail Sales Insights Dashboard</h3>
            <div class="project-links">
                <a href="https://github.com/ysaikumar21/-Retail-Sales-Insights-Dashboard" target="_blank">💻 GitHub Repo</a>
            </div>
            <p>Comprehensive sales analytics dashboard providing insights into retail performance metrics.</p>
            <div>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">Pandas</span>
                <span class="tech-badge">Plotly</span>
                <span class="tech-badge">Power BI</span>
                <span class="tech-badge">SQL</span>
            </div>
            <ul style="margin-bottom: 0;">
                <li>Analyzed 2+ years of sales data across multiple stores</li>
                <li>Identified top-performing products and seasonal trends</li>
                <li>Created interactive visualizations of sales KPIs</li>
                <li>Developed customer segmentation models</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Data Analysis Project 2
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3 class="project-title">Walmart Sales Analysis</h3>
            <div class="project-links">
                <a href="https://github.com/ysaikumar21/Walmart-Sales-Analysis" target="_blank">💻 GitHub Repo</a>
            </div>
            <p>Large-scale retail sales analysis to identify patterns and optimize inventory.</p>
            <div>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">Pandas</span>
                <span class="tech-badge">Matplotlib</span>
                <span class="tech-badge">Seaborn</span>
                <span class="tech-badge">Tableau</span>
            </div>
            <ul style="margin-bottom: 0;">
                <li>Processed and cleaned 500,000+ sales records</li>
                <li>Identified key drivers of sales performance</li>
                <li>Created predictive models for inventory demand</li>
                <li>Developed Tableau dashboards for executive reporting</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Data Science Project 5
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h3 class="project-title">Smart Water Quality Monitoring with AI</h3>
            <div class="project-links">
                <a href="https://water-quality-check-index-7.streamlit.app/" target="_blank">🌐 Live Demo</a>
                <a href="https://github.com/ysaikumar21/your-repo-name" target="_blank">💻 GitHub Repo</a>
            </div>
            <p>AI system for real-time water quality assessment with predictive contamination detection.</p>
            <div>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">TensorFlow</span>
                <span class="tech-badge">Pandas</span>
                <span class="tech-badge">Streamlit</span>
                <span class="tech-badge">Plotly</span>
            </div>
            <ul style="margin-bottom: 0;">
                <li>Integrated with IoT sensor data streams</li>
                <li>Developed contamination prediction models</li>
                <li>Created interactive monitoring dashboard</li>
                <li>Implemented alert notification system</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Education & Certifications
    st.markdown("---")
    st.header("🎓 Education & Certifications")

    edu_col, cert_col = st.columns(2)

    with edu_col:
        st.subheader("Education")
        st.markdown("""
        <div style="background-color: #F8F9FA; padding: 15px; border-radius: 5px;">
            <h4 style="margin-bottom: 5px;">Bachelor of Engineering (B.E.)</h4>
            <p style="margin: 0;">Electronics and Communication Engineering</p>
            <p style="margin: 0; color: #555;">Prakasam Engineering College, Kandukur</p>
            <p style="margin: 0; color: #555;">Graduated: 2024</p>
        </div>
        """, unsafe_allow_html=True)

    with cert_col:
        st.subheader("Certifications")
        with st.expander("6-Month Internship in Data Science with AI"):
            st.write("""
            - Gained hands-on experience in machine learning, deep learning, and predictive analytics
            - Used Python, TensorFlow, and Scikit-learn to develop data-driven solutions
            - Applied feature engineering and model optimization techniques
            """)

        with st.expander("Certification in Data Science with AI Using Python"):
            st.write("""
            - Proficient in data analysis, visualization, and statistical modelling
            - Built and deployed machine learning models
            - Tools: Pandas, NumPy, Matplotlib, Power BI
            """)

    # Contact Form
    st.markdown("---")
    st.header("📬 Get In Touch")

    contact_form = """
    <form action="https://formsubmit.co/saikumar76y@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://your-portfolio.streamlit.app/thankyou">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 4px;">
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 4px;">
        <textarea name="message" placeholder="Your message" required style="width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #ddd; border-radius: 4px; height: 100px;"></textarea>
        <button type="submit" style="background-color: #2E86AB; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Send Message</button>
    </form>
    """

    left_col, right_col = st.columns(2)

    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_col:
        st.markdown("""
        <div style="margin-top: 20px;">
            <h4>Connect with me:</h4>
            <p>📧 <a href="mailto:saikumar76y@gmail.com">saikumar76y@gmail.com</a></p>
            <p>📱 +91 6302158985</p>
            <p>🔗 <a href="https://www.linkedin.com/in/saikumar-y-853666317/" target="_blank">LinkedIn Profile</a></p>
            <p>💻 <a href="https://github.com/ysaikumar21" target="_blank">GitHub Profile</a></p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()