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