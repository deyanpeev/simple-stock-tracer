from github import Github
import base64

github_account = Github("")
repo = github_account.get_user().get_repo('simple-stock-tracer')

repo.create_file("data/filename3.txt", "commit 513124", "new content", branch="main")

# contents = repo.get_contents("data/filename3.txt")
# repo.update_file(contents.path, "Commit id", base64.b64decode(contents.content).decode() + "\n" + "more conent 6", contents.sha, branch="main")
# print(base64.b64decode(contents.content).decode())