# Shiny for Python app to access Wikidata

This is a simple demo in Shiny for Python to access data on Wikidata for politicians and their closes relatives as an attempt to get data on politically exposed persons.

This is also a python package. To run it clone the repor and install the package with:

```
pip install .
```

Then, run the app with:

```
uvicorn pyshinywikidata.app:app --host 127.0.0.1 --port 8000
```


Read more about the motivation for this app:
- [Part 1](https://discindo.org/post/using-wikidata-to-draw-networks-of-politically-exposed-persons-1/)
- [Part 2](https://discindo.org/post/using-wikidata-to-draw-networks-of-politically-exposed-persons-2/)
