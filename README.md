# AI Blogging Workflow (Built with Make.com)

This workflow automatically turns simple blog topic ideas into ready-to-edit blog drafts.  
I built it as a fresher to learn how Make.com connects Google Sheets, GPT-4, and Google Docs without needing to write a lot of custom code.

---

## Workflow explained

- **Step 1 — Start with a blog idea**  
  Whenever I add a new topic in Google Sheets, the workflow automatically picks it up.  

- **Step 2 — Draft content with GPT-4**  
  The AI writes a structured first draft for the blog, making it SEO-friendly and clear.  

- **Step 3 — Format and organize the content**  
  The workflow creates a neatly formatted Google Doc with headings and paragraphs.  

- **Step 4 — Save for review**  
  I can open the Google Doc, review the draft, and make final edits before publishing.  

This saves me hours of writing and formatting — I just give an idea, and the workflow delivers a ready-to-edit blog draft.

---

## Why I built this

- I wanted to practice building real workflows in Make.com.  
- It showed me how to connect multiple tools (Sheets → GPT-4 → Docs) in one flow.  
- As a beginner, this project gave me confidence that I can automate real-world tasks.

---

## Tools used

- **Make.com** — workflow automation platform  
- **Google Sheets** — input for blog topics  
- **OpenAI GPT-4** — AI-powered blog drafting  
- **Google Docs** — output for final drafts

---

## Files included

- `ai_blogging.json` – cleaned Make.com workflow export  
- `helper_title_case.py` – Python helper script to format blog titles  
- `sample_output.png` – screenshot showing a generated blog draft

---

## How to use

1. Import `ai_blogging.json` into Make.com.  
2. Replace connections (`areeshausmani93_connection`) with your own Google and OpenAI credentials.  
3. Add blog topics into Google Sheets — the workflow automatically generates Google Docs drafts for each topic.
