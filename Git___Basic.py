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

git init


# 깃 - 깃허브 연동
'''
	PC에서 디렉토리 생성 및 깃 활성화 후에 깃허브와 연동하는 방법

	1. 깃허브에서 레포지토리 생성 후, url 카피
	2. 해당 디렉토리에 원격 저장소 연결

	* 처음 git repository 생성 뒤 기본 branch 생성을 안해줬기 때문에 발생하는 오류
	  커맨드를 통해 기본 branch 설정을 해줘야 한다.
'''

git remote add origin [url]
# fatal: The current branch master has no upstream branch. To push the current branch and set the remote as upstream, use git push --set-upstream origin master
# 깃허브 연동 후 첫 커밋 후 push시에 위의 에러 발생
git push --set-upstream origin master

# 초기단계에서의 깃허브와 연동
rm -rf .git/
git init
git remote add origin [url]
git commit -m [msg]
git push -f origin master # -f force


# 깃 기본 커맨드 및 사용 프로세스
'''
	1. git status: 현재 저장소의 상태를 확인하는 기능
		- Untracked files: 아직 한 번도 버전 관리하지 않은 파일의 리스트
		- Changes not staged for commit: 변경 후 아직 스테이징이 안된 파일의 리스트
	2. git add [file_name]: 스테이지 영역에 파일을 올리는 기능
		- Changes to be committed: 커밋시 변동될 파일 리스트
	3. git commit -m "[기록 메모]": 스테이지 영역에 있는 파일을 저장소에 업데이트 하는 기능
	4. git push [remote] [branch]: 로컬 브랜츠의 결과를 원격 저장소에 업데이트 하는 기능
	5. git log: 저장소에 저장된 버전 확인
	6. git diff: 수정 파일의 변경된 부분을 확인할 수 있는 기능
'''

git status
git add [file_name]
git commit -m "[기록 메모]"
# git commit -am "[기록 메모]" (add와 commit을 한 번에 수행하는 커맨드)
git push origin master


git log
'''
	# HEAD -> master : 지역 저장소(HEAD)의 최종 커밋
	# origin/master	 : 원격 저장소(origin)의 최종 커밋
	commit f1c7ec998f1140094eda96f0028caabbdd60cb3a (HEAD -> master, origin/master)
	Author: iop2000win <nowplerin@gmail.com>
	Date:   Wed Aug 30 11:45:56 2023 +0900

		test

	commit 00b4f645985695351a62c7389ab8350cd232c443 # 커밋해시(깃해시) - 커밋에 대한 아이디
	Author: iop2000win <nowplerin@gmail.com>
	Date:   Wed Aug 30 11:44:35 2023 +0900

		Upload Git basic files

	- master : 레파지토리의 기본 브랜치
	다른 브랜치에서 작업을 진행한 후에, master 브랜치로 합쳐주는 방식으로 협업이 진행된다.
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
	On branch master
	Your branch is up to date with 'origin/master'.

	Changes not staged for commit:
	  (use "git add <file>..." to update what will be committed)
	  (use "git restore <file>..." to discard changes in working directory)
	        modified:   Git___Basic.py
	        modified:   git_test.txt

	Untracked files:
	  (use "git add <file>..." to include in what will be committed)
	        git_test2.txt

	no changes added to commit (use "git add" and/or "git commit -a")
'''