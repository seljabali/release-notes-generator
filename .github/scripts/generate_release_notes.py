import subprocess
import re

def get_commits_since_last_tag():
    try:
        latest_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0'], stderr=subprocess.DEVNULL).decode().strip()
        # print(f"Latest tag: {latest_tag}")  # Debug print
    except subprocess.CalledProcessError:
        latest_tag = ""
        print("No tags found.")  # Debug print

    commit_logs = subprocess.check_output(['git', 'log', f'{latest_tag}..HEAD', '--pretty=format:%H -- %an -- %s']).decode().strip().split('\n')
    # print(f"Commit logs since last tag: {commit_logs}")  # Debug print
    return commit_logs

def generate_release_notes():
    notes = "## ✨ Enhancements\n"
    commit_logs = get_commits_since_last_tag()
    if commit_logs:
        for log in commit_logs:
            hash, author, message = log.split(' -- ')
            # Attempt to extract PR number from commit message
            pr_match = re.search(r'\(#(\d+)\)', message)
            pr_number = pr_match.group(1) if pr_match else ''
            notes += f"* {message} by {author}\n"
    else:
        notes += "No changes were made since the last release.\n"
    return notes

if __name__ == "__main__":
    print(generate_release_notes())
