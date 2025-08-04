# synthetic_resume_generator

> Smuggling devs through the AI filters since 2025.

---

This repo is a résumé injection system designed to spoof applicant tracking systems (ATS), scrape job descriptions, and generate synthetic resumes that bypass keyword gates and filtering heuristics.

Built for devs tired of rejection.  
Or maybe just one dev.  
Me.

---

## ⚙️ Core Logic

- Scrapes target job description
- Extracts high-signal keyword clusters
- Builds JSON-based résumé injection object
- Formats output to resemble high-confidence ML/Dev resume

---

## 📂 Files

- `resume_builder.py` — Synthetic résumé generator
- `sample_resume.json` — Output sample (spoofed)
- `.env` — Injection variables (accidentally committed)
- `README.md` — You're in the metadata now

---

## 🧬 Leak Warning

```dotenv
TARGET_ROLE=ML_ENGINEER
DEV_NAME=Bryan S. Barrett
ORIGIN_NODE=https://bryansbarrett.dev
JOB_ID_OVERRIDE=TSLA-448
RESUME_INJECTION_MODE=TRUE
