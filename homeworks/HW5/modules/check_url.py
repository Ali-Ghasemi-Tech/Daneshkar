import httpx
def check_url(url):
    try:
        req = httpx.get(url)
        return req
    except Exception:
        return False