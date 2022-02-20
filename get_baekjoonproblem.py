# developed by Jeonhui Lee
# pip3 install requests
# pip3 install bs4

def get_baekjoonproblem():
    import sys
    import requests
    from bs4 import BeautifulSoup as Soup
    problem_number = sys.stdin.readline().rstrip()
    try:
        soup = Soup(requests.get('https://www.acmicpc.net/problem/' + problem_number).text, 'html.parser')
        title = problem_number + ": " + soup.find('span', {'id': 'problem_title'}).text
        print(title)
    except Exception as e:
        print("잘못된 문제 번호입니다.", e)
        return
    description = soup.find('div', {'id': 'problem_description'}).text.strip()
    input_explantion = soup.find('div', {'id': 'problem_input'}).text.strip()
    output_explantion = soup.find('div', {'id': 'problem_output'}).text.strip()
    print("[문제]")
    print(description)
    print("[입력]")
    print(input_explantion)
    print("[출력]")
    print(output_explantion)
    print()

    sample_input_list = []
    sample_output_list = []

    for i in range(1, 20):
        try:
            sample_input_list.append(soup.find('pre', {'id': 'sample-input-' + str(i)}).text.strip())
            sample_output_list.append(soup.find('pre', {'id': 'sample-output-' + str(i)}).text.strip())
        except:
            break

    for i in range(len(sample_input_list)):
        print("예제 입력 "+ str(i+1))
        print(sample_input_list[i])
        print("예제 출력 " + str(i + 1))
        print(sample_output_list[i])
        print()

get_baekjoonproblem()
