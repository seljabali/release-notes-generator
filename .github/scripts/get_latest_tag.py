import sys
import subprocess
import re

def get_latest_tag():
    tags = subprocess.check_output(['git', 'tag', '--sort=-creatordate']).decode().strip().split('\n')
    valid_tags = [tag for tag in tags if re.match(r'\d{4}\.\d{2}\.\d{2}', tag)]
    return valid_tags[0] if valid_tags else None

if __name__ == "__main__":
    print(get_latest_tag())
