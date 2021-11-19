#전역
id_list=[]  #회원가입하면 저장될 아이디 리스트
pw_list=[]  #회원가입하면 저장될 비번 리스트



#함수 정의부

#첫 회원가입/로그인 화면 보여주기
def show_first():
    print("\n\n====== 도서 재고관리 프로그램 ======")
    print('1. 신규 직원 등록하기')
    print('2. 기존 직원 로그인하기')
    print('3. 프로그램 종료하기')

#중복을 확인하는 함수

# 신규직원등록 (회원가입)
def insert_id():    
    get_id = {}
    print('\n>>> 신규 직원 등록을 시작합니다.')



    

    
    

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
            pass
        elif menu == 2:
            pass
        else:
            exit_program()

    


