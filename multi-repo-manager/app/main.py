from flask import Flask, render_template, request, redirect, url_for, jsonify
import json, re, os

app = Flask(__name__, template_folder="templates", static_folder="static")

REPOS_FILE = "/config/multi-repo-manager/repos.json"

def load_repos():
    if not os.path.exists(REPOS_FILE):
        return []
    with open(REPOS_FILE) as f:
        data = json.load(f)
    return data.get("repositories", [])

def save_repos(repos):
    with open(REPOS_FILE, "w") as f:
        json.dump({"repositories": repos}, f, indent=2)

def is_valid_url(url):
    pattern = re.compile(r"^https://github.com/[w.-]+/[w.-]+(/?$)", re.IGNORECASE)
    return bool(pattern.match(url.rstrip("/")))

@app.route("/", methods=["GET"])
def index():
    repos = load_repos()
    return render_template("index.html", repos=repos)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name", "").strip()
    url  = request.form.get("url", "").strip()
    desc = request.form.get("description", "").strip()
    repos = load_repos()
    error = None
    if not name or not url:
        error = "Name and URL are required."
    elif not is_valid_url(url):
        error = "Only GitHub repository URLs are supported (https://github.com/...)."
    elif any(r["url"].rstrip("/") == url.rstrip("/") for r in repos):
        error = "This repository URL is already in the list."
    else:
        repos.append({"name": name, "url": url, "description": desc, "enabled": True})
        save_repos(repos)
        return redirect(url_for("index"))
    return render_template("index.html", repos=repos, error=error)

@app.route("/toggle/<int:idx>", methods=["POST"])
def toggle(idx):
    repos = load_repos()
    if 0 <= idx < len(repos):
        repos[idx]["enabled"] = not repos[idx].get("enabled", True)
        save_repos(repos)
    return redirect(url_for("index"))

@app.route("/delete/<int:idx>", methods=["POST"])
def delete(idx):
    repos = load_repos()
    if 0 <= idx < len(repos):
        repos.pop(idx)
        save_repos(repos)
    return redirect(url_for("index"))

@app.route("/api/repos", methods=["GET"])
def api_repos():
    return jsonify({"repositories": load_repos()})

@app.route("/api/repos", methods=["POST"])
def api_add():
    data = request.get_json(force=True)
    repos = load_repos()
    url = data.get("url", "").strip()
    name = data.get("name", "").strip()
    if not name or not url:
        return jsonify({"error": "name and url required"}), 400
    if not is_valid_url(url):
        return jsonify({"error": "invalid GitHub URL"}), 400
    repos.append({"name": name, "url": url,
                  "description": data.get("description", ""),
                  "enabled": data.get("enabled", True)})
    save_repos(repos)
    return jsonify({"ok": True}), 201

if __name__ == "__main__":
    os.makedirs(os.path.dirname(REPOS_FILE), exist_ok=True)
    app.run(host="0.0.0.0", port=8099, debug=False)
