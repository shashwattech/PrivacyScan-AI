print("Hello world")


import git

# URL of the GitHub repository
repo_url = "https://github.com/abhishek-0713/MyWallet"

# Local directory where you want to clone the repository
local_dir = "/Users/ssrivastava4/Desktop/PrivacyScan AI/Test Repositories"

# Cloning the repository
git.Repo.clone_from(repo_url, local_dir)

print(f"Repository cloned to {local_dir}")




# https://github.com/abhishek-0713/MyWallet
# Rahul Jain
# 2:24 AM
# 1. Write code to download any repository
# 2. Unzip repository locally
# 3. For each file, call the chat api with question " Is this code dealing with any user PII data"?



# curl -X POST "https://sdk-team-opnai-eus-poc.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview" \
# -H "Content-Type: application/json" \
# -H "api-key: 9d5bcffba65648fcafc63d8a95a06c83" \
# -d '{
#   "messages": [
#     {"role": "user", "content": "Tell me about yourself"}
#   ],
#   "max_tokens": 100,
#   "temperature": 0.7
# }'



# curl -X POST "https://sdk-team-opnai-eus-poc.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2023-03-15-preview" \
# -H "Content-Type: application/json" \
# -H "api-key: 9d5bcffba65648fcafc63d8a95a06c83" \
# -d '{
#   "messages": [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello, how can Azure OpenAI help me?"}
#   ],                
#   "max_tokens": 100,
#   "temperature": 0.7










