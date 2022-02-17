# developed by Jeonhui Lee

def get_result():
    import requests
    from bs4 import BeautifulSoup as Soup

    number = input("problem id: ")
    result = ["채점 결과"]
    break_result = ["맞았습니다!!", "틀렸습니다", "컴파일 에러"]

    while result[-1] not in break_result:
        try:
            req = requests.get('https://www.acmicpc.net/status?user_id=whas02&problem_id=' + number + '&from_mine=1')
            result.append(Soup(req.text, 'html.parser').find("td", "result").text)
        except Exception:
            print("채점 중이지 않습니다.")
            break
        print(result[-1])
        print(result[-1] if (len(result) > 2 and result[-1] != result[-2]) else "")

    if result[-1] == "맞았습니다!!":
        git_push(number)


def git_push(number):
    import os
    from github import Github
    from github import InputGitTreeElement

    g = Github("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")
    # token으로 github에 접속

    repo = g.get_repo("Jeonhui/baekjoon")
    # repository 설정

    commit_message = input("commit message: ")

    repo_ref = repo.get_git_ref("heads/main")
    repo_sha = repo_ref.object.sha
    base_tree = repo.get_git_tree(repo_sha)
    # push를 위한 설정

    file_path = "solved/" + number + ".py"
    # 파일 경로
    # InputGitTreeElement에 넣기 위해 repository 안 경로로 설정

    with open(os.getcwd() + "/" + file_path, 'r') as file:
        data = file.read()
        print(data)
        element = InputGitTreeElement(file_path, '100644', 'blob', data)
        # 파일 내용 element 저장

    tree = repo.create_git_tree([element], base_tree)
    parent = repo.get_git_commit(repo_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    repo_ref.edit(commit.sha)
    # push




git_push("2525")
