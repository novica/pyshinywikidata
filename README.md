# Shiny for Python app to access Wikidata

This is a simple demo in Shiny for Python to access data on Wikidata for politicians and their closes relatives as an attempt to get data on politically exposed persons.

This is also a python package managed with [`uv`](https://docs.astral.sh/uv) and automated to be deployed to Posit Connect. To run it clone the repository and install the package with:

```
uv sync
```

Then, run the app with:

```
uv run uvicorn pyshinywikidata.app:app
```

## Deploy to Posit Connect

Deployment to Posit Connect (for more see: [Git-Backed Content](https://docs.posit.co/connect/user/git-backed/)) is automated by the github actions workflow [`deploy.yml`](.github/workflows/deploy.yml).
Since we use `uv` to manage the project, the `requirements.txt` and `manifest.json` files needed by Posit,
are created automatically and only added to the deploy branch.

## Read more about the motivation for this app:
- [Part 1](https://discindo.org/post/using-wikidata-to-draw-networks-of-politically-exposed-persons-1/)
- [Part 2](https://discindo.org/post/using-wikidata-to-draw-networks-of-politically-exposed-persons-2/)
- [Part 3](https://discindo.org/post/using-uv-to-manage-environment-for-a-python-shiny-app-and-set-up-a-workflow-to-publish-it-to-posit-connect/)
