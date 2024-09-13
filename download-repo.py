import git
import os
import sys
import scanner

# URL or local directory provided as argument
arg = sys.argv[1]

# Check if argument is a URL or local path
if arg.startswith('http'):
    repo_url = arg
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    local_dir = os.path.join(os.getcwd(), "repos")
    local_dir = os.path.join(local_dir, repo_name)
else:
    #throw error
    print("Invalid URL")

# Create the directory if it doesn't exist
if not os.path.exists(local_dir):
    os.makedirs(local_dir)

# Cloning the repository
if os.path.exists(local_dir):
    os.system(f"rm -rf {local_dir}")

git.Repo.clone_from(repo_url, local_dir)

print(f"Repository cloned to {local_dir}")

scanner.scan_folder_for_pii(local_dir)
