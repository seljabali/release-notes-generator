import sys
from datetime import datetime, timezone 
import subprocess
import re

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

if __name__ == "__main__":
    print(calculate_next_tag())
