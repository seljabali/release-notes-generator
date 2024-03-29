import subprocess
import re
import sys
from datetime import datetime, timezone 

repoUrl = "https://github.com/seljabali/super-duper-computing-machine"
devsMap = {'Sami Eljabali': '@seljabali'}

def getAuthorHandlesFromNames(authors_set):
    values = []
    for author in authors_set:
        if author in devsMap:
            # If the key is found, append its value to the list
            values.append(devsMap[author])
    
    result_string = ', '.join(values)
    return result_string

def get_latest_tag():
    tags = subprocess.check_output(['git', 'tag', '--sort=-creatordate']).decode().strip().split('\n')
    valid_tags = [tag for tag in tags if re.match(r'\d{4}\.\d{2}\.\d{2}', tag)]
    return valid_tags[0] if valid_tags else None

def calculate_next_tag():
    now = datetime.now(timezone.utc)
    year, week, _ = now.isocalendar()
    week_str = f"{week:02d}"  # Ensure week is two digits

    latest_tag = get_latest_tag()
    if latest_tag:
        latest_year, latest_week, latest_release = map(int, latest_tag.split('.'))
        if latest_year == year and f"{latest_week:02d}" == week_str:
            next_release = latest_release + 1
        else:
            next_release = 1
    else:
        next_release = 1

    # Here's the critical part ensuring the release number has a leading zero
    next_release_str = f"{next_release:02d}"

    next_tag = f"{year}.{week_str}.{next_release_str}"
    return next_tag

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
    authorsSet = set()
    if commit_logs:
        for log in commit_logs:
            hash, author, message = log.split(' -- ')
            # Attempt to extract PR number from commit message
            pr_match = re.search(r'\(#(\d+)\)', message)
            pr_number = pr_match.group(1) if pr_match else ''
            notes += f"* {message}\n"
            authorsSet.add(author)
    else:
        notes += "No changes were made since the last release.\n"

    notes += "\n\n"
    notes += "Thanks to " + getAuthorHandlesFromNames(authorsSet) + "\n\n"
    notes += "Change log " + repoUrl + "/compare/" + get_latest_tag() + "..." + calculate_next_tag()
    return notes

if __name__ == "__main__":
    print(generate_release_notes())
