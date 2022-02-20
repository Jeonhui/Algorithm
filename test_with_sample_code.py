def test():
    import sys
    import requests
    from bs4 import BeautifulSoup as Soup

    problem_number = sys.stdin.readline().rstrip()
    soup = Soup(requests.get('https://www.acmicpc.net/problem/' + problem_number).text, 'html.parser')

    title = problem_number + ": " + soup.find('span', {'id': 'problem_title'}).text

    sample_input_list = []
    sample_output_list = []

    for i in range(1, 20):
        try:
            sample_input_list.append(soup.find('pre', {'id': 'sample-input-' + str(i)}).text.strip())
            sample_output_list.append(soup.find('pre', {'id': 'sample-output-' + str(i)}).text.strip())
        except:
            break

    print(title)
    for i in range(len(sample_input_list)):
        print("______________________")
        print("예제 입력 " + str(i + 1))
        print(sample_input_list[i])
        print("예제 출력 " + str(i + 1))
        print(sample_output_list[i])
        print("실행 결과")

        result = run_test(problem_number, sample_input_list[i])

        if sample_output_list[i].rstrip() == result.rstrip():
            print(result)
        else:
            print(result)
            print("틀렸습니다.")
            return
    print("______________________")
    print("맞았습니다.")


def run_test(problem_number, arv):
    import os
    import subprocess

    try:
        file = subprocess.Popen(
            ['python', os.getcwd() + '/solved/' + problem_number + ".py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
    except Exception as e:
        print("파일이 존재하지 않습니다.", e)
        return

    file.communicate(input=bytes(arv.rstrip(), encoding="utf-8"))
    out, err = file.communicate()

    return out.decode('utf-8').rstrip()


test()
