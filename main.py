from bs4 import BeautifulSoup
import requests, re, json


list_url= ['https://vladimir.mukomoloff.ru']
list_check_tag = ['title', 'description', 'keywords', 'h1', 'h2', 'h3']
list_page_content = []
filter_url = ['http', 'tel:', 'mailto','.jpg', '.jpeg', '.png', '.gif', '.pdf', '.webp', 'sort=', 'order=', 'display=']
num = 0

def create_content(soup, url):
    content = {
        'url': url
    }

    for tag in list_check_tag:
        content[tag] = []
        tags = soup.find_all(tag)
        match len(tags):
            case 0:
                try:
                    content[tag] = soup.find('meta', attrs={'name': tag})['content']
                except TypeError:
                    content[tag] = None
            case 1:
                content[tag] = tags[0].text
            case _:
                for item in tags:
                    content[tag].append(item.text)
    
    return content

def check_content(content, *search):
    for tag in list_check_tag:
        if content[tag] != None:
            if type(content[tag]) == list:
                for item in content[tag]:
                    if re.search(r'|'.join(search), item):
                        return True
            else:
                if re.search(r'|'.join(search), content[tag]):
                    return True
    return False


while True:
    try:
        url = list_url[0] + list_url[num] if len(list_url) > 1 else list_url[0]
        page = requests.get(url)
        print('Checking: ' + url)
    except IndexError:
        break
    except requests.exceptions.InvalidURL:
        num += 1
        continue
    
    soup = BeautifulSoup(page.text, 'html.parser')
    page_content = create_content(soup, url)

    if check_content(page_content, 'Москв'):
        list_page_content.append(page_content)

    
    for tag in soup.find_all('a'):
        href = tag.get('href')
        slag = re.search(r'|'.join(filter_url), href) if href else True
        if not slag and href not in list_url:
            list_url.append(href)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(list_page_content, file, indent=4, ensure_ascii=False)

    num += 1