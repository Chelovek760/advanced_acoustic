import requests

files = {'file': open('anomaly_id_01_00247_freq_37.wav', 'rb')}
r = requests.post('http://127.0.0.1:5001/', files=files)
print(r.content)
