import requests

url = "https://chat.openai.com/backend-api/conversation"

data = {
    "action": "next",
    "messages": [
        {
            "id": "27ba30d8-0cb2-48f3-83ae-23ad25124796",
            "role": "user",
            "content": {
                "content_type": "text",
                "parts": [
                    "test"
                ]
            }
        }
    ],
    "parent_message_id": "74659441-013a-42d0-8fe5-6c0ff9feb7dc",
    "model": "text-davinci-002-render"
}

headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJhdmVyeWJpc2t1cEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZ2VvaXBfY291bnRyeSI6IlVTIn0sImh0dHBzOi8vYXBpLm9wZW5haS5jb20vYXV0aCI6eyJ1c2VyX2lkIjoidXNlci1lUnNaUzkxYU5mOEJPTFYzSlUxMXRWbjMifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEzOTAzOTU1MjUzMDYxNzg5MjcxIiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjcwNTMwODc0LCJleHAiOjE2NzA2MTcyNzQsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb2ZmbGluZV9hY2Nlc3MifQ.wZpFNNOLuzeo03gt5-7unKMUeV1KRpI_BnVfdkENh607mw63N_0s5LLtSjBUQep0ClviJJjFU4ZHzZysox1WIb-Ng_kwqjyqHX65X8MCCQd77ktXT7dGlqxhkAoNzKIpK597m9NfhEF1MP9ebBhhmGW06REOEUXmsCRUP2nZyQIGG6YNB0Z3nCFoANkjvugRA863tizDgA55H_HvbF710ikWT1NpRmbCCVenyrfg2FBuPOw-tuAeYEAmpgHUEE5khsHb4IVNqD5cRB9e-a40Q6SR5B5pShf5YLLEnodOylKfC4S3A5EqoDPjjZ4zzbLQIhaM4jOUzCLzcbitEsStQA"}

res = requests.post(url, data=data, headers=headers)
print(res)
print(res.text)
