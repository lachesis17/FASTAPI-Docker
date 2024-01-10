### **Simple FastAPI via uvicorn and Docker to return word counts and stats from a text file via POST request.**

_Hyphonated words and words containing an apostrophe are treat as a single word for simplicity._
_Dates are one word, numbers are one word, all symbols are discarded apart from ampersand "&", since it's "and"!_

# Commands:
To run locally without Docker, use:
```
pip install -r 'requirements.txt'
uvicorn fastapi_wordcount:app --reload --port 8005
```

To build and run via Docker, use:
```
docker build -t fastapi-app .
docker run -p 8005:8005 fastapi-app
```

# Test a POST request via POSTMAN:

- Text File
Using the provided example to submit a plaintext,txt file:
```
/example.txt
```
In the host application POST function path "/count_text":
```
http://127.0.0.1:8005/count_text
```
With:
```
POST > Body > form-data > file: example.txt > SEND
```



- String
Using a string:
```
some example text
```
In the host application POST function path "/count_text":
```
http://127.0.0.1:8005/count_text
```
With:
```
POST > Body > form-data > string: some example text > SEND
```


- Errors:
Using a string:
```
Submitting a file and a string
```

```
Submitting nothing
```