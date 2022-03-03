## /bl-wl-server

- `npm i`
- `node app.js`

```bash
curl --location --request POST 'http://127.0.0.1:6000/api/searchUrl' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url":"https://qw-2-2-2.glitch.me/"
}'
```

## /faviconsimilarityapi

- `pip install -r requirementswin.txt`
- `uvicorn main:app --reload`

```bash

curl --location --request POST 'http://127.0.0.1:8000/query' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url":"https://google.com/"
}'

```

## /mainapp

- `npm i`
- `node app.js`

```bash

curl --location --request POST 'http://127.0.0.1:4000/analyze' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url":"https://google.com/"
}'

```

## /urlanalyzer

- `pip install -r requirements.txt`
- `python app.py`

```bash

curl --location --request POST 'http://127.0.0.1:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url":"https://itsmycode.com/"
}'

```
