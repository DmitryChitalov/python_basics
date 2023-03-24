import subprocess
import chardet

websites = ["yandex.ru", "youtube.com"]

def ping_website(website):
    try:
        response = subprocess.check_output(
            ["ping", "-c", "4", website],
            stderr=subprocess.STDOUT
        )
        return response
    except subprocess.CalledProcessError as e:
        return e.output

for website in websites:
    print(f"Пингую сайт {website}...\n")
    response_bytes = ping_website(website)
    detected_encoding = chardet.detect(response_bytes)['encoding']
    response_str = response_bytes.decode(detected_encoding)
    print(response_str)
