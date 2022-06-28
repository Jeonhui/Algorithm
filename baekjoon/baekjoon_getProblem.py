# developed by Jeonhui Lee
# pip3 install requests
# pip3 install bs4

'''
Baekjoon 문제 번호로 문제 불러오기
'''

def get_baekjoonproblem():
    import sys
    import requests
    from bs4 import BeautifulSoup as Soup

    problem_number = sys.stdin.readline().rstrip()
    # 문제 번호 입력

    try:
        soup = Soup(requests.get('https://www.acmicpc.net/problem/' + problem_number).text, 'html.parser')
        # 문제 주소의 html 파일을 text로 불러옴
        title = problem_number + ": " + soup.find('span', {'id': 'problem_title'}).text
        # id가 problem_title인 span태그를 찾음
        print(title)

    except Exception as e:
        # 잘못된 입력이 들어왔을 시에 problem_tilte을 찾지 못함 -> 종료
        print("잘못된 문제 번호입니다.", e)
        return

    description = soup.find('div', {'id': 'problem_description'}).text.strip()
    input_explantion = soup.find('div', {'id': 'problem_input'}).text.strip()
    output_explantion = soup.find('div', {'id': 'problem_output'}).text.strip()
    # 각각 id가 problem_description, problem_input, problem_out인 div 태그를 찾음

    # 출력
    print("[문제]")
    print(description)
    print("[입력]")
    print(input_explantion)
    print("[출력]")
    print(output_explantion)
    print()

    # 입출력 예제을 저장할 배열
    sample_input_list = []
    sample_output_list = []

    # 최대 20번까지 반복하고 더이상 없으면 for문을 빠져나옴
    for i in range(1, 20):
        try:
            sample_input_list.append(soup.find('pre', {'id': 'sample-input-' + str(i)}).text.strip())
            sample_output_list.append(soup.find('pre', {'id': 'sample-output-' + str(i)}).text.strip())
            # 입출력 예제를 가져와서 배열에 저장
        except:
            break

    # 입출력 예제  출력
    for i in range(len(sample_input_list)):
        print("예제 입력 " + str(i + 1))
        print(sample_input_list[i])
        print("예제 출력 " + str(i + 1))
        print(sample_output_list[i])
        print()


get_baekjoonproblem()
