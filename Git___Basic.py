# 작업 디렉토리 생성
'''
	1. 작업 및 파일 관리를 위한 경로 생성 후, 해당 경로로 작업 디렉토리 설정
	2. 해당 디렉토리에 대한 사용자 정보 설정
	3. 깃 초기화
'''

mkdir	[작업 경로명]
cd		[작업 경로명]

# --local, --global 옵션을 통해 사용자 정보 값을 해당 경로에 대해서만 설정할 것인지, PC의 전체 git 저장소에 대해서 설정할 것인지 설정 가능
git config --local user.name [사용자명]
git config --global user.email [사용자 이메일]
git config --global init.defaultBranch main

git init


# branch 명 변경
'''
	git branch: 브랜치를 관리하는 깃 명령어 (추가 명령어 없이 사용시 브랜치명 확인 기능)
	git remote: 원격저장소와 관련된 작업 명령어
'''
git branch # 현재의 브랜치명 확인

git branch -m [변경전 브랜치명] [변경후 브랜치명]
git fetch origin

git branch -u [원격저장소]/[브랜치명] [로컬 브랜치명] # 원격 저장소 origin의 main 브랜치와 로컬 브랜치 main을 연결
git remote set-head [원격저장소] -a # set-head: 원격 저장소의 HEAD를 설정하는 서브 명령어



# 깃 - 깃허브 연동
'''
	PC에서 디렉토리 생성 및 깃 활성화 후에 깃허브와 연동하는 방법

	1. 깃허브에서 레포지토리 생성 후, url 카피
	2. 해당 디렉토리에 원격 저장소 연결

	* 처음 git repository 생성 뒤 기본 branch 생성을 안해줬기 때문에 발생하는 오류
	  커맨드를 통해 기본 branch 설정을 해줘야 한다.
'''

git remote add origin [url]
# fatal: The current branch main has no upstream branch. To push the current branch and set the remote as upstream, use git push --set-upstream origin main
# 깃허브 연동 후 첫 커밋 후 push시에 위의 에러 발생
git push --set-upstream origin main # 로컬 저장소(origin)의 원격 저장소를 (main)으로 지정하여 push

# 초기단계에서의 깃허브와 연동
rm -rf .git/
git init
git remote add origin [url]
git commit -m [msg]
git push -f origin main # -f force


# 깃 기본 커맨드 및 사용 프로세스
'''
	1 . git status: 현재 저장소의 상태를 확인하는 기능
		- Untracked files: 아직 한 번도 버전 관리하지 않은 파일의 리스트
		- Changes not staged for commit: 변경 후 아직 스테이징이 안된 파일의 리스트
	2 . git add [file_name]: 스테이지 영역에 파일을 올리는 기능
		- Changes to be committed: 커밋시 변동될 파일 리스트
	3 . git commit -m "[기록 메모]": 스테이지 영역에 있는 파일을 저장소에 업데이트 하는 기능
		git commit --amend : 가장 최근의 커밋 메시지 수정
		git commit -am ""
	4 . git push [remote] [branch]: 로컬 브랜츠의 결과를 원격 저장소에 업데이트 하는 기능
	5 . git log: 저장소에 저장된 버전 확인
		git log --stat: 변경 내용까지 조회
	6 . git diff: 수정 파일의 변경된 부분을 확인할 수 있는 기능
	7 . git rm [file_name]: 레포지토리에 올라가 있는 파일 제거
	8 . git mv [old_name] [new_name]: 레포지토리에 올라가 있는 파일명 변경
	9 . git restore [file_name]: 최근 커밋으로 해당 파일을 되돌림
		git restore --source [git_hash] [file_name]: 특정 커밋 시점(git_hash)으로 해당 파일을 되돌림
		git restore --staged [file_name]: 스테이징된 특정파일의 스테이징을 취소함
	10. git reset --hard [git_hash]: 특정 커밋 시점으로 완전히 돌아감
		git reset --soft [git_hash]: soft의 경우, 커밋과 스테이징에서는 사라지지만 작업 공간에서의 파일은 그대로 유지되어 있는 상태로 돌아간다.
	11. git revert [git_hash]: 특정 커밋(git_hash)을 취소하는 기능, 복수의 커밋 아이디 입력 가능
'''

git status
git add [file_name]
git commit -m "[기록 메모]"
# git commit -am "[기록 메모]" (add와 commit을 한 번에 수행하는 커맨드)
git commit -ammend
# vi 창이 뜨며, 메세지를 수정한 후에 vi창을 종료하면 변경이 입력된다.
git push origin main


git log (--stat)
'''
	# HEAD -> main : 지역 저장소(HEAD)의 최종 커밋
	# origin/main	 : 원격 저장소(origin)의 최종 커밋
	commit f1c7ec998f1140094eda96f0028caabbdd60cb3a (HEAD -> main, origin/main)
	Author: iop2000win <nowplerin@gmail.com>
	Date:   Wed Aug 30 11:45:56 2023 +0900

		test # commit message

	commit 00b4f645985695351a62c7389ab8350cd232c443 # 커밋해시(깃해시) - 커밋에 대한 아이디
	Author: iop2000win <nowplerin@gmail.com>
	Date:   Wed Aug 30 11:44:35 2023 +0900

		Upload Git basic files

	(
	 vi_text.txt | 3 +++
 	 1 file changed, 3 insertions(+)
	) # git log 옆에 --stat을 입력해줄 경우, 변경된 이력도 함께 조회할 수 있다.

	- main : 레파지토리의 기본 브랜치
	다른 브랜치에서 작업을 진행한 후에, main 브랜치로 합쳐주는 방식으로 협업이 진행된다.
'''

git diff
'''
-git init
\ No newline at end of file
+git init

위와 같이 -(붉은 색), +(초록 색)으로 파일의 변경된 부분을 확인할 수 있다.
'''


# tracked & untracked file
'''
	On branch main
	Your branch is up to date with 'origin/main'.

	Changes not staged for commit:
	  (use "git add <file>..." to update what will be committed)
	  (use "git restore <file>..." to discard changes in working directory)
	        modified:   Git___Basic.py
	        modified:   git_test.txt # tracked files

	Untracked files:
	  (use "git add <file>..." to include in what will be committed)
	        git_test2.txt # untracked files

	no changes added to commit (use "git add" and/or "git commit -a")
'''


# 버전 관리 제외
'''
특정한 파일이나 경로에 대해서는 깃을 통한 버전관리를 하고싶지 않을 경우,
.gitignore 파일을 통해서 비대상 데이터를 설정할 수 있다.

.gitignore 파일 안에 제외할 파일들에 대한 정보를 입력하면, add 시에 처리되지 않는다.
'''
touch .gitignore
vi .gitignore
