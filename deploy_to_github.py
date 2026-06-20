#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════
  🦅 IC Imagine 8th Grade Math — One-Click Deploy
═══════════════════════════════════════════════════════════

This script uploads your entire math site to GitHub Pages.
No git install needed — it uses the GitHub website API.

BEFORE RUNNING THIS SCRIPT, you need TWO things:
  1. A free GitHub account (https://github.com/signup)
  2. A "Personal Access Token" — the script tells you how to get one

TO RUN:
  - Windows: Double-click this file, OR open Command Prompt and type:
             python deploy_to_github.py
  - Mac:     Open Terminal and type:
             python3 deploy_to_github.py
═══════════════════════════════════════════════════════════
"""

import os, sys, json, base64, time, glob

# ─── Check Python version ───
if sys.version_info < (3, 6):
    print("❌ Python 3.6+ is required. You have:", sys.version)
    print("   Download from: https://python.org")
    input("Press Enter to exit...")
    sys.exit(1)

try:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
except ImportError:
    print("❌ Missing urllib — this should be built into Python.")
    input("Press Enter to exit...")
    sys.exit(1)


# ─── Configuration ───
REPO_NAME = "ic-imagine-math"
SITE_FOLDER = "8th_grade_math"


def api(method, endpoint, token, data=None):
    """Make a GitHub API request."""
    url = f"https://api.github.com{endpoint}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "IC-Imagine-Deploy"
    }
    body = json.dumps(data).encode() if data else None
    if body:
        headers["Content-Type"] = "application/json"
    req = Request(url, data=body, headers=headers, method=method)
    try:
        resp = urlopen(req)
        return json.loads(resp.read().decode()) if resp.read else {}
    except HTTPError as e:
        error_body = e.read().decode()
        try:
            error_json = json.loads(error_body)
            return {"error": True, "status": e.code, "message": error_json.get("message", str(e))}
        except:
            return {"error": True, "status": e.code, "message": str(e)}


def upload_file(token, username, repo, filepath, repo_path):
    """Upload a single file to GitHub."""
    with open(filepath, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    
    data = {
        "message": f"Add {repo_path}",
        "content": content
    }
    
    result = api("PUT", f"/repos/{username}/{repo}/contents/{repo_path}", token, data)
    return not result.get("error", False)


def main():
    print()
    print("═══════════════════════════════════════════════════════")
    print("  🦅 IC Imagine 8th Grade Math — Deploy to GitHub")
    print("═══════════════════════════════════════════════════════")
    print()
    
    # ─── Find the site files ───
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Look for the folder in common locations
    candidates = [
        os.path.join(script_dir, SITE_FOLDER),
        os.path.join(script_dir),
        os.path.join(os.path.expanduser("~"), "Downloads", SITE_FOLDER),
        os.path.join(os.path.expanduser("~"), "Desktop", SITE_FOLDER),
    ]
    
    site_dir = None
    for c in candidates:
        if os.path.isdir(c) and os.path.isfile(os.path.join(c, "index.html")):
            site_dir = c
            break
    
    if not site_dir:
        print("❌ Can't find the site files.")
        print()
        print("Make sure:")
        print("  1. You unzipped 8th_grade_math_FINAL.zip")
        print("  2. This script is in the SAME folder as the '8th_grade_math' folder")
        print("     OR the 53 files are in the same folder as this script")
        print()
        print(f"I looked in: {script_dir}")
        input("\nPress Enter to exit...")
        return
    
    files = []
    for f in os.listdir(site_dir):
        full = os.path.join(site_dir, f)
        if os.path.isfile(full) and not f.startswith('.') and f != "deploy.sh" and f != os.path.basename(__file__):
            files.append((full, f))
    
    print(f"✅ Found {len(files)} files in: {site_dir}")
    print()
    
    # ─── Get credentials ───
    print("─── STEP 1: GitHub Username ───")
    print()
    username = input("Enter your GitHub username: ").strip()
    if not username:
        print("❌ Username can't be blank.")
        input("Press Enter to exit...")
        return
    
    print()
    print("─── STEP 2: Personal Access Token ───")
    print()
    print("You need a token to upload files. Here's how to get one:")
    print()
    print("  1. Go to: https://github.com/settings/tokens/new")
    print("     (Log in if asked)")
    print()
    print("  2. Fill in:")
    print("     • Note: 'math site deploy'")
    print("     • Expiration: 30 days (or whatever you want)")
    print("     • Check the box next to 'repo' (the first checkbox)")
    print()
    print("  3. Scroll down and click 'Generate token'")
    print()
    print("  4. COPY the token (starts with 'ghp_'). You only see it ONCE!")
    print()
    token = input("Paste your token here: ").strip()
    if not token:
        print("❌ Token can't be blank.")
        input("Press Enter to exit...")
        return
    
    # ─── Verify credentials ───
    print()
    print("Checking your credentials...")
    user_info = api("GET", "/user", token)
    if user_info.get("error"):
        print(f"❌ Authentication failed: {user_info.get('message')}")
        print("   Double-check your token and try again.")
        input("Press Enter to exit...")
        return
    
    actual_user = user_info.get("login", username)
    print(f"✅ Logged in as: {actual_user}")
    print()
    
    # ─── Create repository ───
    print("─── STEP 3: Creating repository ───")
    print()
    
    # Check if repo already exists
    existing = api("GET", f"/repos/{actual_user}/{REPO_NAME}", token)
    if not existing.get("error"):
        print(f"Repository '{REPO_NAME}' already exists.")
        print()
        choice = input("Overwrite it with fresh files? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            print("OK, not overwriting. Exiting.")
            input("Press Enter to exit...")
            return
        # Delete and recreate
        print("Deleting old repository...")
        api("DELETE", f"/repos/{actual_user}/{REPO_NAME}", token)
        time.sleep(2)
    
    print(f"Creating repository: {REPO_NAME}...")
    result = api("POST", "/user/repos", token, {
        "name": REPO_NAME,
        "description": "IC Imagine Public Charter School — 8th Grade Math",
        "homepage": f"https://{actual_user}.github.io/{REPO_NAME}/",
        "private": False,
        "auto_init": True  # Creates a README so we have a branch
    })
    
    if result.get("error"):
        print(f"❌ Failed to create repo: {result.get('message')}")
        if "already exists" in str(result.get("message", "")):
            print("   The repo might still be deleting. Wait 30 seconds and try again.")
        input("Press Enter to exit...")
        return
    
    print("✅ Repository created!")
    print()
    time.sleep(3)  # Give GitHub a moment
    
    # ─── Upload all files ───
    print("─── STEP 4: Uploading files ───")
    print()
    print(f"Uploading {len(files)} files (this takes 2-3 minutes)...")
    print()
    
    success = 0
    failed = 0
    for i, (filepath, filename) in enumerate(files):
        pct = int((i + 1) / len(files) * 100)
        bar = "█" * (pct // 5) + "░" * (20 - pct // 5)
        print(f"\r  [{bar}] {pct}% — {filename}", end="", flush=True)
        
        ok = upload_file(token, actual_user, REPO_NAME, filepath, filename)
        if ok:
            success += 1
        else:
            failed += 1
            # Retry once
            time.sleep(1)
            ok = upload_file(token, actual_user, REPO_NAME, filepath, filename)
            if ok:
                success += 1
                failed -= 1
        
        # Rate limit: GitHub allows ~10-20 requests per minute for contents API
        time.sleep(1.5)
    
    print()
    print()
    print(f"✅ Uploaded: {success}/{len(files)} files")
    if failed > 0:
        print(f"⚠️  Failed: {failed} files (you can re-upload these manually on github.com)")
    print()
    
    # ─── Enable GitHub Pages ───
    print("─── STEP 5: Enabling GitHub Pages ───")
    print()
    
    pages_result = api("POST", f"/repos/{actual_user}/{REPO_NAME}/pages", token, {
        "source": {"branch": "main", "path": "/"}
    })
    
    if pages_result.get("error"):
        print("⚠️  Couldn't auto-enable Pages. Do it manually:")
        print(f"   1. Go to: https://github.com/{actual_user}/{REPO_NAME}/settings/pages")
        print("   2. Source → main → / (root) → Save")
    else:
        print("✅ GitHub Pages enabled!")
    
    print()
    time.sleep(3)
    
    # ─── Done! ───
    site_url = f"https://{actual_user}.github.io/{REPO_NAME}/index.html"
    repo_url = f"https://github.com/{actual_user}/{REPO_NAME}"
    
    print("═══════════════════════════════════════════════════════")
    print()
    print("  🎉 YOUR SITE IS LIVE!")
    print()
    print(f"  🌐 Site URL:  {site_url}")
    print(f"  📁 Repo URL:  {repo_url}")
    print()
    print("  (It may take 2-3 minutes for the site to appear.)")
    print("  (If you get a 404, wait a moment and refresh.)")
    print()
    print("═══════════════════════════════════════════════════════")
    print()
    print("Share the Site URL with your students!")
    print()
    print("TO UPDATE LATER:")
    print("  Just run this script again. It will replace the old files.")
    print()
    
    input("Press Enter to close...")


if __name__ == "__main__":
    main()
