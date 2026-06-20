# 🦅 IC Imagine 8th Grade Math — Installation Instructions
## Setting Up a NEW GitHub Pages Site from Scratch

---

## Step 1: Download and Unzip the Site Files

1. Download the `8th_grade_math_FINAL_9.zip` file from Claude
2. Unzip it on your computer:
   - **Windows**: Right-click the zip → "Extract All" → Choose your Desktop or Downloads
   - **Mac**: Double-click the zip file
3. You should now have a folder with **51 files** (31 HTML files, 18 PDFs, a deploy script, and this instruction file)

---

## Step 2: Create a GitHub Account (if you don't have one)

1. Go to **https://github.com/signup**
2. Create a free account
3. Verify your email address
4. Remember your **username** — you'll need it for your site URL

---

## Step 3: Create a New Repository

1. Sign in to GitHub
2. Click the **green "New" button** on the left side of the dashboard
   - Or go directly to: **https://github.com/new**
3. Fill in the settings:
   - **Repository name**: `ic-imagine-math` (or whatever you'd like — this becomes part of your URL)
   - **Description** (optional): `8th Grade Math - IC Imagine`
   - **Public** must be selected (GitHub Pages only works with public repos on free accounts)
   - **DO NOT** check "Add a README file" — leave it unchecked
   - **DO NOT** add .gitignore or license
4. Click the green **"Create repository"** button
5. You'll see a page that says "Quick setup" — **don't close this page yet**, but you won't need to run any of those commands

---

## Step 4: Upload All Your Files

1. On your new empty repository page, click the link that says **"uploading an existing file"**
   - If you don't see that link, click **"Add file"** → **"Upload files"** near the top
2. Open your unzipped folder on your computer
3. Select **ALL 51 files** inside the folder:
   - **Windows**: Open the folder, press **Ctrl+A** to select all
   - **Mac**: Open the folder, press **Cmd+A** to select all
4. **Drag all the selected files** into the upload area on GitHub
   - You should see it say something like "51 files" being uploaded
   - **IMPORTANT**: Drag the FILES, not the folder itself. GitHub needs the files at the top level, not inside a subfolder
5. Wait for all files to finish uploading (you'll see progress bars)
6. At the bottom of the page, under "Commit changes":
   - Type a message like: `Initial upload of 8th grade math site`
   - Make sure **"Commit directly to the main branch"** is selected
7. Click the green **"Commit changes"** button
8. Wait for it to process — this may take 30-60 seconds with 51 files

---

## Step 5: Enable GitHub Pages

1. In your repository, click the **"Settings"** tab (gear icon, top of page)
2. In the left sidebar, scroll down and click **"Pages"**
3. Under **"Source"**, you should see a dropdown that says "None"
4. Change it to **"main"** (or "master" — whatever branch name appears)
5. Leave the folder as **"/ (root)"**
6. Click **"Save"**
7. You'll see a message: "GitHub Pages source saved"
8. Wait 2-5 minutes for the site to build

---

## Step 6: Visit Your Live Site

Your site will be live at:

```
https://YOUR-USERNAME.github.io/ic-imagine-math/
```

Replace `YOUR-USERNAME` with your actual GitHub username and `ic-imagine-math` with whatever you named your repository in Step 3.

For example, if your username is `mathteacher2025` and you named the repo `ic-imagine-math`, your URL would be:
```
https://mathteacher2025.github.io/ic-imagine-math/
```

**Note:** The first time may take up to 5 minutes. If you see a 404 page, wait a few minutes and refresh.

---

## Checklist: Verify Everything Works

Open your site and check:

- [ ] Home page loads with all unit cards and the Kingfisher logo
- [ ] Unit 1: All 7 tabs visible and clickable (scroll right if needed)
- [ ] Unit 2: Review tab at end only
- [ ] Unit 3: 10 tabs — One-Step through Review, with SVG step-by-step visuals
- [ ] Unit 4: 8 parallel lines problems in 4.2, triangle problems in 4.3
- [ ] Unit 5: 8 tabs — Theorem, Hypotenuse, Missing Leg, Converse, Word Problems, Coord Distance, Review
- [ ] Unit 6: All 7 tabs have comprehensive notes (Functions, Slope, Tables, Real-World, Comparing, Qualitative, Systems)
- [ ] Unit 7: Review tab at the end
- [ ] Unit 8: Review tab at the end
- [ ] Kingfisher Tutor (bird icon, bottom-right corner) opens when clicked

---

## Future Updates

When you have new changes from Claude in a new zip file:

1. Go to your repository on GitHub
2. Click **"Add file"** → **"Upload files"**
3. Drag in all the updated files (they will replace the old ones)
4. Type a commit message describing what changed
5. Click **"Commit changes"**
6. Wait 1-2 minutes for the site to rebuild

---

## Troubleshooting

**"404 - Page not found" when visiting the site?**
- Make sure GitHub Pages is enabled (Step 5)
- Make sure the `index.html` file is at the top level of the repo (not inside a subfolder)
- Wait 5 minutes — the first build takes longer

**Files ended up inside a subfolder?**
- This happens if you dragged the FOLDER instead of the individual FILES
- Delete the subfolder on GitHub (click it, then the trash icon on each file)
- Re-upload by dragging the 51 individual files

**Site looks like the old version?**
- Hard refresh: **Ctrl+Shift+R** (Windows) or **Cmd+Shift+R** (Mac)
- Or try opening in a private/incognito browser window

**Some pages show errors?**
- Make sure all 51 files were uploaded (check the file count in your repo)
- PDFs are needed for worksheet and answer key links

**AI Tutor says "needs API key"?**
- This is expected — the Anthropic API requires authentication
- Students will see a friendly message about this
- Making it fully functional would require a backend proxy (advanced setup for later)
