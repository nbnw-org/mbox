# Runs the metric for the given repositories.

metric_repos = [
    "mbox_word_count",
]


### Code to execute run.py in mbox_word_count/run.py

import os
import subprocess

# TODO Clear metrics.txt

for repo in metric_repos:
    print(f"Running {repo}...")
    subprocess.run(["python3", "{}/run.py".format(repo)])
    print(f"{repo} done.")

print("All repositories done.")