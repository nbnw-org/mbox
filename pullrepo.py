import os
from git import Repo

def clone_or_pull(repo_url, target_dir):
    try:
        if os.path.exists(target_dir):
            print(f"Repository {target_dir} already exists, performing pull...")
            repo = Repo(target_dir)
            origin = repo.remotes.origin
            origin.pull()
        else:
            print(f"Cloning {repo_url} into {target_dir}...")
            Repo.clone_from(repo_url, target_dir)
    except Exception as e:
        print(f"An error occurred: {e}")

NBNW_BASE_URL = "https://github.com/nbnw-org/"

metric_repos = [
    "mbox_word_count",
]

for repo in metric_repos:
    repo_url = NBNW_BASE_URL + repo
    clone_or_pull(repo_url, repo)