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


book_store = [
    {
        '책번호': 'a001',
        '책이름': '삼국지',
        '가격': 9000,
        '수량': 2,
        '총액': 18000
    },
    {
        '책번호': 'a002',
        '책이름': '해리포터',
        '가격': 8000,
        '수량': 6,
        '총액': 48000
    },
    {
        '책번호': 'a003',
        '책이름': '반지의제왕',
        '가격': 7500,
        '수량': 2,
        '총액': 15000
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

        code = input('\n아이디 >> ')
        flag = False  # 중복 플래그

        # 제품번호 중복검증
        for u in user_list:
            if code == u['id']:

                # 중복된 경우
                print('\n!!! 아이디가 이미 존재합니다. 다시 입력하세요 !!!')
                flag = True
                break
        if flag == False:
            return code     # 중복안된 제품번호


# 신규직원등록 (회원가입)
def insert_id_pw():    
    
    user = {}
    print('\n>>> 신규 직원 등록을 시작합니다.')
    print('>>> (영문/숫자/문자로 입력해주세요)')
    user['id'] = check_duplicate_code_id()
    user['pw'] = input('비밀번호 >> ')
    user['name'] = input('이름 >> ')

    user_list.append(user)
    
    print('\n>> 회원가입이 완료되었습니다. <<')

# 기존 직원 로그인
# 아이디를 입력받는
def input_id():
    return input('\n아이디 >> ') 
# 비번을 입력받는
def input_pw():
    return input('비밀번호 >> ') 



#아이디로 정보를 찾아오는
def find_login(find_id):
    for already_user in user_list:
        if find_id == already_user['id']:
            return already_user
    return {}

'''
#비밀번호로 정보를 찾아오는
def find_login(find_pw):
    for already_user in user_list:
        if find_pw == already_user['pw']:
            return already_user
    return {}
'''

# 로그인 하는
def login():
    find_id = input_id()
    already_user = find_login(find_id)
    
    
    if len(already_user) > 0:            
        in_pw = input_pw() # 방금 입력한 비번
        real_pw = already_user['pw']
                            
        while True:
            if in_pw == real_pw:
                print('>> {}님, 로그인에 성공하셨습니다. <<'.format(already_user['id']))
                return True
            else :
                print('\n!!! 비밀번호를 잘못 입력했습니다 !!!')
                # 도서목록
                break

                
                                
    else:
        print('\n!!! 가입되지 않은 정보입니다 !!!')
           
######################################################################################
   
# 로그인 이후 나오는 도서 재고관리 프로그램
# 로그인 이후 나오는 메뉴 출력함수
def show_second():
    print("\n\n=========================")
    print('# 1. 신규 도서 등록하기')
    print('# 2. 모든 도서 조회하기')
    print('# 3. 개별 도서 조회하기')
    print('# 4. 도서 정보 수정')
    print('# 5. 도서 정보 삭제')
    print('# 6. 프로그램 종료')

# 도서 번호의 중복을 확인하는 함수
def check_book_code():
    while True:
        print('>>> 도서번호 예시: a001, a002, ...')
        book_code = input('\n도서 번호 >> ')

        flag = False

        for b in book_store:
            if book_code == b['책번호']:
                print('\n!!! 도서 번호가 중복되었습니다. 다시 입력하세요 !!!')
                flag = True
                break
        if flag == False:
            return book_code


# 신규 도서 등록 함수
def ipt_book():
    book = {}
    print('\n>>> 도서 정보 등록을 시작합니다.')

    book['책번호'] = check_book_code()
    book['책이름'] = input('도서명 >> ')
    book['가격'] = int(input('가격 >> '))
    book['수량'] = int(input('수량 >> '))
    book['총액'] = book['가격'] * book['수량']

    book_store.append(book)
    print('\n>> 신규 도서가 등록되었습니다. <<')

# 도서정보 출력 머리말
def books_header():
    print('\n\n\t\t ***** 도서 재고 조회 *****')
    print('=' * 60)
    print('{:<7s}{:^12s}{:^10s}{:^7s}{:^12s}'.format('책번호','책이름','가격','수량','총액'))
    print('=' * 60)
    
# 전체 도서정보를 출력하는 함수
def all_books():
    books_header()

    total_price =0
    for book in book_store:
        total_price += book['총액']
        print('{:<7s}{:^16s}{:>8d}원{:>7d}개{:>12d}원'.format(book['책번호'],book['책이름'],book['가격'],book['수량'],book['총액']))
    print('=' * 60)
    print(f'\t\t도서 재고 총액: {total_price}원')

# 도서번호를 입력받는 함수
def input_code(msg):
    print(f'\n\n>> {msg}하실 제품의 번호를 입력하세요')
    print('>> 도서번호 예시: a001, a002, ...')
    book_code = input('도서번호 >> ')
    return book_code


# 도서번호로 해당 제품을 찾아오는 함수
def search_code(book_code):
    for book in book_store:
        if book_code == book['책번호']:
            return book
    return {}

# 개별 도서 정보 조회
def search_book():
    book_code = input_code('조회')
    book = search_code(book_code)   
    
    if len(book) > 0:
        books_header()
        print('{:<7s}{:^16s}{:>8d}원{:>7d}개{:>12d}원'.format(book['책번호'],book['책이름'],book['가격'],book['수량'],book['총액']))
        print('=' * 60)
    else:
        print('\n!! 존재하지 않는 도서입니다. !!')

# 도서 정보 수정하기
def modify_book():
    book_code = input_code('수정')
    book = search_code(book_code)

    if len(book) > 0:
        print('\n# [{}] {}의 정보를 수정합니다.'.format(book['책번호'],book['책이름']))
        print('[ 1. 수량 변경 | 2. 단가 변경 | 3. 일괄 변경 | 4. 취소 ]')
        select = int(input('=> '))
        if select == 1:         
            book['수량'] = int(input('=> 수정할 수량({}) >> '.format(book['수량'])))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')
        elif select == 2:
            book['가격'] = int(input('=> 수정할 가격({}) >> '.format(book['가격'])))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')
        elif select == 3:
            book['수량'] = int(input('=> 수정할 수량({}) >> '.format(book['수량'])))
            book['가격'] = int(input('=> 수정할 가격({}) >> '.format(book['가격'])))
            print('\n>> 정보수정이 정상 처리되었습니다. <<')
        else:
            print('# 변경을 취소합니다.')
        book['총액'] = book['가격'] * book['수량']
    else:
        print('\n!! 존재하지 않는 도서입니다. !!')

# 도서정보 삭제 처리 함수
def delete_book():
    book_code = input_code('삭제')
    book = search_code(book_code)

    if len(book) > 0:
        book_store.remove(book)
        print('\n>> 도서가 정상 삭제되었습니다. <<')
    else:
        print('\n!! 존재하지 않는 도서입니다. !!')
        

##################################################################################

#프로그램 종료처리하기
def exit_program():
    import sys
    print('\n>> 프로그램을 종료합니다. [Y/N]')
    answer = input('>> ')
    if answer.lower()[0] == 'y':
        sys.exit()
    else:
        return

############################################################################

#실행부
if __name__ == '__main__':
    
    while True:
        show_first()
        
        menu = int(input('\n>>> '))
        
        if menu == 1:
            insert_id_pw()
        elif menu == 2:
            
            is_login = login()


            if is_login:
                # is_login이 True => 도서 등록 메뉴로 전환
                while True:
                    show_second()
                    book_info = int(input('\n>>> '))

                    if book_info == 1:
                        ipt_book()
                    elif book_info == 2:
                        all_books()
                    elif book_info == 3:
                        search_book()
                    elif book_info == 4:
                        modify_book()
                    elif book_info == 5:
                        delete_book()
                    elif book_info == 6:
                        exit_program()
                    else:
                        print('!! 메뉴를 잘못 입력했습니다. !!')

                    input('\n>> 메뉴화면으로 돌아가시려면 Enter를 누르세요.')

        # 리스트에 정보 없을때 회원가입 시키는거
        elif menu == 3:
            exit_program()
        else:
            print('!! 메뉴를 잘못 입력했습니다. !!')

        input('\n>> 메뉴화면으로 돌아가시려면 Enter를 누르세요.')
        
            

    

