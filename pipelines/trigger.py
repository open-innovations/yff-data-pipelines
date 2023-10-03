import os
import requests


if __name__ == '__main__':
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
    r = requests.post(
        'https://api.github.com/repos/open-innovations/yff-data/dispatches',
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        data='{"event_type": "update_data"}'
    )

    if r.status_code != requests.codes.no_content:
      print(r.text)
