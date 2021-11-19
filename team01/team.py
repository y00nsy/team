#전역


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
# 아이디를 입력받는
def input_id():
    return input('아이디 >> ') 
# 비번을 입력받는
def input_pw():
    return input('비밀번호 >> ') 



#아이디로 정보를 찾아오는
def find_login(id):
    for already_user in user_list:
        if id == already_user['id']:
            return already_user
    return {}
    
def login():
    find_id = input_id()
    already_user = find_login(find_id)

    if len(already_user) > 0:
        in_pw = input_pw() # 방금 입력한 비번
        real_pw = already_user['pw']
            
        while True:
            if in_pw == real_pw:
                print('{}님, 로그인에 성공하셨습니다.'.format(already_user['id']))
                return True
            else :
                print('비밀번호가 틀렸습니다.')
            # 도서목록
            #pass
    else:
        ('가입되지 않은 정보입니다.')
    


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
            is_login = login()

            if is_login:
                # is_login이 True => 도서 등록 메뉴로 전환
                pass
        # 리스트에 정보 없을때 회원가입 시키는거
        elif menu == 3:
            exit_program()
        
            

    


