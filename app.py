from fastapi import FastAPI, Request
from ai.reviewer import review_code
from github_api.github_client import get_pr_files, create_pr_comment

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "AI Code Reviewer Agent is running successfully!"}

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()

    print("Received Webhook")

    if payload.get("action") == "opened":

        repo_name = payload["repository"]["full_name"]
        pr_number = payload["pull_request"]["number"]

        print("Repository:", repo_name)
        print("PR Number:", pr_number)

        files = get_pr_files(repo_name, pr_number)

        full_review = "## 🤖 AI Code Review\n\n"

        for file in files:
            print("\nReviewing:", file.filename)

            code = file.patch if file.patch else ""

            review = review_code(code)

            full_review += f"### {file.filename}\n"
            full_review += review + "\n\n"

        create_pr_comment(repo_name, pr_number, full_review)

        print("Review posted successfully!")

    return {"status": "success"}
#Testing AI Code Reviewer