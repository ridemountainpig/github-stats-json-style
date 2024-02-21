# Github Stats Json Style

## Introduction

This is a simple Github Stats Json Style for your Readme.

## Usage

1. Write your Readme content in the `TEMPLATE.md` file.
2. Place the `{{github_json_stats}}` tag where you want the Github Stats to appear in your Readme.
3. Create a new workflow file in your `.github/workflows` directory.
4. Add the following code to the workflow file, and replace `YOUR_GITHUB_USERNAME` with your Github username and `THE_BRANCH_YOU_WANT_TO_PUSH_TO` with the branch you want to push the stats to. This will generate the Github Stats Json and push it to the specified branch in your repository.

```yml
name: Generate Github Json Stats

on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:

jobs:
  generate-readme:
    runs-on: macos-14

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Github Stats Json Style
        uses: ridemountainpig/github-stats-json-style@v1.0.0
        with:
          username: YOUR_GITHUB_USERNAME
          push-branch: THE_BRANCH_YOU_WANT_TO_PUSH_TO
```

## Example

[TEMPLATE.md Example](TEMPLATE.md)

```json
{
  "Yen Cheng Lin's GitHub Stats, Rank: A": {
    "Total Stars Earned": "92 ⭐️",
    "Total Commits in 2024": "625 🔥",
    "Total PRs": "155 🚀",
    "Total Issues": "61 📬",
    "Contributed to (last year)": "16 🤝"
  }
}
```
