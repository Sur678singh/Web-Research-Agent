# 🧠 Smart Web Research Agent

An AI-powered **multi-tool research assistant** that can search the web, scrape real-time data, and generate intelligent answers using LLMs.

---

## 🚀 Features

* 🔍 **Real-time Web Search** (Tavily API)
* 🌐 **Web Scraping** using BeautifulSoup
* 🧠 **LLM Reasoning** with ChatGroq (LLaMA 3.3-70B)
* ⚡ **LangChain ReAct Agent**
* 💬 Chat-based UI (Frontend)
* 🔄 Dynamic query handling

---

## 🏗️ Tech Stack

### Backend

* FastAPI
* LangChain
* ChatGroq (LLaMA 3.3-70B)
* Tavily Search API
* BeautifulSoup
* Requests

### Frontend

* HTML, CSS, JavaScript
* Chat UI with interactive features

---

## 📂 Project Structure

```
├──main.py          # FastAPI server + agent+  scraping + search tools
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/smart-web-research-agent.git
cd smart-web-research-agent
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create a `.env` file:

```
TAVILY_API_KEY=your_api_key_here
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Start Backend Server

```bash
uvicorn main:app --reload
```

---

### 6️⃣ Open Frontend

Just open `index.html` in browser
OR use Live Server (VS Code)

---

## 🔌 API Endpoints

### POST `/ask`

#### Request:

```json
{
  "question": "What is the future of AI?"
}
```

#### Response:

```json
{
  "input": "...",
  "answer": "..."
}
```

---

## 🧠 How It Works

1. User asks a question
2. Agent decides:

   * Use web search OR not
3. Fetch URLs via Tavily
4. Scrape content from web pages
5. Filter & clean data
6. LLM generates final answer

---

## 🔄 Agent Workflow

```
User Query
   ↓
LangChain Agent (ReAct)
   ↓
[Search Tool] → [Scraper Tool]
   ↓
Filtered Data
   ↓
LLM Response
```

---

## ✨ UI Features

* Chat interface
* Auto-scroll

---

## ⚠️ Limitations

* Scraping may fail on some websites
* Response speed depends on network + model
* No persistent memory (yet)

---

## 🔮 Future Improvements

* ✅ Source citations (URLs)
* ✅ RAG (Vector Database)
* ✅ Multi-agent system (LangGraph)
* ✅ Chat history memory
* ✅ Markdown & code formatting
* ✅ Deployment (Render / Vercel)


## 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Suryansh Singh**

---

## ⭐ Support

If you like this project, please ⭐ the repository!