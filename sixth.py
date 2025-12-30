
import sys
import requests


def download_url_and_get_all_hrefs(url):
    
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Stránku ne nepodařilo stáhnout")
    
    html = response.text
    hrefs = []

    for part in html.split('href="')[1:]:
        href = part.split('"')[0]
        hrefs.append(href)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        print(download_url_and_get_all_hrefs(url))
    
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
