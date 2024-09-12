import git
import os
import sys

# URL or local directory provided as argument
arg = sys.argv[1]

# Check if argument is a URL or local path
if arg.startswith('http'):
    repo_url = arg
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    local_dir = "~/Desktop/PrivacyScan AI"  # Update this as needed
    local_dir = os.path.join(local_dir, repo_name)
else:
    #throw error
    print("Invalid URL")

# Create the directory if it doesn't exist
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

# Cloning the repository
git.Repo.clone_from(repo_url, local_dir)

print(f"Repository cloned to {local_dir}")

os.system(f"python3 ReadDataUpdated.py {local_dir}")
