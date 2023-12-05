import requests
import re

def get_subheadings(url):
    response = requests.get(url)
    html_content = response.text
    subheadings = re.findall(r'<h3>(.*?)</h3>', html_content)
    return subheadings

# Пример использования
url = 'http://www.columbia.edu/~fdc/sample.html'  # Укажите URL-адрес сайта, с которого вы хотите получить подзаголовки
subheadings = get_subheadings(url)
print(subheadings)

