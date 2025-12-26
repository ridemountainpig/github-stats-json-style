import sys
import requests
from bs4 import BeautifulSoup


def generate_github_stats(username):
    url = f"https://yc-github-stats.zeabur.app/api?username={username}"

    header = {
        "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=header)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.title.text.strip()
    description = soup.desc.text.strip()

    metrics = description.split(',')

    description_dict = {}

    for metric in metrics:
        key, value = metric.split(':')
        key = key.strip()
        value = int(value.strip())
        description_dict[key] = value

    description_dict_keys = list(description_dict.keys())

    github_stats_json = f"""
```json
{{
    "{title}": {{
        "{description_dict_keys[0]}": "{description_dict[description_dict_keys[0]]} ⭐️",
        "{description_dict_keys[1]}": "{description_dict[description_dict_keys[1]]} 🔥",
        "{description_dict_keys[2]}": "{description_dict[description_dict_keys[2]]} 🚀",
        "{description_dict_keys[3]}": "{description_dict[description_dict_keys[3]]} 📬",
        "{description_dict_keys[4]}": "{description_dict[description_dict_keys[4]]} 🤝"
    }}
}}
```
    """

    with open("TEMPLATE.md", "r") as file:
        readme_template = file.read()

    readme_template = readme_template.replace(
        "{{github_json_stats}}", github_stats_json)

    with open("README.md", "w") as file:
        file.write(readme_template)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        generate_github_stats(username)
    else:
        print("GitHub username not provided.")
        sys.exit(1)
