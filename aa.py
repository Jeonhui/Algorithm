import requests

with requests.Session() as s:
    req = s.get('https://www.acmicpc.net/submit/3052')
    html = req.text
    # HTTP Header 가져오기
    header = req.headers
    print(header)
    status = req.status_code
    is_ok = req.ok
    print(is_ok)
