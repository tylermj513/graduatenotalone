import requests
from bs4 import BeautifulSoup
import subprocess

file_path = 'timetime.py' 

def contains_string_in_url(url, target_string): 
    response = requests.get(url,verify=False)

    if response.status_code == 200: 
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser') 
        # Search for the target string in specific elements or attributes
        # For example, search within option tags
        options = soup.find_all('option')
        for option in options:
            if target_string in str(option):
                return True
        return False
    else: 
        print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")
        return False

def main():
    url = "https://affairs-guesths.vm.nthu.edu.tw/guest10/index.php?liveFromYear=2024&liveFromMonth=04&liveFromDay=5&liveEndYear=2024&liveEndMonth=4&liveEndDay=5"
    target_string = "<option>1</option>"

    while not contains_string_in_url(url, target_string):
        print(f"The HTML content of {url} does not contain '{target_string}'. Retrying...")
    
    print(f"The HTML content of {url} contains '{target_string}'. Program exiting.")
    subprocess.run(['python', file_path], check=True)
if __name__ == '__main__':
    main()

 