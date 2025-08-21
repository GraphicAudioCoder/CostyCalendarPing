import requests

url = "https://huozynweugrmuecxrsyt.supabase.co/rest/v1/appointments?select=id"
headers = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1b3p5bndldWdybXVlY3hyc3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU2NTk2NjQsImV4cCI6MjA3MTIzNTY2NH0.6V9X_of9YDYw2u9g8MWAMFDdTGWtd1Eb67rWBE98PqM",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh1b3p5bndldWdybXVlY3hyc3l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU2NTk2NjQsImV4cCI6MjA3MTIzNTY2NH0.6V9X_of9YDYw2u9g8MWAMFDdTGWtd1Eb67rWBE98PqM"
}

try:
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print("Ping riuscito!")
    else:
        print("Errore ping:", r.status_code)
except Exception as e:
    print("Errore:", e)
