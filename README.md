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

# Test a POST request via POSTMAN form-data:

- Text File

Using the provided example to submit a plaintext.txt file:
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
![1](https://github.com/lachesis17/FASTAPI-Docker/assets/78860436/b923ec59-7b27-48ec-81b2-ed97e7ad0f1d)

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

![2](https://github.com/lachesis17/FASTAPI-Docker/assets/78860436/1ceaadcd-908b-4689-80bb-e0bc8fbcc8b5)

- Errors:

```
Submitting a file and a string
```
![3](https://github.com/lachesis17/FASTAPI-Docker/assets/78860436/80f80efd-8844-4881-a26f-08d4e4836418)
```
Submitting nothing
```
![4](https://github.com/lachesis17/FASTAPI-Docker/assets/78860436/7651afe5-102a-427f-b6b7-4f06d36493b9)
