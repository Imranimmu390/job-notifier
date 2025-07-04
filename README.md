# 📬 DevOps Job Notifier (Automated)

This is a GitHub Actions-powered automation tool that fetches the latest 
DevOps job listings from RemoteOK and emails the top 5 results daily.

## 🔧 Stack
- Python
- GitHub Actions (CI/CD)
- SMTP (Gmail)

## 📦 How It Works
- Runs every day at 9 AM CST
- Uses GitHub Actions cron
- Fetches jobs via API
- Emails you the job list

## 🔐 Required Secrets
Go to GitHub → Settings → Secrets and add:
- `EMAIL_USER` → your Gmail address
- `EMAIL_PASS` → your Gmail App Password

## 🛠 Run it manually
Go to Actions → "Daily DevOps Job Notifier" → Click "Run workflow"

