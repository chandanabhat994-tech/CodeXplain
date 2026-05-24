# ⚡ Codesplain Ultimate Hub

An all-in-one AI-powered developer workspace built with **Streamlit** and the modern **Google GenAI SDK**. Codesplain Ultimate Hub transforms complex, raw source code into clear, structured, human-readable insights. It doesn't just explain code—it debugs logic flaws, tracks algorithmic complexity, translates snippets across different programming languages, and compiles instant documentation.

---

## 🚀 Key Features

* **📝 Functional Overview:** Provides a high-level, human-readable summary of what the code achieves, avoiding dense technical jargon.
* **🔍 Line-by-Line Breakdown:** Traces execution sequentially, breaking down variables, loops, and conditions using structured lists.
* **🛠️ Auto-Debugger & Fixes:** Scans code blocks for syntax or logical errors, highlights what went wrong, and offers copy-pasteable, corrected code.
* **📊 Complexity Analytics:** Rates code logic on a scale from 1 to 10 and dynamically displays a color-coded status badge (Low, Medium, or High complexity) along with an architectural analysis.
* **🌐 Cross-Language Translator:** Instantly rewrites input logic from one programming language into another (Python, JavaScript, C++, Java, Go, Rust).
* **📥 Markdown Documentation Downloader:** Compiles the full workspace analysis into a professional `.md` file, ready to be added straight to your GitHub repositories.

---

## 🛠️ System Architecture & Workflow

The application operates as a stacked, top-to-bottom pipeline that passes code securely to Google's AI models via environment variables without hardcoding secret keys:
