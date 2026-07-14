from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

g = Github(os.getenv("GITHUB_TOKEN"))

def get_repo(repo_name):
    return g.get_repo(repo_name)

def get_pr_files(repo_name, pr_number):
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    return pr.get_files()

def create_pr_comment(repo_name, pr_number, comment):
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(comment)