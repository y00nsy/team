#전역

# id_list=[]  #회원가입하면 저장될 아이디 리스트
# pw_list=[]  #회원가입하면 저장될 비번 리스트

user_list = [
    {
        "id": "abc123",
        "pw": "1234!",
        "name": "김철수"
    },
    {
        "id": "def123",
        "pw": "5432!",
        "name": "홍길동"
    }
]


#함수 정의부

#첫 회원가입/로그인 화면 보여주기
def show_first():
    print("\n\n====== 도서 재고관리 프로그램 ======")
    print('1. 신규 직원 등록하기')
    print('2. 기존 직원 로그인하기')
    print('3. 프로그램 종료하기')

#중복을 확인하는 함수(아이디)
def check_duplicate_code_id():
    while True:

        code = input('아이디 >> ')
        flag = False  # 중복 플래그

        # 제품번호 중복검증
        for u in user_list:
            if code == u['id']:

                # 중복된 경우
                print('\n# 아이디가 이미 존재합니다. 다시 입력하세요.')
                flag = True
                break
        if flag == False:
            return code     # 중복안된 제품번호


# 신규직원등록 (회원가입)
def insert_id_pw():    
    
    user = {}
    print('\n>>> 신규 직원 등록을 시작합니다.')
    user['id'] = check_duplicate_code_id()
    user['pw'] = input('비밀번호 >> ')
    user['name'] = input('이름 >> ')

    user_list.append(user)
    
    print('\n회원가입이 완료되었습니다.')

# 기존 직원 로그인



#프로그램 종료처리하기
def exit_program():
    import sys
    print('\n# 프로그램을 종료합니다. [Y/N]')
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return

    





#실행부
if __name__ == '__main__':
    
    while True:
        show_first()
        
        menu = int(input('\n >>> '))
        if menu == 1:
            insert_id_pw()
        elif menu == 2:
            pass
        else:
            exit_program()

    


