# developed by Jeonhui Lee
# pip3 install requests
# pip3 install bs4

'''
Baekjoon 입출력 예제 테스트 프로그램
'''

'''
user_file_path = 테스트해 볼 python 파일의 위치
 "_"일 시에 기본 경로 (현재 파일위치/solved/)
'''

user_file_path = "_"


def test():
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
    except Exception as e:
        # 잘못된 입력이 들어왔을 시에 problem_tilte을 찾지 못함 -> 종료
        print("잘못된 문제 번호입니다.", e)
        return

    # 입출력 예제을 저장할 배열
    sample_input_list = []
    sample_output_list = []

    # 최대 20번까지 반복하고 더이상 없으면 for문을 빠져나옴
    for i in range(1, 20):
        try:
            sample_input_list.append(soup.find('pre', {'id': 'sample-input-' + str(i)}).text.strip())
            sample_output_list.append(soup.find('pre', {'id': 'sample-output-' + str(i)}).text.strip())
        except:
            break

    # 입출력 예제  출력
    print(title)
    for i in range(len(sample_input_list)):
        print("______________________")
        print("예제 입력 " + str(i + 1))
        print(sample_input_list[i])
        print("예제 출력 " + str(i + 1))
        print(sample_output_list[i])
        print("실행 결과")

        # run_test함수 호출
        result = run_test(problem_number, sample_input_list[i])

        if sample_output_list[i].rstrip() == result.rstrip():
            print(result)
        else:
            print(result)
            print("틀렸습니다.")
            return
    print("______________________")
    print("맞았습니다!!")


def run_test(problem_number, sample_input):
    import os
    import subprocess

    # 사용자 경로를 지정하지 않았으면 기본 경로로 설정
    # 마지막에 /가 없다면 추가
    file_path = (os.getcwd() + '/solved/') if user_file_path != "_" else user_file_path
    if file_path[-1] != "/":
        file_path = file_path + "/"

    try:
        # 파일 경로의 파이썬 파일을 subprocess로 open
        file = subprocess.Popen(
            ['python', file_path + problem_number + ".py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
    except Exception as e:
        print("파일이 존재하지 않습니다.", e)
        return

    # subprocess 실행된 파일에 sample_input 전달
    file.communicate(input=bytes(sample_input.rstrip(), encoding="utf-8"))
    # subprocess 실행된 파일의 출력을 가져옴
    out, err = file.communicate()

    # 출력값 반환
    return out.decode('utf-8').rstrip()


test()
