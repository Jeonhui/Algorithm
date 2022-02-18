# developed by Jeonhui Lee
# pip3 install pygithub
# pip3 install requests

'''
baekjoon_id = 백준_ID
token = Githubtoken
repository = 'user_name/repository'
ex) 'Jeonhui/baekjoon'
user_github_file_path = github에 저장할 경로
user_file_path = 파일 경로

default -> '_'
    user_github_file_path = 'solved/'
    user_file_path = '현재 위치/solved/'

문제 번호 입력 시 - 결과 출력 및 파일 push
p 입력 시 - 파일 push
'''

import sys

baekjoon_id = 'baekjoon_id'
token = 'ghp_~'
repository = 'user_name/repository'
user_github_file_path = '_'
user_file_path = '_'


def get_result():
    import requests
    from bs4 import BeautifulSoup as Soup
    print("problem number: ", end="")
    problem_number = sys.stdin.readline().rstrip()
    if problem_number == 'p':
        print("push file_name: ", end="")
        file_name = sys.stdin.readline().rstrip()
        git_push(file_name)
        return
    result = ["채점 결과"]
    break_result = ["맞았습니다!!", "틀렸습니다", "컴파일 에러"]

    try:
        req = requests.get('https://www.acmicpc.net/status?user_id=' + baekjoon_id + '&problem_id=' + problem_number)
        soup = Soup(req.text, 'html.parser')
        # soup를 이용해 html 가져오기
        if soup.find('input', {'name': 'problem_id'}).get('value') != "":
            # problem_id가 ""이 나오면 해당 문제가 없음
            while result[-1] not in break_result:
                try:
                    result.append(soup.find("td", "result").text)
                    # result의 값을 가져오기

                except Exception:
                    print("채점 결과가 없습니다.")
                    return
                    # 값을 가져오지 못하면 결과가 없는 것

                if len(result) >= 2 and result[-1] != result[-2]:
                    print(result[-1])
                    # 결과 출력
        else:
            print("문제가 존재하지 않습니다.")
            return

    except Exception as e:
        print("Error:", e)
        return
    try:
        soup = Soup(requests.get('https://www.acmicpc.net/problem/'+problem_number).text, 'html.parser')
        title = problem_number +": " + soup.find('span', {'id': 'problem_title'}).text
    except Exception:
        title = ""

    if result[-1] == "맞았습니다!!":
        git_push(problem_number, title)


def git_push(file_name, *title):
    import os
    from github import Github
    from github import InputGitTreeElement
    try:
        g = Github(token)
        # token github에 접속
        repo = g.get_repo(repository)
        # repository 설정
        repo_ref = repo.get_git_ref("heads/main")
        repo_sha = repo_ref.object.sha
        base_tree = repo.get_git_tree(repo_sha)
        # push를 위한 설정

    except Exception:
        print("잘못된 접근입니다. (token or repository)")
        return

    github_file_path = ("solved/" if user_github_file_path == "_" else user_github_file_path) + file_name + ".py"
    # 파일 경로 (github)
    # InputGitTreeElement에 넣기 위해 repository 안 경로로 설정
    if user_file_path == "_":
        file_path = os.getcwd() + "/solved/" + file_name + ".py"  # default
    else:
        file_path = user_file_path + ("/" if user_file_path[-1] != "/" else "") + file_name + ".py"
    # 내 컴퓨터의 파일 경로

    print("a:", github_file_path)
    print("b:", file_path)

    try:
        with open(file_path, 'r') as file:
            data = file.read()

            print()
            print("source code")
            print(file_path)
            print("____________________________")
            print(data)
            print("____________________________\n")

            element = InputGitTreeElement(github_file_path, '100644', 'blob', data)
            # 파일 내용 element 저장

            try:
                if len(title) != 0:
                    commit_message = title[0]
                else:
                    print("commit message: ", end="")
                    commit_message = sys.stdin.readline().rstrip()
                tree = repo.create_git_tree([element], base_tree)
                parent = repo.get_git_commit(repo_sha)
                commit = repo.create_git_commit(commit_message, tree, [parent])
                repo_ref.edit(commit.sha)
                print("Push에 성공했습니다.")
                # push
            except Exception:
                print("Push에 실패했습니다.")
                return
    except Exception:
        print("파일이 존재하지 않습니다.")
        return


get_result()
