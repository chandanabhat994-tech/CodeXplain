import streamlit as st
from google import genai
import os
import time

# 1. Page Configuration (Centered for a spacious, professional flow)
st.set_page_config(
    page_title="CodesXplain Hub", 
    page_icon="⚡", 
    layout="centered"
)

# Premium Custom UI Styles
st.markdown("""
    <style>
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 44px !important;
        font-weight: 800;
        background: linear-gradient(45deg, #1E88E5, #00D2FF, #7928CA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }
    .hero-subtitle {
        font-size: 16px !important;
        color: #6A737D;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-box {
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<h1 class="hero-title">⚡ CodeXplain Hub</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">The all-in-one developer workspace. Explain, debug, measure, translate, and document your code instantly.</p>', unsafe_allow_html=True)

# 2. Initialize AI Client
if "GEMINI_API_KEY" in os.environ:
    client = genai.Client()
else:
    st.error("🚨 GEMINI_API_KEY Missing from environment variables.")
    st.info("Please set your GEMINI_API_KEY parameter to keep your core processing engine active.")
    st.stop()

# 3. Streamlined Configuration Parameters (Clean 2-Column Grid Frontend Header)
st.markdown("### 📥 Source Code Settings")

c1, c2 = st.columns(2)
with c1:
    style = st.selectbox("Explanation Depth:", ["Detailed Breakdown", "Beginner Friendly (ELI5)", "Quick Summary"], index=0)
with c2:
    target_lang = st.selectbox("Translate Code To:", ["Don't Translate", "Python", "JavaScript", "C++", "Java", "Go", "Rust"], index=0)

# Code Text Editor Block UI Component
code_input = st.text_area(
    "Paste your raw code block below:", 
    height=250, 
    placeholder="// Paste your functions, loops, or buggy scripts here..."
)

explain_btn = st.button("🚀 Deconstruct & Optimize Logic", type="primary", use_container_width=True)

st.markdown("---")

# 4. Workspace Display Panel
st.markdown("### 🧠 Workspace Insights")

if explain_btn:
    if not code_input.strip():
        st.warning("Please add a code snippet first inside the code input window above.")
    else:
        with st.spinner("Analyzing architecture, debugging logic, and compiling metrics..."):
            try:
                # Master prompt orchestrator to generate segmented data payloads
                prompt = f"""
                You are a senior software architect and world-class computer science instructor. 
                Analyze the following code snippet and provide responses strictly partitioned by the double hashtag headings below.
                
                Code Explanation Style Requested: {style}.
                Target Translation Language Requested: {target_lang}.

                Provide your entire response structured matching this layout exactly:
                
                ## Overview
                (Provide a clean, high level 2-3 sentence summary of what this code achieves in plain English)
                
                ## Logic Flow Breakdown
                (Break down the sequential line execution simply. Use lists, bolding, or markdown tables where helpful)
                
                ## Auto Debugger Report
                (Scan the code for bugs, type mismatches, inefficiencies, or syntax errors. Explain what is wrong or could be cleaner. Then provide a code block with the fully corrected/optimized code)
                
                ## Complexity Metric Score
                (Provide a single raw integer score from 1 to 10 based on Time/Space complexity, followed by a 1-sentence description on a new line. Example format line 1: 5. Example format line 2: The nested loops cause quadratic time complexity.)
                
                ## Language Translation Code
                (If a translation language was requested, provide the exact code rewritten into that target language. If "Don't Translate" was picked, just output: Translation not requested.)
                
                Source Code to parse:
                ```
                {code_input}
                ```
                """
                
                # Network Resilient Request Loop
                response = None
                for attempt in range(3):
                    try:
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents=prompt,
                        )
                        break
                    except Exception as api_err:
                        if "429" in str(api_err) or "503" in str(api_err):
                            if attempt < 2:
                                time.sleep(3)
                                continue
                        raise api_err
                
                if response:
                    st.balloons() # Run-time execution drop celebration
                    
                    ai_text = response.text
                    sections = ai_text.split("## ")
                    
                    # Data allocation variables
                    overview_data, logic_data, debug_data, complexity_data, translation_data = "", "", "", "", ""
                    
                    for section in sections:
                        if not section.strip():
                            continue
                        lines = section.split("\n", 1)
                        title = lines[0].strip().lower()
                        content = lines[1].strip() if len(lines) > 1 else ""
                        
                        if "overview" in title:
                            overview_data = content
                        elif "flow" in title or "logic" in title:
                            logic_data = content
                        elif "debugger" in title or "report" in title:
                            debug_data = content
                        elif "complexity" in title or "metric" in title:
                            complexity_data = content
                        elif "translation" in title:
                            translation_data = content

                    # Generate organized 5-tab stacked execution board UI
                    tab1, tab2, tab3, tab4, tab5 = st.tabs([
                        "📝 Functional Overview", 
                        "🔍 Line Breakdown", 
                        "🛠️ Auto-Debugger & Fixes", 
                        "📊 Complexity Analytics",
                        "🌐 Code Translator"
                    ])
                    
                    with tab1:
                        st.info(overview_data if overview_data else "Overview data compilation complete.")
                    
                    with tab2:
                        st.markdown(logic_data if logic_data else "Detailed breakdown tracing complete.")
                        
                    with tab3:
                        st.markdown("### 🪲 Code Health Check")
                        st.markdown(debug_data if debug_data else "No structural anomalies identified by analyzer node.")
                        
                    with tab4:
                        st.markdown("### 📈 Algorithmic Complexity Meter")
                        try:
                            # Isolate integer tier from text block
                            comp_lines = complexity_data.split("\n", 1)
                            score_num = int(comp_lines[0].strip())
                            reason_text = comp_lines[1].strip() if len(comp_lines) > 1 else ""
                            
                            # Shift status alert color thresholds
                            if score_num <= 3:
                                bg_color, text_lbl = "#D4EDDA", f"Low Complexity ({score_num}/10)"
                            elif score_num <= 7:
                                bg_color, text_lbl = "#FFF3CD", f"Medium Complexity ({score_num}/10)"
                            else:
                                bg_color, text_lbl = "#F8D7DA", f"High Complexity ({score_num}/10)"
                                
                            st.markdown(f'<div class="metric-box" style="background-color: {bg_color};">{text_lbl}</div>', unsafe_allow_html=True)
                            st.markdown(f"**AI Structural Analysis:** {reason_text}")
                        except:
                            st.markdown(complexity_data)
                            
                    with tab5:
                        st.markdown(f"### 🎯 Translated Implementation ({target_lang})")
                        st.markdown(translation_data if translation_data else "Select a translation language parameters above to run.")

                    st.markdown("---")
                    # Global compilation markdown downloader unit
                    st.download_button(
                        label="📥 Download Full Workspace Documentation (.md)",
                        data=ai_text,
                        file_name="codesplain_documentation.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                else:
                    st.error("Engine failed to resolve an extraction model response layer.")
            except Exception as e:
                st.error(f"Runtime compilation exception during setup assembly: {e}")
else:
    # Completely hidden workspace footprint before the trigger event fires
    st.empty()