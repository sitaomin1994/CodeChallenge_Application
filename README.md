### Question - Applications

Imagine you have a program that needs to look up information about items using their item ID, often in large batches.

Unfortunately, the only API available for returning this data takes one item at a time, which means you will have to perform one query per item. Additionally, the API is limited to five simultaneous requests. Any additional requests will be served with HTTP 429 (too many requests).

Write a client utility for your program to use that will retrieve the information for all given IDs as quickly as possible without triggering the simultaneous requests limit and without performing unnecessary queries for item IDs that have already been seen.

API Usage:

GET https://eluv.io/items/:id

Required headers:

Authorization: Base64(:id)

Example:

curl https://eluv.io/items/cRF2dvDZQsmu37WGgK6MTcL7XjH -H "Authorization: Y1JGMmR2RFpRc211MzdXR2dLNk1UY0w3WGpI"

### Solution

Request using python aiohttp and asyncio

### Execution
Environment - Python 3.9

Install required package
```shell
pip install -r requirements.txt
```
Run program
```shell
python main.py --test_file='your test file path'
```

Result shows in 'Result/' each request result as a text file