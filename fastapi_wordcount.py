from fastapi import FastAPI, File, UploadFile
import hashlib

app = FastAPI()

'''To run without Docker, use command:
uvicorn fastapi_wordcount:app --reload --port 8005
'''

# Dict to hold the file checksum and it's word counts
results = {}

# Get a checksum of the file to use in caching
def get_checksum(file: str) -> str:
    return hashlib.md5(file.encode()).hexdigest()

# Set a POST request to the app with the text file, decode it
@app.post("/count_text")
async def decode_file(file: UploadFile = File(...)):
    file_content = await file.read()
    file_decoded = file_content.decode()

    checksum = get_checksum(file_decoded)

    # If we have the checksum, return it's value, else add the new checksum and count the words
    if checksum in results:
        result = results[checksum]
    else:
        result = count_words(file_decoded)
        results[checksum] = result

    return result

# Simple count of words saved to Dict as the value for a file checksum
def count_words(file: str) -> dict:
    words = file.split()
    word_lens = [len(word.strip(".,!?-=*[]{}()#_@:;£$%^`~/\\")) for word in words]
    word_count = len(words)
    avg_len = sum(word_lens) / word_count

    freq_lengths = {} # Get the most occuring word lengths
    for length in word_lens:
        freq_lengths[length] = freq_lengths.get(length, 0) + 1

    word_lens_counts = {"Number of words of length " + str(length): freq_lengths[length] for length in set(word_lens)}

    max_freq = max(freq_lengths.values())
    most_freq_lengths = list(set([length for length, freq in freq_lengths.items() if freq == max_freq]))
    most_freq_lengths_str = ' & '.join(map(str, most_freq_lengths)) # Making it pretty for the response

    return {
        'Word count': word_count,
        'Average word length': float(round(avg_len, 3)),
        'Number of words of length': word_lens_counts,
        f'The most frequently occurring word length is {len(most_freq_lengths)} for word lengths of': most_freq_lengths_str,
    }

