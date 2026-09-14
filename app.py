import streamlit as st
from pathlib import Path

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Aruneshwar Thakur | Finance & Investment Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f5f7f9;
    color: #172033;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 4.5rem;
    line-height: 0.98;
    color: #172033;
    margin-bottom: 0.8rem;
}

.hero-role {
    font-size: 1.55rem;
    font-weight: 600;
    color: #394861;
    margin-bottom: 0.8rem;
}

.eyebrow {
    color: #9a7134;
    font-size: 0.78rem;
    letter-spacing: 0.25rem;
    font-weight: 600;
    text-transform: uppercase;
}

.subtitle {
    color: #718096;
    letter-spacing: 0.18rem;
    font-size: 0.78rem;
    text-transform: uppercase;
}

.body-text {
    font-size: 1.08rem;
    line-height: 1.75;
    color: #566176;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    color: #172033;
    margin-bottom: 0.5rem;
}

.section-note {
    color: #718096;
    margin-bottom: 2rem;
}

.info-card {
    background: white;
    border: 1px solid #dce1e7;
    border-radius: 12px;
    padding: 1.4rem;
    margin-bottom: 1rem;
}

.project-card {
    background: white;
    border: 1px solid #dce1e7;
    border-radius: 14px;
    padding: 1.6rem;
    min-height: 250px;
    margin-bottom: 1rem;
}

.project-number {
    color: #9a7134;
    font-size: 0.75rem;
    letter-spacing: 0.18rem;
    font-weight: 700;
}

.project-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.55rem;
    color: #172033;
    margin: 0.5rem 0;
}

.tag {
    display: inline-block;
    padding: 0.35rem 0.7rem;
    border: 1px solid #d5dae1;
    border-radius: 999px;
    color: #5e697b;
    font-size: 0.75rem;
    margin: 0.2rem;
}

.metric {
    background: #172033;
    color: white;
    border-radius: 12px;
    padding: 1.2rem;
    text-align: center;
}

.metric-value {
    font-size: 1.7rem;
    font-weight: 700;
}

.metric-label {
    color: #cbd2dc;
    font-size: 0.78rem;
}

.footer {
    border-top: 1px solid #dce1e7;
    padding-top: 2rem;
    margin-top: 4rem;
    color: #718096;
    font-size: 0.85rem;
}

