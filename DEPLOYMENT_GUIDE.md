# Kelly - AI Scientist Poet Chatbot 🎭

## Quick Deploy to Render (FREE)

### Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named "kelly-ai-poet"
3. Don't initialize with README (we already have one)

### Step 2: Push Code to GitHub

Run these commands in your terminal (PowerShell):

```powershell
cd "c:\Users\yohan\Kelly"
git init
git add .
git commit -m "Initial commit: Kelly AI Scientist Poet"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/kelly-ai-poet.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 3: Deploy on Render

1. Go to https://render.com and sign up (free)
2. Click "New +" and select "Web Service"
3. Connect your GitHub account
4. Select the "kelly-ai-poet" repository
5. Configure:
   - **Name**: kelly-ai-poet (or any name you like)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free
6. Click "Create Web Service"

### Step 4: Access Your Chatbot

After deployment (takes ~2-3 minutes), Render will give you a URL like:
`https://kelly-ai-poet.onrender.com`

---

## Alternative: Deploy to Railway (FREE)

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your kelly-ai-poet repository
5. Railway will auto-detect settings
6. Get your URL from the deployment

---

## Alternative: Deploy to PythonAnywhere (FREE)

1. Sign up at https://www.pythonanywhere.com (free account)
2. Go to "Web" tab
3. Click "Add a new web app"
4. Choose Flask and Python 3.10
5. Upload your files or clone from GitHub
6. Set working directory to your app folder
7. Reload and get your URL: `https://YOUR_USERNAME.pythonanywhere.com`

---

## Need Help?

If you don't have Git installed, you can:
1. Download Git from https://git-scm.com/download/win
2. Or manually upload files to GitHub through the web interface
3. Or use GitHub Desktop: https://desktop.github.com/

---

**Your Kelly chatbot is ready to deploy! Choose any of the free hosting options above.** 🚀
