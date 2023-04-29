#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <repository owner>")
        sys.exit(1)

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")

    else:
        print(f"Error: {response.status_code}")
        sys.exit(1)