a {
    color: #9a7134 !important;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------
projects = [
    {
        "number": "01",
        "title": "Arizon Network",
        "subtitle": "Strategic Financial & Market Intelligence for Business Growth",
        "category": "INTERNSHIP · FINANCIAL ANALYSIS · MARKET INTELLIGENCE",
        "purpose": "Support business growth through structured market intelligence, company research and financial analysis.",
        "process": "Developed a market intelligence database covering 50 companies across multiple sectors; conducted company profiling and market research; identified potential collaboration prospects; and contributed to financial diagnostics covering financial statements, ratio analysis, DuPont analysis and risk assessment.",
        "outcome": "Built a 50-company intelligence database and identified 26 potential collaboration prospects. The internship also produced financial diagnostics and contributed to an AI-assisted interview evaluation solution.",
        "role": "Finance Analyst Intern",
        "contribution": "Personally worked on company profiling, market research, financial analysis, prospect identification, lead-generation support and recruitment documentation. Also contributed to the HireU AI-assisted interview evaluation concept.",
        "evidence": "GitHub evidence repository link to be added after project files are uploaded.",
    },
    {
        "number": "02",
        "title": "JSW Energy",
        "subtitle": "Kutehr Hydro Project – Investment Analysis",
        "category": "INVESTMENT ANALYSIS · FINANCIAL MODELLING",
        "purpose": "Evaluate the investment attractiveness of the Kutehr hydro project using project-level financial analysis.",
        "process": "Analysed project economics, financing structure, cash flows, debt servicing and return indicators. Evaluated project IRR, equity IRR and DSCR alongside project risks to form an investment view.",
        "outcome": "The analysis indicated a cautious positive investment view, supported by project-level return and debt-service metrics.",
        "role": "Financial Analysis / Investment Research",
        "contribution": "Built the financial analysis and interpreted return, cash-flow and debt-service indicators to arrive at an investment conclusion.",
        "evidence": "GitHub evidence repository link to be added after project files are uploaded.",
    },
    {
        "number": "03",
        "title": "Virat Kohli Footwear",
        "subtitle": "Market Sizing, STP & Go-to-Market Strategy",
        "category": "BUSINESS STRATEGY · MARKET SIZING · STP",
        "purpose": "Assess the opportunity for a Virat Kohli-led footwear venture and determine how it could enter and compete in the Indian market.",
        "process": "Conducted market sizing using TAM, SAM and SOM; evaluated consumer segments; developed targeting and positioning; assessed pricing; and designed a phased go-to-market strategy.",
        "outcome": "Developed a structured market-entry recommendation covering target consumer, positioning, pricing and distribution strategy.",
        "role": "Market Research & Strategy Analyst",
        "contribution": "Conducted market sizing, segmentation, targeting and positioning analysis and translated findings into a market-entry strategy.",
        "evidence": "GitHub evidence repository link to be added after project files are uploaded.",
    },
    {
        "number": "04",
        "title": "Financial Markets",
        "subtitle": "Crisis Diversification & Portfolio Strategy",
        "category": "FINANCIAL MARKETS · PORTFOLIO ANALYSIS",
        "purpose": "Study diversification behaviour and portfolio implications across major market crisis periods.",
        "process": "Analysed market behaviour across crisis periods including COVID-19 and geopolitical events. Compared asset behaviour across equities, defence and oil-related exposure and examined volatility and connectedness.",
        "outcome": "Developed portfolio-level observations on diversification, volatility and the changing relationship between asset classes during stressed market conditions.",
        "role": "Financial Markets Research Analyst",
        "contribution": "Conducted market research, comparative analysis and portfolio interpretation across different crisis periods.",
        "evidence": "GitHub evidence repository link to be added after project files are uploaded.",
    },
    {
        "number": "05",
        "title": "MACD Technical Analysis",
        "subtitle": "Technical Analysis using Excel",
        "category": "TECHNICAL ANALYSIS · EXCEL",
        "purpose": "Apply the Moving Average Convergence Divergence (MACD) indicator to evaluate market price trends.",
        "process": "Prepared the MACD analysis in Excel using moving-average calculations, signal-line analysis and visual interpretation of indicator movements.",
        "outcome": "Created an Excel-based technical analysis demonstrating the application of MACD for interpreting market momentum and potential trend signals.",
        "role": "Financial Analytics Student",
        "contribution": "Built the Excel analysis and interpreted MACD movements using structured calculations and charts.",
        "evidence": "GitHub evidence repository link to be added after project files are uploaded.",
    },
]


# ---------------------------------------------------------
# HEADER / NAVIGATION
# ---------------------------------------------------------
st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center;
border-bottom:1px solid #dce1e7;padding-bottom:1rem;margin-bottom:2rem;">
<div>
<span style="font-weight:700;letter-spacing:.2rem;">A. THAKUR</span>
<span style="color:#9a7134;"> / FINANCE</span>
</div>
<div style="color:#718096;font-size:.8rem;letter-spacing:.12rem;">
PROFESSIONAL E-PORTFOLIO
</div>
</div>
""", unsafe_allow_html=True)

page = st.radio(
    "Navigation",
    ["Home", "Projects", "Skills & Tools", "Resume", "Contact"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")


# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------
if page == "Home":

    col1, col2 = st.columns([1.55, 1], gap="large")

    with col1:
        st.markdown('<div class="eyebrow">Portfolio Note · Ref 01</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Aruneshwar<br>Thakur</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-role">Finance & Investment Analyst</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="subtitle">PGDM (Finance) · Financial Analysis · Investment Research · Business Intelligence</div>',
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown(
            '<div class="body-text">I turn financial and market data into structured insights for investment evaluation, business decisions, and growth strategy.</div>',
            unsafe_allow_html=True
        )

        st.write("")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("View Projects", use_container_width=True):
                st.session_state["page"] = "Projects"
        with c2:
            st.link_button(
                "LinkedIn Profile",
                "https://www.linkedin.com/in/aruneshwar-thakur/",
                use_container_width=True
            )

    with col2:
        photo_path = Path("assets/profile_photo.jpg")
        if photo_path.exists():
            st.image(str(photo_path), use_container_width=True)
        else:
            st.markdown("""
            <div style="
            height:330px;
            border:1px solid #dce1e7;
            border-radius:50%;
            background:#e9edf2;
            display:flex;
            align-items:center;
            justify-content:center;
            color:#718096;
            text-align:center;">
            <div>
            <strong>Professional Headshot</strong><br>
            <small>Upload profile_photo.jpg<br>to assets/</small>
            </div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="eyebrow">Academic Credentials</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
    <b>PGDM — Finance</b> — Fortune Institute of International Business (FIIB), New Delhi
    <span style="color:#718096;"> · 2025–2027</span><br><br>
    <b>Bachelor of Arts</b> — University of Himachal Pradesh
    <span style="color:#718096;"> · 2020–2023</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Featured Work</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-note">Five selected projects demonstrating finance, investment analysis, business research and analytical capability.</div>',
        unsafe_allow_html=True
    )

    for p in projects[:3]:
        st.markdown(f"""
        <div class="project-card">
        <div class="project-number">{p["number"]} · {p["category"]}</div>
        <div class="project-title">{p["title"]}</div>
        <div style="color:#566176;margin-bottom:1rem;">{p["subtitle"]}</div>
        <div>{p["purpose"]}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-card">
    <b>Excel for Finance</b> — Coursera<br>
    <b>Financial Modeling & Valuation Analyst</b> — CFI<br>
    <b>Basics of Investment Banking</b> — Internshala
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------
elif page == "Projects":

    st.markdown('<div class="eyebrow">Selected Work · Evidence First</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-note">Each project follows the FIIB evidence structure: Purpose → Process → Outcome → My Role → My Contribution → Evidence.</div>',
        unsafe_allow_html=True
    )

    selected = st.selectbox(
        "Select a project",
        [f'{p["number"]} — {p["title"]}' for p in projects]
    )

    project = projects[[f'{p["number"]} — {p["title"]}' for p in projects].index(selected)]

    st.markdown(
        f'<div class="eyebrow">{project["number"]} · {project["category"]}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="section-title">{project["title"]}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="hero-role">{project["subtitle"]}</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Purpose")
        st.write(project["purpose"])

        st.markdown("### Process")
        st.write(project["process"])

        st.markdown("### Outcome")
        st.write(project["outcome"])

    with col2:
        st.markdown("### My Role")
        st.write(project["role"])

        st.markdown("### My Contribution")
        st.write(project["contribution"])

        st.markdown("### Evidence / Working Files")
        st.info(project["evidence"])

    st.markdown("---")

    if project["title"] == "Arizon Network":
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric"><div class="metric-value">50</div><div class="metric-label">COMPANIES RESEARCHED</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric"><div class="metric-value">26</div><div class="metric-label">PRIORITY PROSPECTS</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric"><div class="metric-value">7+</div><div class="metric-label">INDUSTRY SECTORS COVERED</div></div>', unsafe_allow_html=True)

    elif project["title"] == "JSW Energy":
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown('<div class="metric"><div class="metric-value">6.4%</div><div class="metric-label">PROJECT IRR</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown('<div class="metric"><div class="metric-value">6.6%</div><div class="metric-label">EQUITY IRR</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="metric"><div class="metric-value">1.34×</div><div class="metric-label">MINIMUM DSCR</div></div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# SKILLS & TOOLS
# ---------------------------------------------------------
elif page == "Skills & Tools":

    st.markdown('<div class="eyebrow">Capability Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Skills & Tools</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Relevant Skills")
        skills = [
            "Financial Statement Analysis",
            "Ratio Analysis",
            "Financial Analysis",
            "Investment Analysis",
            "Market Research",
            "Business Research",
            "Data Visualization",
            "Financial Modelling",
        ]
        for skill in skills:
            st.markdown(f'<span class="tag">{skill}</span>', unsafe_allow_html=True)

    with col2:
        st.markdown("### Tools")
        tools = [
            ("Excel", "Advanced"),
            ("Power BI", "Intermediate"),
            ("SPSS", "Beginner"),
            ("R Studio", "Beginner"),
            ("Python", "Basic"),
            ("Bloomberg Terminal", "Exposure"),
        ]
        for tool, level in tools:
            st.markdown(
                f'<div class="info-card"><b>{tool}</b><br><span style="color:#718096;">{level}</span></div>',
                unsafe_allow_html=True
            )


# ---------------------------------------------------------
# RESUME
# ---------------------------------------------------------
elif page == "Resume":

    st.markdown('<div class="eyebrow">Professional Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Resume</div>', unsafe_allow_html=True)

    resume_path = Path("assets/Aruneshwar_Thakur_Resume.pdf")

    if resume_path.exists():
        st.pdf(str(resume_path))
        st.download_button(
            "Download Resume",
            data=resume_path.read_bytes(),
            file_name="Aruneshwar_Thakur_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    else:
        st.info(
            "Resume PDF will appear here after Aruneshwar_Thakur_Resume.pdf "
            "is uploaded to the assets folder."
        )


# ---------------------------------------------------------
# CONTACT
# ---------------------------------------------------------
elif page == "Contact":

    st.markdown('<div class="eyebrow">Professional Contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Let's Connect</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
    <b>Email</b><br>
    27-aruneshwar.thakur@fiib.edu.in
    </div>

    <div class="info-card">
    <b>Phone</b><br>
    +91 6230314426
    </div>

    <div class="info-card">
    <b>Location</b><br>
    New Delhi, India
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Connect on LinkedIn",
        "https://www.linkedin.com/in/aruneshwar-thakur/",
        use_container_width=True
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
Aruneshwar Thakur · PGDM Finance · FIIB · New Delhi<br>
Finance & Investment Analyst · Financial Analysis · Investment Research · Business Intelligence
</div>
""", unsafe_allow_html=True)
