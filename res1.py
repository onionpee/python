import time
import os
import random
import enemy

number = [1, 2, 3, 4, 5]
selector = []

print('-----------------------------------------------------')
print('n가지 게임을 모두 수행해야 이기는 게임입니다.')
print('모든 게임을 수행해야 마지막 게임을 진행할 수 있습니다.')
print('-----------------------------------------------------')
while True:
    time.sleep(0.5)
    start = input('a) 러시안 룰렛, b) 가위바위보, c) 언오버, d)홀짝 e) 섯다 f) 인물추리퀴즈') #a ~ f 게임 선택
    if start == 'a': #러시안 룰렛
        if 1 not in number:
            print('-----------------------------------------------------')
            print('이미 진행한 게임입니다.') #number 리스트에서 1이 없을 경우
            print('-----------------------------------------------------')
            time.sleep(0.5)
            continue #start로 돌아감
        while True:
            print('-----------------------------------------------------')
            print('러시안 룰렛입니다.')
            print('생존3이 뽑힐경우 승리합니다')
            print('"사망" 이 나올경우 패배합니다')
            print('-----------------------------------------------------')
            time.sleep(1) # 1초간 대기시간
            bullet = ['생존1', '생존2', '생존3', '사망', '생존4', '생존5']
            print('-----------------------------------------------------')
            print(f'탄환 목록 : {bullet}')
            print('-----------------------------------------------------')
            i = 5
            while True:
                empty = random.randint(1, i)
                a = bullet.pop(empty) # bullet에서 empty로 a를 뽑음
                print('-----------------------------------------------------')
                b = input('빵야 빵야')
                print('-----------------------------------------------------')
                print(a)
                print('-----------------------------------------------------')
                i = i - 1 #총알 갯수 줄이기
                if a == '사망': #불렛에서 뽑은게 사망일 경우
                    print('총에 맞았읍니다.')
                    print('-----------------------------------------------------')
                    time.sleep(1)
                    exit(0)
                    #sys.system('shutdown -l') #시스템 로그오프
                    break
                if a == '생존3': #불렛에서 뽑은게 생존일 경우
                    print('다행이다!')
                    print('-----------------------------------------------------')
                    time.sleep(1)
                    break # 생존 시 while 처음으로 돌아감감    elif number == 2:
            # number.remove(1)
            break
        number.remove(1)
    elif start == 'b':
        if 2 not in number:
            print('-----------------------------------------------------')
            print('이미 진행한 게임입니다.') #number리스트에 2가 없을경우
            print('-----------------------------------------------------')
            time.sleep(0.5)
            continue
        while True:
            print('-----------------------------------------------------')
            print('간단한 가위바위보 게임입니다.')
            print("'가위', '바위', '보' 중 1가지를 타이핑하여 승부를 겨뤄보세요")
            print('-----------------------------------------------------')
            time.sleep(0.5)
            짱깸뽀 = ['가위', '바위', '보']
            life = 3
            Elife = 3
            while True:
                if life == 0:
                    print('-----------------------------------------------------')
                    print('에구 져버렸네')
                    print('-----------------------------------------------------')
                    exit(0)
                    break
                elif Elife == 0:
                    print('-----------------------------------------------------')
                    print('이겼다 ! ')
                    print('-----------------------------------------------------')
                    break
                enemy = random.choice(짱깸뽀)
                print('-----------------------------------------------------')
                myhand = input('가위 바위 보')
                print('-----------------------------------------------------')
                print(f'나 : {myhand}, 상대 : {enemy}')
                print('-----------------------------------------------------')
                time.sleep(1)
                a = '가위'
                b = '바위'
                c = '보'
                while True:
                    if myhand == a:
                        if enemy == a:
                            print('-----------------------------------------------------')
                            print('비겼읍니다.')
                            print('-----------------------------------------------------')
                            break
                        elif enemy == c:
                            print('-----------------------------------------------------')
                            print('이겼읍니다!')
                            print('-----------------------------------------------------')
                            Elife = Elife - 1
                            break
                        elif enemy == b:
                            print('-----------------------------------------------------')
                            print('졌읍니다!')
                            print('-----------------------------------------------------')
                            # os.system('shutdown -l')
                            # exit(0)
                            life = life - 1
                            break
                    if myhand == b:
                        if enemy == a:
                            print('-----------------------------------------------------')
                            print('이겼읍니다!')
                            print('-----------------------------------------------------')
                            Elife = Elife - 1
                            break
                        elif enemy == b:
                            print('-----------------------------------------------------')
                            print('비겼읍니다.')
                            print('-----------------------------------------------------')
                            break
                        elif enemy == c:
                            print('-----------------------------------------------------')
                            print('졌읍니다!')
                            print('-----------------------------------------------------')
                            # os.system('shutdown -l')
                            # exit(0)
                            life = life - 1
                            break
                    if myhand == c:
                        if enemy == a:
                            print('-----------------------------------------------------')
                            print('졌읍니다!')
                            print('-----------------------------------------------------')
                            # os.system('shutdown -l')
                            # exit(0)
                            life = life - 1
                            break
                        elif enemy == b:
                            print('-----------------------------------------------------')
                            print('이겼읍니다!')
                            print('-----------------------------------------------------')
                            Elife = Elife - 1
                            break
                        elif enemy == c:
                            print('-----------------------------------------------------')
                            print('비겼읍니다!')
                            print('-----------------------------------------------------')
                            break
                    else:  # 이외의 문자 입력 시 재입력 유도
                        print('-----------------------------------------------------')
                        print('상대 : 똑바로 안내?')
                        print('-----------------------------------------------------')
                        break
            break
        number.remove(2)
    elif start == 'c':
        if 3 not in number:
            print('-----------------------------------------------------')
            print('이미 진행한 게임입니다.')
            print('-----------------------------------------------------')
            time.sleep(0.5)
            continue
        while True:
            print('-----------------------------------------------------')
            print('언오버')
            print('1에서 1000사이의 숫자를 10회안에 맞춰보세요')
            print('-----------------------------------------------------')
            time.sleep(1)
            num = random.randrange(1, 1000)
            life = 10
            while True:
                print('-----------------------------------------------------')
                result = input('숫자는?')
                print('-----------------------------------------------------')
                result = int(result)
                if num > result:
                    life -= 1
                    print('-----------------------------------------------------')
                    print('오버입니다')
                    print(f'남은 목숨 {life}')
                    print('-----------------------------------------------------')
                    time.sleep(1)
                if num < result:
                    life -= 1
                    print('-----------------------------------------------------')
                    print('언더입니다')
                    print(f'남은 목숨 {life}')
                    print('-----------------------------------------------------')
                    time.sleep(1)
                if num == result:
                    print('-----------------------------------------------------')
                    print('정답입니다!')
                    print('-----------------------------------------------------')
                    time.sleep(1)
                    break
                elif life == 0:
                    print('-----------------------------------------------------')
                    print('패배입니다!')
                    print('-----------------------------------------------------')
                    # os.system('shutdown -l')
                    exit(0)
                    break
            break
        number.remove(3)
    elif start == 'd':
        if 4 not in number:
            print('-----------------------------------------------------')
            print('이미 진행한 게임입니다.')
            print('-----------------------------------------------------')
            time.sleep(0.5)
            continue
        while True:
            life = 3
            answer = 0
            print('-----------------------------------------------------')
            print('홀짝')
            print('과연 숫자가 홀일지 짝일지 맞춰보시오')
            print('-----------------------------------------------------')
            time.sleep(1)
            while True:
                hole = random.randrange(1, 100)
                print('-----------------------------------------------------')
                input('짤랑 짤랑')
                input('짤랑 짤랑')
                print('-----------------------------------------------------')
                result = input('홀? 짝?')
                print('-----------------------------------------------------')
                if hole % 2 == 0:
                    if result == '홀':
                        print('-----------------------------------------------------')
                        print(hole)
                        print('땡!')
                        print('-----------------------------------------------------')
                        time.sleep(0.5)
                        life -= 1
                    elif result == '짝':
                        print('-----------------------------------------------------')
                        print(hole)
                        print('정답!')
                        print('-----------------------------------------------------')
                        time.sleep(0.5)
                        answer += 1
                elif hole % 2 == 1:
                    if result == '홀':
                        print('-----------------------------------------------------')
                        print(hole)
                        print('정답!')
                        print('-----------------------------------------------------')
                        time.sleep(0.5)
                        answer += 1
                    elif result == '짝':
                        print('-----------------------------------------------------')
                        print(hole)
                        print('땡!')
                        print('-----------------------------------------------------')
                        time.sleep(0.5)
                        life -= 1
                if life == 0:
                    print('-----------------------------------------------------')
                    print('끝!')
                    time.sleep(0.5)
                    print('-----------------------------------------------------')
                    exit(0)
                    break
                if answer == 3:
                    print('-----------------------------------------------------')
                    print('성공!')
                    time.sleep(0.5)
                    print('-----------------------------------------------------')
                    break
            break
        number.remove(4)
    elif start == 'e':
        if 5 not in number:
            print('-----------------------------------------------------')
            print('이미 진행한 게임입니다.')
            print('-----------------------------------------------------')
            time.sleep(0.5)
            continue
        handcard = ['1월 두루미', '1월 소나무', '2월 매화', '2월 휘파람새', '3월 벚꽃', '3월 막', '4월 등나무', '4월 두견새',
                    '5월 창포', '5월 다리', '6월 모란', '6월 나비', '7월 싸리나무', '7월 멧돼지', '8월 억새', '8월 기러기',
                    '9월 국화', '9월 술잔', '10월 단풍', '10월 사슴']
        my_money = 100
        your_money = 100
        table_money = 0
        myhand = 0
        yourhand = 0
        while True:
            if my_money <= 0:  # 게임 시작 시 금액 확인
                print('-----------------------------------------------------')
                print('보유 금액이 부족하여 게임을 할 수 없습니다.')  # 보유머니 부족 시 자동 종료
                print('-----------------------------------------------------')
                time.sleep(0.3)
                exit(0)
                break
            elif your_money <= 0:  # 상대 보유머니 부족 시 자동 종료
                print('-----------------------------------------------------')
                print('상대가 보유 금액이 부족하여 게임을 종료합니다.')
                print('-----------------------------------------------------')
                break
            my_money = my_money - 10  # 기본 배팅금액 배팅
            your_money = your_money - 10
            table_money = table_money + 20
            myhandcard = random.sample(handcard, 2)
            yourhandcard = random.sample(handcard, 2)
            print('-----------------------------------------------------')
            print(f'내 패 : {myhandcard[0]}\n'
                  f'보유 금액 : {my_money}')
            print('-----------------------------------------------------')

            if myhandcard == ['1월 소나무', '1월 두루미']:
                myhand = 13
            elif myhandcard == ['1월 두루미', '1월 소나무']:
                myhand = 13
            elif myhandcard == ['1월 두루미', '2월 휘파람새']:
                myhand = 14
            elif myhandcard == ['1월 두루미', '2월 매화']:
                myhand = 14
            elif myhandcard == ['1월 두루미', '3월 벚꽃']:
                myhand = 3
            elif myhandcard == ['1월 두루미', '3월 막']:
                myhand = 25
            elif myhandcard == ['1월 두루미', '4월 등나무']:
                myhand = 15
            elif myhandcard == ['1월 두루미', '4월 두견새']:
                myhand = 15
            elif myhandcard == ['1월 두루미', '5월 창포']:
                myhand = 23
            elif myhandcard == ['1월 두루미', '5월 다리']:
                myhand = 23
            elif myhandcard == ['1월 두루미', '6월 모란']:
                myhand = 22
            elif myhandcard == ['1월 두루미', '6월 나비']:
                myhand = 22
            elif myhandcard == ['1월 두루미', '7월 싸리나무']:
                myhand = 21
            elif myhandcard == ['1월 두루미', '7월 멧돼지']:
                myhand = 21
            elif myhandcard == ['8월 억새', '1월 두루미']:
                myhand = 2
            elif myhandcard == ['1월 두루미', '8월 억새']:
                myhand = 2
            elif myhandcard == ['1월 두루미', '8월 기러기']:
                myhand = 20
            elif myhandcard == ['1월 두루미', '9월 국화']:
                myhand = 16
            elif myhandcard == ['1월 두루미', '9월 술잔']:
                myhand = 16
            elif myhandcard == ['1월 두루미', '10월 단풍']:
                myhand = 17
            elif myhandcard == ['1월 두루미', '10월 사슴']:
                myhand = 17
            elif myhandcard == ['1월 소나무', '2월 휘파람새']:
                myhand = 14
            elif myhandcard == ['1월 소나무', '2월 매화']:
                myhand = 14
            elif myhandcard == ['1월 소나무', '3월 벚꽃']:
                myhand = 25
            elif myhandcard == ['1월 소나무', '3월 막']:
                myhand = 25
            elif myhandcard == ['1월 소나무', '4월 등나무']:
                myhand = 15
            elif myhandcard == ['1월 소나무', '4월 두견새']:
                myhand = 15
            elif myhandcard == ['1월 소나무', '5월 창포']:
                myhand = 23
            elif myhandcard == ['1월 소나무', '5월 다리']:
                myhand = 23
            elif myhandcard == ['1월 소나무', '6월 모란']:
                myhand = 22
            elif myhandcard == ['1월 소나무', '6월 나비']:
                myhand = 22
            elif myhandcard == ['1월 소나무', '7월 싸리나무']:
                myhand = 21
            elif myhandcard == ['1월 소나무', '7월 멧돼지']:
                myhand = 21
            elif myhandcard == ['1월 소나무', '8월 억새']:
                myhand = 20
            elif myhandcard == ['1월 소나무', '8월 기러기']:
                myhand = 20
            elif myhandcard == ['1월 소나무', '9월 국화']:
                myhand = 16
            elif myhandcard == ['1월 소나무', '9월 술잔']:
                myhand = 16
            elif myhandcard == ['1월 소나무', '10월 단풍']:
                myhand = 17
            elif myhandcard == ['1월 소나무', '10월 사슴']:
                myhand = 17
            elif myhandcard == ['2월 매화', '1월 두루미']:
                myhand = 14
            elif myhandcard == ['2월 매화', '1월 소나무']:
                myhand = 14
            elif myhandcard == ['2월 휘파람새', '1월 두루미']:
                myhand = 14
            elif myhandcard == ['2월 휘파람새', '1월 소나무']:
                myhand = 14
            elif myhandcard == ['2월 매화', '2월 휘파람새']:
                myhand = 12
            elif myhandcard == ['2월 휘파람새', '2월 매화']:
                myhand = 12
            elif myhandcard == ['2월 매화', '3월 벚꽃']:
                myhand = 24
            elif myhandcard == ['2월 매화', '3월 막']:
                myhand = 24
            elif myhandcard == ['2월 매화', '4월 등나무']:
                myhand = 23
            elif myhandcard == ['2월 매화', '4월 두견새']:
                myhand = 23
            elif myhandcard == ['2월 매화', '5월 창포']:
                myhand = 22
            elif myhandcard == ['2월 매화', '5월 다리']:
                myhand = 22
            elif myhandcard == ['2월 매화', '6월 모란']:
                myhand = 21
            elif myhandcard == ['2월 매화', '6월 나비']:
                myhand = 21
            elif myhandcard == ['2월 매화', '7월 싸리나무']:
                myhand = 20
            elif myhandcard == ['2월 매화', '7월 멧돼지']:
                myhand = 20
            elif myhandcard == ['2월 매화', '8월 억새']:
                myhand = 29
            elif myhandcard == ['2월 매화', '8월 기러기']:
                myhand = 29
            elif myhandcard == ['2월 매화', '9월 국화']:
                myhand = 28
            elif myhandcard == ['2월 매화', '9월 술잔']:
                myhand = 28
            elif myhandcard == ['2월 매화', '10월 단풍']:
                myhand = 27
            elif myhandcard == ['2월 매화', '10월 사슴']:
                myhand = 27
            elif myhandcard == ['2월 휘파람새', '3월 벚꽃']:
                myhand = 24
            elif myhandcard == ['2월 휘파람새', '3월 막']:
                myhand = 24
            elif myhandcard == ['2월 휘파람새', '4월 등나무']:
                myhand = 23
            elif myhandcard == ['2월 휘파람새', '4월 두견새']:
                myhand = 23
            elif myhandcard == ['2월 휘파람새', '5월 창포']:
                myhand = 22
            elif myhandcard == ['2월 휘파람새', '5월 다리']:
                myhand = 22
            elif myhandcard == ['2월 휘파람새', '6월 모란']:
                myhand = 21
            elif myhandcard == ['2월 휘파람새', '6월 나비']:
                myhand = 21
            elif myhandcard == ['2월 휘파람새', '7월 싸리나무']:
                myhand = 20
            elif myhandcard == ['2월 휘파람새', '7월 멧돼지']:
                myhand = 20
            elif myhandcard == ['2월 휘파람새', '8월 억새']:
                myhand = 29
            elif myhandcard == ['2월 휘파람새', '8월 기러기']:
                myhand = 29
            elif myhandcard == ['2월 휘파람새', '9월 국화']:
                myhand = 28
            elif myhandcard == ['2월 휘파람새', '9월 술잔']:
                myhand = 28
            elif myhandcard == ['2월 휘파람새', '10월 단풍']:
                myhand = 27
            elif myhandcard == ['2월 휘파람새', '10월 사슴']:
                myhand = 27
            elif myhandcard == ['3월 벚꽃', '1월 두루미']:
                myhand = 3
            elif myhandcard == ['3월 벚꽃', '1월 소나무']:
                myhand = 25
            elif myhandcard == ['3월 벚꽃', '2월 매화']:
                myhand = 24
            elif myhandcard == ['3월 벚꽃', '2월 휘파람새']:
                myhand = 24
            elif myhandcard == ['3월 막', '1월 두루미']:
                myhand = 25
            elif myhandcard == ['3월 막', '1월 소나무']:
                myhand = 25
            elif myhandcard == ['3월 막', '2월 매화']:
                myhand = 24
            elif myhandcard == ['3월 막', '2월 휘파람새']:
                myhand = 24
            elif myhandcard == ['3월 벚꽃', '3월 막']:
                myhand = 11
            elif myhandcard == ['3월 막', '3월 벚꽃']:
                myhand = 11
            elif myhandcard == ['3월 벚꽃', '4월 등나무']:
                myhand = 22
            elif myhandcard == ['3월 벚꽃', '4월 두견새']:
                myhand = 22
            elif myhandcard == ['3월 벚꽃', '5월 창포']:
                myhand = 21
            elif myhandcard == ['3월 벚꽃', '5월 다리']:
                myhand = 21
            elif myhandcard == ['3월 벚꽃', '6월 모란']:
                myhand = 20
            elif myhandcard == ['3월 벚꽃', '6월 나비']:
                myhand = 20
            elif myhandcard == ['3월 벚꽃', '7월 싸리나무']:
                myhand = 29
            elif myhandcard == ['3월 벚꽃', '7월 멧돼지']:
                myhand = 29
            elif myhandcard == ['8월 억새', '3월 벚꽃']:
                myhand = 1
            elif myhandcard == ['3월 벚꽃', '8월 억새']:
                myhand = 1
            elif myhandcard == ['3월 벚꽃', '8월 기러기']:
                myhand = 28
            elif myhandcard == ['3월 벚꽃', '9월 국화']:
                myhand = 27
            elif myhandcard == ['3월 벚꽃', '9월 술잔']:
                myhand = 27
            elif myhandcard == ['3월 벚꽃', '10월 단풍']:
                myhand = 26
            elif myhandcard == ['3월 벚꽃', '10월 사슴']:
                myhand = 26
            elif myhandcard == ['3월 막', '4월 등나무']:
                myhand = 22
            elif myhandcard == ['3월 막', '4월 두견새']:
                myhand = 22
            elif myhandcard == ['3월 막', '5월 창포']:
                myhand = 21
            elif myhandcard == ['3월 막', '5월 다리']:
                myhand = 21
            elif myhandcard == ['3월 막', '6월 모란']:
                myhand = 20
            elif myhandcard == ['3월 막', '6월 나비']:
                myhand = 20
            elif myhandcard == ['3월 막', '7월 싸리나무']:
                myhand = 29
            elif myhandcard == ['3월 막', '7월 멧돼지']:
                myhand = 29
            elif myhandcard == ['3월 막', '8월 억새']:
                myhand = 28
            elif myhandcard == ['3월 막', '8월 기러기']:
                myhand = 28
            elif myhandcard == ['3월 막', '9월 국화']:
                myhand = 27
            elif myhandcard == ['3월 막', '9월 술잔']:
                myhand = 27
            elif myhandcard == ['3월 막', '10월 단풍']:
                myhand = 26
            elif myhandcard == ['3월 막', '10월 사슴']:
                myhand = 26
            elif myhandcard == ['4월 등나무', '1월 두루미']:
                myhand = 15
            elif myhandcard == ['4월 등나무', '1월 소나무']:
                myhand = 15
            elif myhandcard == ['4월 등나무', '2월 매화']:
                myhand = 23
            elif myhandcard == ['4월 등나무', '2월 휘파람새']:
                myhand = 23
            elif myhandcard == ['4월 등나무', '3월 벚꽃']:
                myhand = 22
            elif myhandcard == ['4월 등나무', '3월 막']:
                myhand = 22
            elif myhandcard == ['4월 두견새', '1월 두루미']:
                myhand = 15
            elif myhandcard == ['4월 두견새', '1월 소나무']:
                myhand = 15
            elif myhandcard == ['4월 두견새', '2월 매화']:
                myhand = 23
            elif myhandcard == ['4월 두견새', '2월 휘파람새']:
                myhand = 23
            elif myhandcard == ['4월 두견새', '3월 벚꽃']:
                myhand = 22
            elif myhandcard == ['4월 두견새', '3월 막']:
                myhand = 22
            elif myhandcard == ['4월 등나무', '4월 두견새']:
                myhand = 10
            elif myhandcard == ['4월 두견새', '4월 등나무']:
                myhand = 10
            elif myhandcard == ['4월 등나무', '5월 창포']:
                myhand = 20
            elif myhandcard == ['4월 등나무', '5월 다리']:
                myhand = 20
            elif myhandcard == ['4월 등나무', '6월 모란']:
                myhand = 19
            elif myhandcard == ['4월 등나무', '6월 나비']:
                myhand = 19
            elif myhandcard == ['4월 등나무', '7월 싸리나무']:
                myhand = 28
            elif myhandcard == ['4월 등나무', '7월 멧돼지']:
                myhand = 28
            elif myhandcard == ['4월 등나무', '8월 억새']:
                myhand = 27
            elif myhandcard == ['4월 등나무', '8월 기러기']:
                myhand = 27
            elif myhandcard == ['4월 등나무', '9월 국화']:
                myhand = 26
            elif myhandcard == ['4월 등나무', '9월 술잔']:
                myhand = 26
            elif myhandcard == ['4월 등나무', '10월 단풍']:
                myhand = 18
            elif myhandcard == ['4월 등나무', '10월 사슴']:
                myhand = 18
            elif myhandcard == ['4월 두견새', '5월 창포']:
                myhand = 20
            elif myhandcard == ['4월 두견새', '5월 다리']:
                myhand = 20
            elif myhandcard == ['4월 두견새', '6월 모란']:
                myhand = 19
            elif myhandcard == ['4월 두견새', '6월 나비']:
                myhand = 19
            elif myhandcard == ['4월 두견새', '7월 싸리나무']:
                myhand = 28
            elif myhandcard == ['4월 두견새', '7월 멧돼지']:
                myhand = 28
            elif myhandcard == ['4월 두견새', '8월 억새']:
                myhand = 27
            elif myhandcard == ['4월 두견새', '8월 기러기']:
                myhand = 27
            elif myhandcard == ['4월 두견새', '9월 국화']:
                myhand = 26
            elif myhandcard == ['4월 두견새', '9월 술잔']:
                myhand = 26
            elif myhandcard == ['4월 두견새', '10월 단풍']:
                myhand = 18
            elif myhandcard == ['4월 두견새', '10월 사슴']:
                myhand = 18
            elif myhandcard == ['5월 창포', '1월 두루미']:
                myhand = 23
            elif myhandcard == ['5월 창포', '1월 소나무']:
                myhand = 23
            elif myhandcard == ['5월 창포', '2월 매화']:
                myhand = 22
            elif myhandcard == ['5월 창포', '2월 휘파람새']:
                myhand = 22
            elif myhandcard == ['5월 창포', '3월 벚꽃']:
                myhand = 21
            elif myhandcard == ['5월 창포', '3월 막']:
                myhand = 21
            elif myhandcard == ['5월 창포', '4월 등나무']:
                myhand = 20
            elif myhandcard == ['5월 창포', '4월 두견새']:
                myhand = 20
            elif myhandcard == ['5월 다리', '1월 두루미']:
                myhand = 23
            elif myhandcard == ['5월 다리', '1월 소나무']:
                myhand = 23
            elif myhandcard == ['5월 다리', '2월 매화']:
                myhand = 22
            elif myhandcard == ['5월 다리', '2월 휘파람새']:
                myhand = 22
            elif myhandcard == ['5월 다리', '3월 벚꽃']:
                myhand = 21
            elif myhandcard == ['5월 다리', '3월 막']:
                myhand = 21
            elif myhandcard == ['5월 다리', '4월 등나무']:
                myhand = 20
            elif myhandcard == ['5월 다리', '4월 두견새']:
                myhand = 20
            elif myhandcard == ['5월 다리', '5월 창포']:
                myhand = 9
            elif myhandcard == ['5월 창포', '5월 다리']:
                myhand = 9
            elif myhandcard == ['5월 창포', '6월 모란']:
                myhand = 28
            elif myhandcard == ['5월 창포', '6월 나비']:
                myhand = 28
            elif myhandcard == ['5월 창포', '7월 싸리나무']:
                myhand = 27
            elif myhandcard == ['5월 창포', '7월 멧돼지']:
                myhand = 27
            elif myhandcard == ['5월 창포', '8월 억새']:
                myhand = 26
            elif myhandcard == ['5월 창포', '8월 기러기']:
                myhand = 26
            elif myhandcard == ['5월 창포', '9월 국화']:
                myhand = 25
            elif myhandcard == ['5월 창포', '9월 술잔']:
                myhand = 25
            elif myhandcard == ['5월 창포', '10월 단풍']:
                myhand = 24
            elif myhandcard == ['5월 창포', '10월 사슴']:
                myhand = 24
            elif myhandcard == ['5월 다리', '6월 모란']:
                myhand = 28
            elif myhandcard == ['5월 다리', '6월 나비']:
                myhand = 28
            elif myhandcard == ['5월 다리', '7월 싸리나무']:
                myhand = 27
            elif myhandcard == ['5월 다리', '7월 멧돼지']:
                myhand = 27
            elif myhandcard == ['5월 다리', '8월 억새']:
                myhand = 26
            elif myhandcard == ['5월 다리', '8월 기러기']:
                myhand = 26
            elif myhandcard == ['5월 다리', '9월 국화']:
                myhand = 25
            elif myhandcard == ['5월 다리', '9월 술잔']:
                myhand = 25
            elif myhandcard == ['5월 다리', '10월 단풍']:
                myhand = 24
            elif myhandcard == ['5월 다리', '10월 사슴']:
                myhand = 24
            elif myhandcard == ['6월 모란', '1월 두루미']:
                myhand = 22
            elif myhandcard == ['6월 모란', '1월 소나무']:
                myhand = 22
            elif myhandcard == ['6월 모란', '2월 매화']:
                myhand = 21
            elif myhandcard == ['6월 모란', '2월 휘파람새']:
                myhand = 21
            elif myhandcard == ['6월 모란', '3월 벚꽃']:
                myhand = 20
            elif myhandcard == ['6월 모란', '3월 막']:
                myhand = 20
            elif myhandcard == ['6월 모란', '4월 등나무']:
                myhand = 29
            elif myhandcard == ['6월 모란', '4월 두견새']:
                myhand = 29
            elif myhandcard == ['6월 모란', '5월 창포']:
                myhand = 28
            elif myhandcard == ['6월 모란', '5월 다리']:
                myhand = 28
            elif myhandcard == ['6월 나비', '1월 두루미']:
                myhand = 22
            elif myhandcard == ['6월 나비', '1월 소나무']:
                myhand = 22
            elif myhandcard == ['6월 나비', '2월 매화']:
                myhand = 21
            elif myhandcard == ['6월 나비', '2월 휘파람새']:
                myhand = 21
            elif myhandcard == ['6월 나비', '3월 벚꽃']:
                myhand = 20
            elif myhandcard == ['6월 나비', '3월 막']:
                myhand = 20
            elif myhandcard == ['6월 나비', '4월 등나뭐']:
                myhand = 29
            elif myhandcard == ['6월 나비', '4월 두견새']:
                myhand = 29
            elif myhandcard == ['6월 나비', '5월 창포']:
                myhand = 28
            elif myhandcard == ['6월 나비', '5월 다리']:
                myhand = 28
            elif myhandcard == ['6월 모란', '6월 나비']:
                myhand = 8
            elif myhandcard == ['6월 나비', '6월 모란']:
                myhand = 8
            elif myhandcard == ['6월 모란', '7월 싸리나무']:
                myhand = 26
            elif myhandcard == ['6월 모란', '7월 멧돼지']:
                myhand = 26
            elif myhandcard == ['6월 모란', '8월 억새']:
                myhand = 25
            elif myhandcard == ['6월 모란', '8월 기러기']:
                myhand = 25
            elif myhandcard == ['6월 모란', '9월 국화']:
                myhand = 24
            elif myhandcard == ['6월 모란', '9월 술잔']:
                myhand = 24
            elif myhandcard == ['6월 모란', '10월 단풍']:
                myhand = 23
            elif myhandcard == ['6월 모란', '10월 사슴']:
                myhand = 23
            elif myhandcard == ['6월 나비', '7월 싸리나무']:
                myhand = 26
            elif myhandcard == ['6월 나비', '7월 멧돼지']:
                myhand = 26
            elif myhandcard == ['6월 나비', '8월 억새']:
                myhand = 25
            elif myhandcard == ['6월 나비', '8월 기러기']:
                myhand = 25
            elif myhandcard == ['6월 나비', '9월 국화']:
                myhand = 24
            elif myhandcard == ['6월 나비', '9월 술잔']:
                myhand = 24
            elif myhandcard == ['6월 나비', '10월 단풍']:
                myhand = 23
            elif myhandcard == ['6월 나비', '10월 사슴']:
                myhand = 23
            elif myhandcard == ['7월 싸리나무', '1월 두루미']:
                myhand = 21
            elif myhandcard == ['7월 싸리나무', '1월 소나무']:
                myhand = 21
            elif myhandcard == ['7월 싸리나무', '2월 매화']:
                myhand = 20
            elif myhandcard == ['7월 싸리나무', '2월 휘파람새']:
                myhand = 20
            elif myhandcard == ['7월 싸리나무', '3월 벚꽃']:
                myhand = 29
            elif myhandcard == ['7월 싸리나무', '3월 막']:
                myhand = 29
            elif myhandcard == ['7월 싸리나무', '4월 등나무']:
                myhand = 28
            elif myhandcard == ['7월 싸리나무', '4월 두견새']:
                myhand = 28
            elif myhandcard == ['7월 싸리나무', '5월 창포']:
                myhand = 27
            elif myhandcard == ['7월 싸리나무', '5월 다리']:
                myhand = 27
            elif myhandcard == ['7월 싸리나무', '6월 모란']:
                myhand = 26
            elif myhandcard == ['7월 싸리나무', '6월 나비']:
                myhand = 26
            elif myhandcard == ['7월 멧돼지', '1월 두루미']:
                myhand = 21
            elif myhandcard == ['7월 멧돼지', '1월 소나무']:
                myhand = 21
            elif myhandcard == ['7월 멧돼지', '2월 매화']:
                myhand = 20
            elif myhandcard == ['7월 멧돼지', '2월 휘파람새']:
                myhand = 20
            elif myhandcard == ['7월 멧돼지', '3월 벚꽃']:
                myhand = 29
            elif myhandcard == ['7월 멧돼지', '3월 막']:
                myhand = 29
            elif myhandcard == ['7월 멧돼지', '4월 등나무']:
                myhand = 28
            elif myhandcard == ['7월 멧돼지', '4월 두견새']:
                myhand = 28
            elif myhandcard == ['7월 멧돼지', '5월 창포']:
                myhand = 27
            elif myhandcard == ['7월 멧돼지', '5월 다리']:
                myhand = 27
            elif myhandcard == ['7월 멧돼지', '6월 모란']:
                myhand = 26
            elif myhandcard == ['7월 멧돼지', '6월 나비']:
                myhand = 26
            elif myhandcard == ['7월 싸리나무', '7월 멧돼지']:
                myhand = 7
            elif myhandcard == ['7월 멧돼지', '7월 싸리나무']:
                myhand = 7
            elif myhandcard == ['7월 싸리나무', '8월 억새']:
                myhand = 24
            elif myhandcard == ['7월 싸리나무', '8월 기러기']:
                myhand = 24
            elif myhandcard == ['7월 싸리나무', '9월 국화']:
                myhand = 23
            elif myhandcard == ['7월 싸리나무', '9월 술잔']:
                myhand = 23
            elif myhandcard == ['7월 싸리나무', '10월 단풍']:
                myhand = 22
            elif myhandcard == ['7월 싸리나무', '10월 사슴']:
                myhand = 22
            elif myhandcard == ['7월 멧돼지', '8월 억새']:
                myhand = 24
            elif myhandcard == ['7월 멧돼지', '8월 기러기']:
                myhand = 24
            elif myhandcard == ['7월 멧돼지', '9월 국화']:
                myhand = 23
            elif myhandcard == ['7월 멧돼지', '9월 술잔']:
                myhand = 23
            elif myhandcard == ['7월 멧돼지', '10월 단풍']:
                myhand = 22
            elif myhandcard == ['7월 멧돼지', '10월 사슴']:
                myhand = 22
            elif myhandcard == ['8월 억새', '1월 두루미']:
                myhand = 20
            elif myhandcard == ['8월 억새', '1월 소나무']:
                myhand = 20
            elif myhandcard == ['8월 억새', '2월 매화']:
                myhand = 29
            elif myhandcard == ['8월 억새', '2월 휘파람새']:
                myhand = 29
            elif myhandcard == ['8월 억새', '3월 벚꽃']:
                myhand = 28
            elif myhandcard == ['8월 억새', '3월 막']:
                myhand = 28
            elif myhandcard == ['8월 억새', '4월 등나무']:
                myhand = 27
            elif myhandcard == ['8월 억새', '4월 두견새']:
                myhand = 27
            elif myhandcard == ['8월 억새', '5월 창포']:
                myhand = 26
            elif myhandcard == ['8월 억새', '5월 다리']:
                myhand = 26
            elif myhandcard == ['8월 억새', '6월 모란']:
                myhand = 25
            elif myhandcard == ['8월 억새', '6월 나비']:
                myhand = 25
            elif myhandcard == ['8월 억새', '7월 싸리나무']:
                myhand = 24
            elif myhandcard == ['8월 억새', '7월 멧돼지']:
                myhand = 24
            elif myhandcard == ['8월 기러기', '1월 두루미']:
                myhand = 20
            elif myhandcard == ['8월 기러기', '1월 소나무']:
                myhand = 20
            elif myhandcard == ['8월 기러기', '2월 매화']:
                myhand = 29
            elif myhandcard == ['8월 기러기', '2월 휘파람새']:
                myhand = 29
            elif myhandcard == ['8월 기러기', '3월 벚꽃']:
                myhand = 28
            elif myhandcard == ['8월 기러기', '3월 막']:
                myhand = 28
            elif myhandcard == ['8월 기러기', '4월 등나무']:
                myhand = 27
            elif myhandcard == ['8월 기러기', '4월 두견새']:
                myhand = 27
            elif myhandcard == ['8월 기러기', '5월 창포']:
                myhand = 26
            elif myhandcard == ['8월 기러기', '5월 다리']:
                myhand = 26
            elif myhandcard == ['8월 기러기', '6월 모란']:
                myhand = 25
            elif myhandcard == ['8월 기러기', '6월 나비']:
                myhand = 25
            elif myhandcard == ['8월 기러기', '7월 싸리나무']:
                myhand = 24
            elif myhandcard == ['8월 기러기', '7월 멧돼지']:
                myhand = 24
            elif myhandcard == ['8월 억새', '8월 기러기']:
                myhand = 6
            elif myhandcard == ['8월 기러기', '8월 억새']:
                myhand = 6
            elif myhandcard == ['8월 기러기', '9월 국화']:
                myhand = 22
            elif myhandcard == ['8월 기러기', '9월 술잔']:
                myhand = 22
            elif myhandcard == ['8월 기러기', '10월 단풍']:
                myhand = 21
            elif myhandcard == ['8월 기러기', '10월 사슴']:
                myhand = 21
            elif myhandcard == ['8월 억새', '9월 국화']:
                myhand = 22
            elif myhandcard == ['8월 억새', '9월 술잔']:
                myhand = 22
            elif myhandcard == ['8월 억새', '10월 단풍']:
                myhand = 21
            elif myhandcard == ['8월 억새', '10월 사슴']:
                myhand = 21
            elif myhandcard == ['9월 국화', '1월 두루미']:
                myhand = 16
            elif myhandcard == ['9월 국화', '1월 소나무']:
                myhand = 16
            elif myhandcard == ['9월 국화', '2월 매화']:
                myhand = 28
            elif myhandcard == ['9월 국화', '2월 휘파람새']:
                myhand = 28
            elif myhandcard == ['9월 국화', '3월 벚꽃']:
                myhand = 27
            elif myhandcard == ['9월 국화', '3월 막']:
                myhand = 27
            elif myhandcard == ['9월 국화', '4월 등나무']:
                myhand = 26
            elif myhandcard == ['9월 국화', '4월 두견새']:
                myhand = 26
            elif myhandcard == ['9월 국화', '5월 창포']:
                myhand = 25
            elif myhandcard == ['9월 국화', '5월 다리']:
                myhand = 25
            elif myhandcard == ['9월 국화', '6월 모란']:
                myhand = 24
            elif myhandcard == ['9월 국화', '6월 나비']:
                myhand = 24
            elif myhandcard == ['9월 국화', '7월 싸리나무']:
                myhand = 23
            elif myhandcard == ['9월 국화', '7월 멧돼지']:
                myhand = 23
            elif myhandcard == ['9월 국화', '8월 억새']:
                myhand = 22
            elif myhandcard == ['9월 국화', '8월 기러기']:
                myhand = 22
            elif myhandcard == ['9월 술잔', '1월 두루미']:
                myhand = 16
            elif myhandcard == ['9월 술잔', '1월 소나무']:
                myhand = 16
            elif myhandcard == ['9월 술잔', '2월 매화']:
                myhand = 28
            elif myhandcard == ['9월 술잔', '2월 휘파람새']:
                myhand = 28
            elif myhandcard == ['9월 술잔', '3월 벚꽃']:
                myhand = 27
            elif myhandcard == ['9월 술잔', '3월 막']:
                myhand = 27
            elif myhandcard == ['9월 술잔', '4월 등나무']:
                myhand = 26
            elif myhandcard == ['9월 술잔', '4월 두견새']:
                myhand = 26
            elif myhandcard == ['9월 술잔', '5월 창포']:
                myhand = 25
            elif myhandcard == ['9월 술잔', '5월 다리']:
                myhand = 25
            elif myhandcard == ['9월 술잔', '6월 나비']:
                myhand = 24
            elif myhandcard == ['9월 술잔', '6월 모란']:
                myhand = 24
            elif myhandcard == ['9월 술잔', '7월 싸리나무']:
                myhand = 23
            elif myhandcard == ['9월 술잔', '7월 멧돼지']:
                myhand = 23
            elif myhandcard == ['9월 술잔', '8월 억새']:
                myhand = 22
            elif myhandcard == ['9월 술잔', '8월 기러기']:
                myhand = 22
            elif myhandcard == ['9월 국화', '9월 술잔']:
                myhand = 5
            elif myhandcard == ['9월 술잔', '9월 국화']:
                myhand = 5
            elif myhandcard == ['9월 국화', '10월 단풍']:
                myhand = 20
            elif myhandcard == ['9월 국화', '10월 사슴']:
                myhand = 20
            elif myhandcard == ['10월 사슴', '9월 술잔']:
                myhand = 20
            elif myhandcard == ['10월 단풍', '9월 술잔']:
                myhand = 20
            elif myhandcard == ['10월 단풍', '1월 두루미']:
                myhand = 17
            elif myhandcard == ['10월 단풍', '1월 소나무']:
                myhand = 17
            elif myhandcard == ['10월 단풍', '2월 매화']:
                myhand = 27
            elif myhandcard == ['10월 단풍', '2월 휘파람새']:
                myhand = 27
            elif myhandcard == ['10월 단풍', '3월 벚꽃']:
                myhand = 26
            elif myhandcard == ['10월 단풍', '3월 막']:
                myhand = 26
            elif myhandcard == ['10월 단풍', '4월 등나무']:
                myhand = 18
            elif myhandcard == ['10월 단풍', '4월 두견새']:
                myhand = 18
            elif myhandcard == ['10월 단풍', '5월 창포']:
                myhand = 24
            elif myhandcard == ['10월 단풍', '5월 다리']:
                myhand = 24
            elif myhandcard == ['10월 단풍', '6월 모란']:
                myhand = 23
            elif myhandcard == ['10월 단풍', '6월 나비']:
                myhand = 23
            elif myhandcard == ['10월 단풍', '7월 싸리나무']:
                myhand = 22
            elif myhandcard == ['10월 단풍', '7월 멧돼지']:
                myhand = 22
            elif myhandcard == ['10월 단풍', '8월 억새']:
                myhand = 21
            elif myhandcard == ['10월 단풍', '8월 기러기']:
                myhand = 21
            elif myhandcard == ['10월 단풍', '9월 국화']:
                myhand = 20
            elif myhandcard == ['10월 단풍', '9월 술잔']:
                myhand = 20
            elif myhandcard == ['10월 사슴', '1월 두루미']:
                myhand = 17
            elif myhandcard == ['10월 사슴', '1월 소나무']:
                myhand = 17
            elif myhandcard == ['10월 사슴', '2월 매화']:
                myhand = 27
            elif myhandcard == ['10월 사슴', '2월 휘파람새']:
                myhand = 27
            elif myhandcard == ['10월 사슴', '3월 벚꽃']:
                myhand = 26
            elif myhandcard == ['10월 사슴', '3월 막']:
                myhand = 26
            elif myhandcard == ['10월 사슴', '4월 등나무']:
                myhand = 18
            elif myhandcard == ['10월 사슴', '4월 두견새']:
                myhand = 18
            elif myhandcard == ['10월 사슴', '5월 창포']:
                myhand = 24
            elif myhandcard == ['10월 사슴', '5월 다리']:
                myhand = 24
            elif myhandcard == ['10월 사슴', '6월 모란']:
                myhand = 23
            elif myhandcard == ['10월 사슴', '6월 나비']:
                myhand = 23
            elif myhandcard == ['10월 사슴', '7월 싸리나무']:
                myhand = 22
            elif myhandcard == ['10월 사슴', '7월 멧돼지']:
                myhand = 22
            elif myhandcard == ['10월 사슴', '8월 억새']:
                myhand = 21
            elif myhandcard == ['10월 사슴', '8월 기러기']:
                myhand = 21
            elif myhandcard == ['10월 사슴', '9월 국화']:
                myhand = 20
            elif myhandcard == ['10월 사슴', '9월 술잔']:
                myhand = 20
            elif myhandcard == ['10월 사슴', '10월 단풍']:
                myhand = 4
            elif myhandcard == ['10월 단풍', '10월 사슴']:
                myhand = 4
            if yourhandcard == ['1월 소나무', '1월 두루미']:
                yourhand = 13
            elif yourhandcard == ['1월 두루미', '1월 소나무']:
                yourhand = 13
            elif yourhandcard == ['1월 두루미', '2월 휘파람새']:
                yourhand = 14
            elif yourhandcard == ['1월 두루미', '2월 매화']:
                yourhand = 14
            elif yourhandcard == ['1월 두루미', '3월 벚꽃']:
                yourhand = 3
            elif yourhandcard == ['1월 두루미', '3월 막']:
                yourhand = 25
            elif yourhandcard == ['1월 두루미', '4월 등나무']:
                yourhand = 15
            elif yourhandcard == ['1월 두루미', '4월 두견새']:
                yourhand = 15
            elif yourhandcard == ['1월 두루미', '5월 창포']:
                yourhand = 23
            elif yourhandcard == ['1월 두루미', '5월 다리']:
                yourhand = 23
            elif yourhandcard == ['1월 두루미', '6월 모란']:
                yourhand = 22
            elif yourhandcard == ['1월 두루미', '6월 나비']:
                yourhand = 22
            elif yourhandcard == ['1월 두루미', '7월 싸리나무']:
                yourhand = 21
            elif yourhandcard == ['1월 두루미', '7월 멧돼지']:
                yourhand = 21
            elif yourhandcard == ['8월 억새', '1월 두루미']:
                yourhand = 2
            elif yourhandcard == ['1월 두루미', '8월 억새']:
                yourhand = 2
            elif yourhandcard == ['1월 두루미', '8월 기러기']:
                yourhand = 20
            elif yourhandcard == ['1월 두루미', '9월 국화']:
                yourhand = 16
            elif yourhandcard == ['1월 두루미', '9월 술잔']:
                yourhand = 16
            elif yourhandcard == ['1월 두루미', '10월 단풍']:
                yourhand = 17
            elif yourhandcard == ['1월 두루미', '10월 사슴']:
                yourhand = 17
            elif yourhandcard == ['1월 소나무', '2월 휘파람새']:
                yourhand = 14
            elif yourhandcard == ['1월 소나무', '2월 매화']:
                yourhand = 14
            elif yourhandcard == ['1월 소나무', '3월 벚꽃']:
                yourhand = 25
            elif yourhandcard == ['1월 소나무', '3월 막']:
                yourhand = 25
            elif yourhandcard == ['1월 소나무', '4월 등나무']:
                yourhand = 15
            elif yourhandcard == ['1월 소나무', '4월 두견새']:
                yourhand = 15
            elif yourhandcard == ['1월 소나무', '5월 창포']:
                yourhand = 23
            elif yourhandcard == ['1월 소나무', '5월 다리']:
                yourhand = 23
            elif yourhandcard == ['1월 소나무', '6월 모란']:
                yourhand = 22
            elif yourhandcard == ['1월 소나무', '6월 나비']:
                yourhand = 22
            elif yourhandcard == ['1월 소나무', '7월 싸리나무']:
                yourhand = 21
            elif yourhandcard == ['1월 소나무', '7월 멧돼지']:
                yourhand = 21
            elif yourhandcard == ['1월 소나무', '8월 억새']:
                yourhand = 20
            elif yourhandcard == ['1월 소나무', '8월 기러기']:
                yourhand = 20
            elif yourhandcard == ['1월 소나무', '9월 국화']:
                yourhand = 16
            elif yourhandcard == ['1월 소나무', '9월 술잔']:
                yourhand = 16
            elif yourhandcard == ['1월 소나무', '10월 단풍']:
                yourhand = 17
            elif yourhandcard == ['1월 소나무', '10월 사슴']:
                yourhand = 17
            elif yourhandcard == ['2월 매화', '1월 두루미']:
                yourhand = 14
            elif yourhandcard == ['2월 매화', '1월 소나무']:
                yourhand = 14
            elif yourhandcard == ['2월 휘파람새', '1월 두루미']:
                yourhand = 14
            elif yourhandcard == ['2월 휘파람새', '1월 소나무']:
                yourhand = 14
            elif yourhandcard == ['2월 매화', '2월 휘파람새']:
                yourhand = 12
            elif yourhandcard == ['2월 휘파람새', '2월 매화']:
                yourhand = 12
            elif yourhandcard == ['2월 매화', '3월 벚꽃']:
                yourhand = 24
            elif yourhandcard == ['2월 매화', '3월 막']:
                yourhand = 24
            elif yourhandcard == ['2월 매화', '4월 등나무']:
                yourhand = 23
            elif yourhandcard == ['2월 매화', '4월 두견새']:
                yourhand = 23
            elif yourhandcard == ['2월 매화', '5월 창포']:
                yourhand = 22
            elif yourhandcard == ['2월 매화', '5월 다리']:
                yourhand = 22
            elif yourhandcard == ['2월 매화', '6월 모란']:
                yourhand = 21
            elif yourhandcard == ['2월 매화', '6월 나비']:
                yourhand = 21
            elif yourhandcard == ['2월 매화', '7월 싸리나무']:
                yourhand = 20
            elif yourhandcard == ['2월 매화', '7월 멧돼지']:
                yourhand = 20
            elif yourhandcard == ['2월 매화', '8월 억새']:
                yourhand = 29
            elif yourhandcard == ['2월 매화', '8월 기러기']:
                yourhand = 29
            elif yourhandcard == ['2월 매화', '9월 국화']:
                yourhand = 28
            elif yourhandcard == ['2월 매화', '9월 술잔']:
                yourhand = 28
            elif yourhandcard == ['2월 매화', '10월 단풍']:
                yourhand = 27
            elif yourhandcard == ['2월 매화', '10월 사슴']:
                yourhand = 27
            elif yourhandcard == ['2월 휘파람새', '3월 벚꽃']:
                yourhand = 24
            elif yourhandcard == ['2월 휘파람새', '3월 막']:
                yourhand = 24
            elif yourhandcard == ['2월 휘파람새', '4월 등나무']:
                yourhand = 23
            elif yourhandcard == ['2월 휘파람새', '4월 두견새']:
                yourhand = 23
            elif yourhandcard == ['2월 휘파람새', '5월 창포']:
                yourhand = 22
            elif yourhandcard == ['2월 휘파람새', '5월 다리']:
                yourhand = 22
            elif yourhandcard == ['2월 휘파람새', '6월 모란']:
                yourhand = 21
            elif yourhandcard == ['2월 휘파람새', '6월 나비']:
                yourhand = 21
            elif yourhandcard == ['2월 휘파람새', '7월 싸리나무']:
                yourhand = 20
            elif yourhandcard == ['2월 휘파람새', '7월 멧돼지']:
                yourhand = 20
            elif yourhandcard == ['2월 휘파람새', '8월 억새']:
                yourhand = 29
            elif yourhandcard == ['2월 휘파람새', '8월 기러기']:
                yourhand = 29
            elif yourhandcard == ['2월 휘파람새', '9월 국화']:
                yourhand = 28
            elif yourhandcard == ['2월 휘파람새', '9월 술잔']:
                yourhand = 28
            elif yourhandcard == ['2월 휘파람새', '10월 단풍']:
                yourhand = 27
            elif yourhandcard == ['2월 휘파람새', '10월 사슴']:
                yourhand = 27
            elif yourhandcard == ['3월 벚꽃', '1월 두루미']:
                yourhand = 3
            elif yourhandcard == ['3월 벚꽃', '1월 소나무']:
                yourhand = 25
            elif yourhandcard == ['3월 벚꽃', '2월 매화']:
                yourhand = 24
            elif yourhandcard == ['3월 벚꽃', '2월 휘파람새']:
                yourhand = 24
            elif yourhandcard == ['3월 막', '1월 두루미']:
                yourhand = 25
            elif yourhandcard == ['3월 막', '1월 소나무']:
                yourhand = 25
            elif yourhandcard == ['3월 막', '2월 매화']:
                yourhand = 24
            elif yourhandcard == ['3월 막', '2월 휘파람새']:
                yourhand = 24
            elif yourhandcard == ['3월 벚꽃', '3월 막']:
                yourhand = 11
            elif yourhandcard == ['3월 막', '3월 벚꽃']:
                yourhand = 11
            elif yourhandcard == ['3월 벚꽃', '4월 등나무']:
                yourhand = 22
            elif yourhandcard == ['3월 벚꽃', '4월 두견새']:
                yourhand = 22
            elif yourhandcard == ['3월 벚꽃', '5월 창포']:
                yourhand = 21
            elif yourhandcard == ['3월 벚꽃', '5월 다리']:
                yourhand = 21
            elif yourhandcard == ['3월 벚꽃', '6월 모란']:
                yourhand = 20
            elif yourhandcard == ['3월 벚꽃', '6월 나비']:
                yourhand = 20
            elif yourhandcard == ['3월 벚꽃', '7월 싸리나무']:
                yourhand = 29
            elif yourhandcard == ['3월 벚꽃', '7월 멧돼지']:
                yourhand = 29
            elif yourhandcard == ['8월 억새', '3월 벚꽃']:
                yourhand = 1
            elif yourhandcard == ['3월 벚꽃', '8월 억새']:
                yourhand = 1
            elif yourhandcard == ['3월 벚꽃', '8월 기러기']:
                yourhand = 28
            elif yourhandcard == ['3월 벚꽃', '9월 국화']:
                yourhand = 27
            elif yourhandcard == ['3월 벚꽃', '9월 술잔']:
                yourhand = 27
            elif yourhandcard == ['3월 벚꽃', '10월 단풍']:
                yourhand = 26
            elif yourhandcard == ['3월 벚꽃', '10월 사슴']:
                yourhand = 26
            elif yourhandcard == ['3월 막', '4월 등나무']:
                yourhand = 22
            elif yourhandcard == ['3월 막', '4월 두견새']:
                yourhand = 22
            elif yourhandcard == ['3월 막', '5월 창포']:
                yourhand = 21
            elif yourhandcard == ['3월 막', '5월 다리']:
                yourhand = 21
            elif yourhandcard == ['3월 막', '6월 모란']:
                yourhand = 20
            elif yourhandcard == ['3월 막', '6월 나비']:
                yourhand = 20
            elif yourhandcard == ['3월 막', '7월 싸리나무']:
                yourhand = 29
            elif yourhandcard == ['3월 막', '7월 멧돼지']:
                yourhand = 29
            elif yourhandcard == ['3월 막', '8월 억새']:
                yourhand = 28
            elif yourhandcard == ['3월 막', '8월 기러기']:
                yourhand = 28
            elif yourhandcard == ['3월 막', '9월 국화']:
                yourhand = 27
            elif yourhandcard == ['3월 막', '9월 술잔']:
                yourhand = 27
            elif yourhandcard == ['3월 막', '10월 단풍']:
                yourhand = 26
            elif yourhandcard == ['3월 막', '10월 사슴']:
                yourhand = 26
            elif yourhandcard == ['4월 등나무', '1월 두루미']:
                yourhand = 15
            elif yourhandcard == ['4월 등나무', '1월 소나무']:
                yourhand = 15
            elif yourhandcard == ['4월 등나무', '2월 매화']:
                yourhand = 23
            elif yourhandcard == ['4월 등나무', '2월 휘파람새']:
                yourhand = 23
            elif yourhandcard == ['4월 등나무', '3월 벚꽃']:
                yourhand = 22
            elif yourhandcard == ['4월 등나무', '3월 막']:
                yourhand = 22
            elif yourhandcard == ['4월 두견새', '1월 두루미']:
                yourhand = 15
            elif yourhandcard == ['4월 두견새', '1월 소나무']:
                yourhand = 15
            elif yourhandcard == ['4월 두견새', '2월 매화']:
                yourhand = 23
            elif yourhandcard == ['4월 두견새', '2월 휘파람새']:
                yourhand = 23
            elif yourhandcard == ['4월 두견새', '3월 벚꽃']:
                yourhand = 22
            elif yourhandcard == ['4월 두견새', '3월 막']:
                yourhand = 22
            elif yourhandcard == ['4월 등나무', '4월 두견새']:
                yourhand = 10
            elif yourhandcard == ['4월 두견새', '4월 등나무']:
                yourhand = 10
            elif yourhandcard == ['4월 등나무', '5월 창포']:
                yourhand = 20
            elif yourhandcard == ['4월 등나무', '5월 다리']:
                yourhand = 20
            elif yourhandcard == ['4월 등나무', '6월 모란']:
                yourhand = 19
            elif yourhandcard == ['4월 등나무', '6월 나비']:
                yourhand = 19
            elif yourhandcard == ['4월 등나무', '7월 싸리나무']:
                yourhand = 28
            elif yourhandcard == ['4월 등나무', '7월 멧돼지']:
                yourhand = 28
            elif yourhandcard == ['4월 등나무', '8월 억새']:
                yourhand = 27
            elif yourhandcard == ['4월 등나무', '8월 기러기']:
                yourhand = 27
            elif yourhandcard == ['4월 등나무', '9월 국화']:
                yourhand = 26
            elif yourhandcard == ['4월 등나무', '9월 술잔']:
                yourhand = 26
            elif yourhandcard == ['4월 등나무', '10월 단풍']:
                yourhand = 18
            elif yourhandcard == ['4월 등나무', '10월 사슴']:
                yourhand = 18
            elif yourhandcard == ['4월 두견새', '5월 창포']:
                yourhand = 20
            elif yourhandcard == ['4월 두견새', '5월 다리']:
                yourhand = 20
            elif yourhandcard == ['4월 두견새', '6월 모란']:
                yourhand = 19
            elif yourhandcard == ['4월 두견새', '6월 나비']:
                yourhand = 19
            elif yourhandcard == ['4월 두견새', '7월 싸리나무']:
                yourhand = 28
            elif yourhandcard == ['4월 두견새', '7월 멧돼지']:
                yourhand = 28
            elif yourhandcard == ['4월 두견새', '8월 억새']:
                yourhand = 27
            elif yourhandcard == ['4월 두견새', '8월 기러기']:
                yourhand = 27
            elif yourhandcard == ['4월 두견새', '9월 국화']:
                yourhand = 26
            elif yourhandcard == ['4월 두견새', '9월 술잔']:
                yourhand = 26
            elif yourhandcard == ['4월 두견새', '10월 단풍']:
                yourhand = 18
            elif yourhandcard == ['4월 두견새', '10월 사슴']:
                yourhand = 18
            elif yourhandcard == ['5월 창포', '1월 두루미']:
                yourhand = 23
            elif yourhandcard == ['5월 창포', '1월 소나무']:
                yourhand = 23
            elif yourhandcard == ['5월 창포', '2월 매화']:
                yourhand = 22
            elif yourhandcard == ['5월 창포', '2월 휘파람새']:
                yourhand = 22
            elif yourhandcard == ['5월 창포', '3월 벚꽃']:
                yourhand = 21
            elif yourhandcard == ['5월 창포', '3월 막']:
                yourhand = 21
            elif yourhandcard == ['5월 창포', '4월 등나무']:
                yourhand = 20
            elif yourhandcard == ['5월 창포', '4월 두견새']:
                yourhand = 20
            elif yourhandcard == ['5월 다리', '1월 두루미']:
                yourhand = 23
            elif yourhandcard == ['5월 다리', '1월 소나무']:
                yourhand = 23
            elif yourhandcard == ['5월 다리', '2월 매화']:
                yourhand = 22
            elif yourhandcard == ['5월 다리', '2월 휘파람새']:
                yourhand = 22
            elif yourhandcard == ['5월 다리', '3월 벚꽃']:
                yourhand = 21
            elif yourhandcard == ['5월 다리', '3월 막']:
                yourhand = 21
            elif yourhandcard == ['5월 다리', '4월 등나무']:
                yourhand = 20
            elif yourhandcard == ['5월 다리', '4월 두견새']:
                yourhand = 20
            elif yourhandcard == ['5월 다리', '5월 창포']:
                yourhand = 9
            elif yourhandcard == ['5월 창포', '5월 다리']:
                yourhand = 9
            elif yourhandcard == ['5월 창포', '6월 모란']:
                yourhand = 28
            elif yourhandcard == ['5월 창포', '6월 나비']:
                yourhand = 28
            elif yourhandcard == ['5월 창포', '7월 싸리나무']:
                yourhand = 27
            elif yourhandcard == ['5월 창포', '7월 멧돼지']:
                yourhand = 27
            elif yourhandcard == ['5월 창포', '8월 억새']:
                yourhand = 26
            elif yourhandcard == ['5월 창포', '8월 기러기']:
                yourhand = 26
            elif yourhandcard == ['5월 창포', '9월 국화']:
                yourhand = 25
            elif yourhandcard == ['5월 창포', '9월 술잔']:
                yourhand = 25
            elif yourhandcard == ['5월 창포', '10월 단풍']:
                yourhand = 24
            elif yourhandcard == ['5월 창포', '10월 사슴']:
                yourhand = 24
            elif yourhandcard == ['5월 다리', '6월 모란']:
                yourhand = 28
            elif yourhandcard == ['5월 다리', '6월 나비']:
                yourhand = 28
            elif yourhandcard == ['5월 다리', '7월 싸리나무']:
                yourhand = 27
            elif yourhandcard == ['5월 다리', '7월 멧돼지']:
                yourhand = 27
            elif yourhandcard == ['5월 다리', '8월 억새']:
                yourhand = 26
            elif yourhandcard == ['5월 다리', '8월 기러기']:
                yourhand = 26
            elif yourhandcard == ['5월 다리', '9월 국화']:
                yourhand = 25
            elif yourhandcard == ['5월 다리', '9월 술잔']:
                yourhand = 25
            elif yourhandcard == ['5월 다리', '10월 단풍']:
                yourhand = 24
            elif yourhandcard == ['5월 다리', '10월 사슴']:
                yourhand = 24
            elif yourhandcard == ['6월 모란', '1월 두루미']:
                yourhand = 22
            elif yourhandcard == ['6월 모란', '1월 소나무']:
                yourhand = 22
            elif yourhandcard == ['6월 모란', '2월 매화']:
                yourhand = 21
            elif yourhandcard == ['6월 모란', '2월 휘파람새']:
                yourhand = 21
            elif yourhandcard == ['6월 모란', '3월 벚꽃']:
                yourhand = 20
            elif yourhandcard == ['6월 모란', '3월 막']:
                yourhand = 20
            elif yourhandcard == ['6월 모란', '4월 등나무']:
                yourhand = 29
            elif yourhandcard == ['6월 모란', '4월 두견새']:
                yourhand = 29
            elif yourhandcard == ['6월 모란', '5월 창포']:
                yourhand = 28
            elif yourhandcard == ['6월 모란', '5월 다리']:
                yourhand = 28
            elif yourhandcard == ['6월 나비', '1월 두루미']:
                yourhand = 22
            elif yourhandcard == ['6월 나비', '1월 소나무']:
                yourhand = 22
            elif yourhandcard == ['6월 나비', '2월 매화']:
                yourhand = 21
            elif yourhandcard == ['6월 나비', '2월 휘파람새']:
                yourhand = 21
            elif yourhandcard == ['6월 나비', '3월 벚꽃']:
                yourhand = 20
            elif yourhandcard == ['6월 나비', '3월 막']:
                yourhand = 20
            elif yourhandcard == ['6월 나비', '4월 등나뭐']:
                yourhand = 29
            elif yourhandcard == ['6월 나비', '4월 두견새']:
                yourhand = 29
            elif yourhandcard == ['6월 나비', '5월 창포']:
                yourhand = 28
            elif yourhandcard == ['6월 나비', '5월 다리']:
                yourhand = 28
            elif yourhandcard == ['6월 모란', '6월 나비']:
                yourhand = 8
            elif yourhandcard == ['6월 나비', '6월 모란']:
                yourhand = 8
            elif yourhandcard == ['6월 모란', '7월 싸리나무']:
                yourhand = 26
            elif yourhandcard == ['6월 모란', '7월 멧돼지']:
                yourhand = 26
            elif yourhandcard == ['6월 모란', '8월 억새']:
                yourhand = 25
            elif yourhandcard == ['6월 모란', '8월 기러기']:
                yourhand = 25
            elif yourhandcard == ['6월 모란', '9월 국화']:
                yourhand = 24
            elif yourhandcard == ['6월 모란', '9월 술잔']:
                yourhand = 24
            elif yourhandcard == ['6월 모란', '10월 단풍']:
                yourhand = 23
            elif yourhandcard == ['6월 모란', '10월 사슴']:
                yourhand = 23
            elif yourhandcard == ['6월 나비', '7월 싸리나무']:
                yourhand = 26
            elif yourhandcard == ['6월 나비', '7월 멧돼지']:
                yourhand = 26
            elif yourhandcard == ['6월 나비', '8월 억새']:
                yourhand = 25
            elif yourhandcard == ['6월 나비', '8월 기러기']:
                yourhand = 25
            elif yourhandcard == ['6월 나비', '9월 국화']:
                yourhand = 24
            elif yourhandcard == ['6월 나비', '9월 술잔']:
                yourhand = 24
            elif yourhandcard == ['6월 나비', '10월 단풍']:
                yourhand = 23
            elif yourhandcard == ['6월 나비', '10월 사슴']:
                yourhand = 23
            elif yourhandcard == ['7월 싸리나무', '1월 두루미']:
                yourhand = 21
            elif yourhandcard == ['7월 싸리나무', '1월 소나무']:
                yourhand = 21
            elif yourhandcard == ['7월 싸리나무', '2월 매화']:
                yourhand = 20
            elif yourhandcard == ['7월 싸리나무', '2월 휘파람새']:
                yourhand = 20
            elif yourhandcard == ['7월 싸리나무', '3월 벚꽃']:
                yourhand = 29
            elif yourhandcard == ['7월 싸리나무', '3월 막']:
                yourhand = 29
            elif yourhandcard == ['7월 싸리나무', '4월 등나무']:
                yourhand = 28
            elif yourhandcard == ['7월 싸리나무', '4월 두견새']:
                yourhand = 28
            elif yourhandcard == ['7월 싸리나무', '5월 창포']:
                yourhand = 27
            elif yourhandcard == ['7월 싸리나무', '5월 다리']:
                yourhand = 27
            elif yourhandcard == ['7월 싸리나무', '6월 모란']:
                yourhand = 26
            elif yourhandcard == ['7월 싸리나무', '6월 나비']:
                yourhand = 26
            elif yourhandcard == ['7월 멧돼지', '1월 두루미']:
                yourhand = 21
            elif yourhandcard == ['7월 멧돼지', '1월 소나무']:
                yourhand = 21
            elif yourhandcard == ['7월 멧돼지', '2월 매화']:
                yourhand = 20
            elif yourhandcard == ['7월 멧돼지', '2월 휘파람새']:
                yourhand = 20
            elif yourhandcard == ['7월 멧돼지', '3월 벚꽃']:
                yourhand = 29
            elif yourhandcard == ['7월 멧돼지', '3월 막']:
                yourhand = 29
            elif yourhandcard == ['7월 멧돼지', '4월 등나무']:
                yourhand = 28
            elif yourhandcard == ['7월 멧돼지', '4월 두견새']:
                yourhand = 28
            elif yourhandcard == ['7월 멧돼지', '5월 창포']:
                yourhand = 27
            elif yourhandcard == ['7월 멧돼지', '5월 다리']:
                yourhand = 27
            elif yourhandcard == ['7월 멧돼지', '6월 모란']:
                yourhand = 26
            elif yourhandcard == ['7월 멧돼지', '6월 나비']:
                yourhand = 26
            elif yourhandcard == ['7월 싸리나무', '7월 멧돼지']:
                yourhand = 7
            elif yourhandcard == ['7월 멧돼지', '7월 싸리나무']:
                yourhand = 7
            elif yourhandcard == ['7월 싸리나무', '8월 억새']:
                yourhand = 24
            elif yourhandcard == ['7월 싸리나무', '8월 기러기']:
                yourhand = 24
            elif yourhandcard == ['7월 싸리나무', '9월 국화']:
                yourhand = 23
            elif yourhandcard == ['7월 싸리나무', '9월 술잔']:
                yourhand = 23
            elif yourhandcard == ['7월 싸리나무', '10월 단풍']:
                yourhand = 22
            elif yourhandcard == ['7월 싸리나무', '10월 사슴']:
                yourhand = 22
            elif yourhandcard == ['7월 멧돼지', '8월 억새']:
                yourhand = 24
            elif yourhandcard == ['7월 멧돼지', '8월 기러기']:
                yourhand = 24
            elif yourhandcard == ['7월 멧돼지', '9월 국화']:
                yourhand = 23
            elif yourhandcard == ['7월 멧돼지', '9월 술잔']:
                yourhand = 23
            elif yourhandcard == ['7월 멧돼지', '10월 단풍']:
                yourhand = 22
            elif yourhandcard == ['7월 멧돼지', '10월 사슴']:
                yourhand = 22
            elif yourhandcard == ['8월 억새', '1월 두루미']:
                yourhand = 20
            elif yourhandcard == ['8월 억새', '1월 소나무']:
                yourhand = 20
            elif yourhandcard == ['8월 억새', '2월 매화']:
                yourhand = 29
            elif yourhandcard == ['8월 억새', '2월 휘파람새']:
                yourhand = 29
            elif yourhandcard == ['8월 억새', '3월 벚꽃']:
                yourhand = 28
            elif yourhandcard == ['8월 억새', '3월 막']:
                yourhand = 28
            elif yourhandcard == ['8월 억새', '4월 등나무']:
                yourhand = 27
            elif yourhandcard == ['8월 억새', '4월 두견새']:
                yourhand = 27
            elif yourhandcard == ['8월 억새', '5월 창포']:
                yourhand = 26
            elif yourhandcard == ['8월 억새', '5월 다리']:
                yourhand = 26
            elif yourhandcard == ['8월 억새', '6월 모란']:
                yourhand = 25
            elif yourhandcard == ['8월 억새', '6월 나비']:
                yourhand = 25
            elif yourhandcard == ['8월 억새', '7월 싸리나무']:
                yourhand = 24
            elif yourhandcard == ['8월 억새', '7월 멧돼지']:
                yourhand = 24
            elif yourhandcard == ['8월 기러기', '1월 두루미']:
                yourhand = 20
            elif yourhandcard == ['8월 기러기', '1월 소나무']:
                yourhand = 20
            elif yourhandcard == ['8월 기러기', '2월 매화']:
                yourhand = 29
            elif yourhandcard == ['8월 기러기', '2월 휘파람새']:
                yourhand = 29
            elif yourhandcard == ['8월 기러기', '3월 벚꽃']:
                yourhand = 28
            elif yourhandcard == ['8월 기러기', '3월 막']:
                yourhand = 28
            elif yourhandcard == ['8월 기러기', '4월 등나무']:
                yourhand = 27
            elif yourhandcard == ['8월 기러기', '4월 두견새']:
                yourhand = 27
            elif yourhandcard == ['8월 기러기', '5월 창포']:
                yourhand = 26
            elif yourhandcard == ['8월 기러기', '5월 다리']:
                yourhand = 26
            elif yourhandcard == ['8월 기러기', '6월 모란']:
                yourhand = 25
            elif yourhandcard == ['8월 기러기', '6월 나비']:
                yourhand = 25
            elif yourhandcard == ['8월 기러기', '7월 싸리나무']:
                yourhand = 24
            elif yourhandcard == ['8월 기러기', '7월 멧돼지']:
                yourhand = 24
            elif yourhandcard == ['8월 억새', '8월 기러기']:
                yourhand = 6
            elif yourhandcard == ['8월 기러기', '8월 억새']:
                yourhand = 6
            elif yourhandcard == ['8월 기러기', '9월 국화']:
                yourhand = 22
            elif yourhandcard == ['8월 기러기', '9월 술잔']:
                yourhand = 22
            elif yourhandcard == ['8월 기러기', '10월 단풍']:
                yourhand = 21
            elif yourhandcard == ['8월 기러기', '10월 사슴']:
                yourhand = 21
            elif yourhandcard == ['8월 억새', '9월 국화']:
                yourhand = 22
            elif yourhandcard == ['8월 억새', '9월 술잔']:
                yourhand = 22
            elif yourhandcard == ['8월 억새', '10월 단풍']:
                yourhand = 21
            elif yourhandcard == ['8월 억새', '10월 사슴']:
                yourhand = 21
            elif yourhandcard == ['9월 국화', '1월 두루미']:
                yourhand = 16
            elif yourhandcard == ['9월 국화', '1월 소나무']:
                yourhand = 16
            elif yourhandcard == ['9월 국화', '2월 매화']:
                yourhand = 28
            elif yourhandcard == ['9월 국화', '2월 휘파람새']:
                yourhand = 28
            elif yourhandcard == ['9월 국화', '3월 벚꽃']:
                yourhand = 27
            elif yourhandcard == ['9월 국화', '3월 막']:
                yourhand = 27
            elif yourhandcard == ['9월 국화', '4월 등나무']:
                yourhand = 26
            elif yourhandcard == ['9월 국화', '4월 두견새']:
                yourhand = 26
            elif yourhandcard == ['9월 국화', '5월 창포']:
                yourhand = 25
            elif yourhandcard == ['9월 국화', '5월 다리']:
                yourhand = 25
            elif yourhandcard == ['9월 국화', '6월 모란']:
                yourhand = 24
            elif yourhandcard == ['9월 국화', '6월 나비']:
                yourhand = 24
            elif yourhandcard == ['9월 국화', '7월 싸리나무']:
                yourhand = 23
            elif yourhandcard == ['9월 국화', '7월 멧돼지']:
                yourhand = 23
            elif yourhandcard == ['9월 국화', '8월 억새']:
                yourhand = 22
            elif yourhandcard == ['9월 국화', '8월 기러기']:
                yourhand = 22
            elif yourhandcard == ['9월 술잔', '1월 두루미']:
                yourhand = 16
            elif yourhandcard == ['9월 술잔', '1월 소나무']:
                yourhand = 16
            elif yourhandcard == ['9월 술잔', '2월 매화']:
                yourhand = 28
            elif yourhandcard == ['9월 술잔', '2월 휘파람새']:
                yourhand = 28
            elif yourhandcard == ['9월 술잔', '3월 벚꽃']:
                yourhand = 27
            elif yourhandcard == ['9월 술잔', '3월 막']:
                yourhand = 27
            elif yourhandcard == ['9월 술잔', '4월 등나무']:
                yourhand = 26
            elif yourhandcard == ['9월 술잔', '4월 두견새']:
                yourhand = 26
            elif yourhandcard == ['9월 술잔', '5월 창포']:
                yourhand = 25
            elif yourhandcard == ['9월 술잔', '5월 다리']:
                yourhand = 25
            elif yourhandcard == ['9월 술잔', '6월 나비']:
                yourhand = 24
            elif yourhandcard == ['9월 술잔', '6월 모란']:
                yourhand = 24
            elif yourhandcard == ['9월 술잔', '7월 싸리나무']:
                yourhand = 23
            elif yourhandcard == ['9월 술잔', '7월 멧돼지']:
                yourhand = 23
            elif yourhandcard == ['9월 술잔', '8월 억새']:
                yourhand = 22
            elif yourhandcard == ['9월 술잔', '8월 기러기']:
                yourhand = 22
            elif yourhandcard == ['9월 국화', '9월 술잔']:
                yourhand = 5
            elif yourhandcard == ['9월 술잔', '9월 국화']:
                yourhand = 5
            elif yourhandcard == ['9월 국화', '10월 단풍']:
                yourhand = 20
            elif yourhandcard == ['9월 국화', '10월 사슴']:
                yourhand = 20
            elif yourhandcard == ['10월 사슴', '9월 술잔']:
                yourhand = 20
            elif yourhandcard == ['10월 단풍', '9월 술잔']:
                yourhand = 20
            elif yourhandcard == ['10월 단풍', '1월 두루미']:
                yourhand = 17
            elif yourhandcard == ['10월 단풍', '1월 소나무']:
                yourhand = 17
            elif yourhandcard == ['10월 단풍', '2월 매화']:
                yourhand = 27
            elif yourhandcard == ['10월 단풍', '2월 휘파람새']:
                yourhand = 27
            elif yourhandcard == ['10월 단풍', '3월 벚꽃']:
                yourhand = 26
            elif yourhandcard == ['10월 단풍', '3월 막']:
                yourhand = 26
            elif yourhandcard == ['10월 단풍', '4월 등나무']:
                yourhand = 18
            elif yourhandcard == ['10월 단풍', '4월 두견새']:
                yourhand = 18
            elif yourhandcard == ['10월 단풍', '5월 창포']:
                yourhand = 24
            elif yourhandcard == ['10월 단풍', '5월 다리']:
                yourhand = 24
            elif yourhandcard == ['10월 단풍', '6월 모란']:
                yourhand = 23
            elif yourhandcard == ['10월 단풍', '6월 나비']:
                yourhand = 23
            elif yourhandcard == ['10월 단풍', '7월 싸리나무']:
                yourhand = 22
            elif yourhandcard == ['10월 단풍', '7월 멧돼지']:
                yourhand = 22
            elif yourhandcard == ['10월 단풍', '8월 억새']:
                yourhand = 21
            elif yourhandcard == ['10월 단풍', '8월 기러기']:
                yourhand = 21
            elif yourhandcard == ['10월 단풍', '9월 국화']:
                yourhand = 20
            elif yourhandcard == ['10월 단풍', '9월 술잔']:
                yourhand = 20
            elif yourhandcard == ['10월 사슴', '1월 두루미']:
                yourhand = 17
            elif yourhandcard == ['10월 사슴', '1월 소나무']:
                yourhand = 17
            elif yourhandcard == ['10월 사슴', '2월 매화']:
                yourhand = 27
            elif yourhandcard == ['10월 사슴', '2월 휘파람새']:
                yourhand = 27
            elif yourhandcard == ['10월 사슴', '3월 벚꽃']:
                yourhand = 26
            elif yourhandcard == ['10월 사슴', '3월 막']:
                yourhand = 26
            elif yourhandcard == ['10월 사슴', '4월 등나무']:
                yourhand = 18
            elif yourhandcard == ['10월 사슴', '4월 두견새']:
                yourhand = 18
            elif yourhandcard == ['10월 사슴', '5월 창포']:
                yourhand = 24
            elif yourhandcard == ['10월 사슴', '5월 다리']:
                yourhand = 24
            elif yourhandcard == ['10월 사슴', '6월 모란']:
                yourhand = 23
            elif yourhandcard == ['10월 사슴', '6월 나비']:
                yourhand = 23
            elif yourhandcard == ['10월 사슴', '7월 싸리나무']:
                yourhand = 22
            elif yourhandcard == ['10월 사슴', '7월 멧돼지']:
                yourhand = 22
            elif yourhandcard == ['10월 사슴', '8월 억새']:
                yourhand = 21
            elif yourhandcard == ['10월 사슴', '8월 기러기']:
                yourhand = 21
            elif yourhandcard == ['10월 사슴', '9월 국화']:
                yourhand = 20
            elif yourhandcard == ['10월 사슴', '9월 술잔']:
                yourhand = 20
            elif yourhandcard == ['10월 사슴', '10월 단풍']:
                yourhand = 4
            elif yourhandcard == ['10월 단풍', '10월 사슴']:
                yourhand = 4
            if myhand == 1:
                myhand = '38광땡'
            elif myhand == 2:
                myhand = '18광땡'
            elif myhand == 3:
                myhand = '13광땡'
            elif myhand == 4:
                myhand = '장땡'
            elif myhand == 5:
                myhand = '9땡'
            elif myhand == 6:
                myhand = '8땡'
            elif myhand == 7:
                myhand = '7땡'
            elif myhand == 8:
                myhand = '6땡'
            elif myhand == 9:
                myhand = '5땡'
            elif myhand == 10:
                myhand = '4땡'
            elif myhand == 11:
                myhand = '3땡'
            elif myhand == 12:
                myhand = '2땡'
            elif myhand == 13:
                myhand = '1땡'
            elif myhand == 14:
                myhand = '알리'
            elif myhand == 15:
                myhand = '독사'
            elif myhand == 16:
                myhand = '구삥'
            elif myhand == 17:
                myhand = '장삥'
            elif myhand == 18:
                myhand = '장사'
            elif myhand == 19:
                myhand = '세륙'
            elif myhand == 20:
                myhand = '아홉끗'
            elif myhand == 21:
                myhand = '여덟끗'
            elif myhand == 22:
                myhand = '일곱끗'
            elif myhand == 23:
                myhand = '여섯끗'
            elif myhand == 24:
                myhand = '다섯끗'
            elif myhand == 25:
                myhand = '네끗'
            elif myhand == 26:
                myhand = '세끗'
            elif myhand == 27:
                myhand = '두끗'
            elif myhand == 28:
                myhand = '한끗'
            elif myhand == 29:
                myhand = '망통'
            if yourhand == 1:
                yourhand = '38광땡'
            elif yourhand == 2:
                yourhand = '18광땡'
            elif yourhand == 3:
                yourhand = '13광땡'
            elif yourhand == 4:
                yourhand = '장땡'
            elif yourhand == 5:
                yourhand = '9땡'
            elif yourhand == 6:
                yourhand = '8땡'
            elif yourhand == 7:
                yourhand = '7땡'
            elif yourhand == 8:
                yourhand = '6땡'
            elif yourhand == 9:
                yourhand = '5땡'
            elif yourhand == 10:
                yourhand = '4땡'
            elif yourhand == 11:
                yourhand = '3땡'
            elif yourhand == 12:
                yourhand = '2땡'
            elif yourhand == 13:
                yourhand = '1땡'
            elif yourhand == 14:
                yourhand = '알리'
            elif yourhand == 15:
                yourhand = '독사'
            elif yourhand == 16:
                yourhand = '구삥'
            elif yourhand == 17:
                yourhand = '장삥'
            elif yourhand == 18:
                yourhand = '장사'
            elif yourhand == 19:
                yourhand = '세륙'
            elif yourhand == 20:
                yourhand = '아홉끗'
            elif yourhand == 21:
                yourhand = '여덟끗'
            elif yourhand == 22:
                yourhand = '일곱끗'
            elif yourhand == 23:
                yourhand = '여섯끗'
            elif yourhand == 24:
                yourhand = '다섯끗'
            elif yourhand == 25:
                yourhand = '네끗'
            elif yourhand == 26:
                yourhand = '세끗'
            elif yourhand == 27:
                yourhand = '두끗'
            elif yourhand == 28:
                yourhand = '한끗'
            elif yourhand == 29:
                yourhand = '망통'
            while True:
                if my_money <= 0:  # 게임 시작 시 금액 확인
                    print('-----------------------------------------------------')
                    print('보유 금액이 부족하여 게임을 할 수 없습니다.')  # 보유머니 부족 시 자동 종료
                    print('-----------------------------------------------------')
                    exit(0)
                    break
                elif your_money <= 0:  # 상대 보유머니 부족 시 자동 종료
                    print('-----------------------------------------------------')
                    print('상대가 보유 금액이 부족하여 게임을 종료합니다.')
                    print('-----------------------------------------------------')
                    break
                print('-----------------------------------------------------')
                print('당신의 차례입니다.')
                deal = input('a) raise, b) fold')
                print('-----------------------------------------------------')
                if deal == 'a':
                    print('-----------------------------------------------------')
                    Raise = input(f'배팅 금액을 입력해 주세요. 보유 금액 : {my_money}')
                    print('-----------------------------------------------------')
                    Raise = int(Raise)
                    if Raise > my_money:
                        print('-----------------------------------------------------')
                        print('배팅 금액이 보유 금액보다 많습니다.')
                        print('-----------------------------------------------------')
                        time.sleep(0.3)
                    elif Raise == my_money:
                        print('-----------------------------------------------------')
                        print('올인하시겠습니까 ?')
                        print('-----------------------------------------------------')
                        que = input('a) yes, b) no')
                        if que == 'a':
                            table_money = table_money + my_money
                            my_money = my_money - my_money
                            print('-----------------------------------------------------')
                            print(f'보유 금액')
                            print(f'판돈')
                            print('-----------------------------------------------------')
                            time.sleep(0.3)
                            table_money = table_money + your_money
                            your_money = your_money - your_money
                            print('-----------------------------------------------------')
                            print(f'상대 금액 : {your_money}')
                            print(f'판돈 : {table_money}')
                            print('-----------------------------------------------------')
                            time.sleep(0.3)
                            while True:
                                print('-----------------------------------------------------')
                                print(f'당신의 패 : {myhandcard}, {myhand}')
                                print('당신의 차례입니다.')
                                que = input('a) fold, b) call')
                                print('-----------------------------------------------------')
                                if que == 'a':
                                    print('-----------------------------------------------------')
                                    print('정말 포기하겠습니까?')
                                    fold = input('a) yes, b) no')
                                    print('-----------------------------------------------------')
                                    if fold == 'a':
                                        print('-----------------------------------------------------')
                                        print('나 : 포기하겠어')
                                        print('-----------------------------------------------------')
                                        your_money = your_money + table_money
                                        break
                                    elif fold == 'b':
                                        continue
                                    else:
                                        continue
                                elif que == 'b':
                                    print('-----------------------------------------------------')
                                    print('나 : 올인')
                                    print(f'내 패 : {myhandcard}, {myhand}')
                                    print(f'상대 패 : {yourhandcard}, {yourhand}')
                                    print('-----------------------------------------------------')
                                    if myhand < yourhand:
                                        print('이겼당!')
                                        print('-----------------------------------------------------')
                                        time.sleep(0.3)
                                        my_money = my_money + table_money
                                        print(f'보유금액 : {my_money}')
                                        print(f'상대 금액 : {your_money}')
                                        print('-----------------------------------------------------')
                                        time.sleep(0.3)
                                    elif yourhand < myhand:
                                        print('졌따')
                                        print('-----------------------------------------------------')
                                        time.sleep(0.3)
                                        your_money = your_money + table_money
                                        print(f'상대 금액 : {your_money}')
                                        print('-----------------------------------------------------')
                                        time.sleep(0.3)
                                        break
                                    break
                                else:
                                    continue
                                break
                        if que == 'b':
                            continue
                        else:
                            continue
                    elif Raise < my_money:
                        print('-----------------------------------------------------')
                        print(f'{Raise} 배팅')
                        print('-----------------------------------------------------')
                        table_money = table_money + Raise
                        my_money = my_money - Raise
                        print(f'보유 금액 : {my_money}')
                        print(f'판돈 : {table_money}')
                        print('-----------------------------------------------------')
                        time.sleep(0.3)
                        while True:
                            if your_money <= Raise:
                                table_money = table_money + your_money
                                your_money = your_money - your_money
                            elif your_money > Raise:
                                table_money = table_money + Raise
                                your_money = your_money - Raise
                            print('-----------------------------------------------------')
                            print(f'상대 보유 금액 : {your_money}')
                            print(f'판돈 : {table_money}')
                            print(f'나의 패 : {myhandcard}, {myhand}')
                            print('-----------------------------------------------------')
                            print('당신의 차례입니다')
                            deal = input('a) raise, b) fold')
                            print('-----------------------------------------------------')
                            if deal == 'a':
                                print('-----------------------------------------------------')
                                print(f'배팅 금액을 입력해주세요, 보유 금액 : {my_money}')
                                Raise = input('raise money')
                                print('-----------------------------------------------------')
                                Raise = int(Raise)
                                if Raise > my_money:
                                    print('-----------------------------------------------------')
                                    print('배팅금액이 보유금액보다 많습니다')
                                    print('-----------------------------------------------------')
                                elif Raise == my_money:
                                    print('-----------------------------------------------------')
                                    print('올인 하시겠습니까?')
                                    que = input('a) yes, b) no')
                                    print('-----------------------------------------------------')
                                    if que == 'a':
                                        table_money = table_money + my_money
                                        my_money = my_money - my_money
                                        print('-----------------------------------------------------')
                                        print(f'보유 금액 : {my_money}')
                                        print(f'판돈 : {table_money}')
                                        print('-----------------------------------------------------')
                                        time.sleep(0.3)
                                        table_money = table_money + your_money
                                        your_money = your_money - your_money
                                        print('-----------------------------------------------------')
                                        print(f'상대 보유 금액 : {your_money}')
                                        print(f'판돈 : {table_money}')
                                        print('-----------------------------------------------------')
                                        time.sleep(0.3)
                                        while True:
                                            print('-----------------------------------------------------')
                                            que = input('a) fold, b) call')
                                            print('-----------------------------------------------------')
                                            if que == 'a':
                                                print('-----------------------------------------------------')
                                                print('포기하시겠습니까 ?')
                                                fold = input('a) yes, b) no')
                                                print('-----------------------------------------------------')
                                                if fold == 'a':
                                                    print('나 : 포기하겠어')
                                                    print('-----------------------------------------------------')
                                                    break
                                                elif fold == 'b':
                                                    continue
                                                else:
                                                    continue
                                            elif que == 'b':
                                                print('-----------------------------------------------------')
                                                print('올인!')
                                                print(f'내 패 : {myhandcard}, {myhand}')
                                                print(f'상대 패 : {yourhandcard}, {yourhand}')
                                                print('-----------------------------------------------------')
                                                if myhand < yourhand:
                                                    print('이겼당!')
                                                    print('-----------------------------------------------------')
                                                    time.sleep(0.3)
                                                    my_money = my_money + table_money
                                                    print('-----------------------------------------------------')
                                                    print(f'보유금액 : {my_money}')
                                                    print(f'상대 금액 : {your_money}')
                                                    print('-----------------------------------------------------')
                                                    time.sleep(0.3)
                                                    break
                                                elif yourhand < myhand:
                                                    print('졌따')
                                                    print('-----------------------------------------------------')
                                                    time.sleep(0.3)
                                                    your_money = your_money + table_money
                                                    print(f'상대 금액 : {your_money}')
                                                    print('-----------------------------------------------------')
                                                    time.sleep(0.3)
                                                    break
                                                break
                                            else:
                                                continue
                                        break
                                    break

                                    if que == 'b':
                                        continue
                                    else:
                                        continue
                                elif Raise < my_money:
                                    print('-----------------------------------------------------')
                                    print(f'{Raise} 배팅')
                                    print('-----------------------------------------------------')
                                    table_money = table_money + Raise
                                    my_money = my_money - Raise
                                    print(f'보유금액 :{my_money}')
                                    print(f'판돈 : {table_money}')
                                    print('-----------------------------------------------------')
                                    time.sleep(0.3)
                                    if your_money <= Raise:
                                        table_money = table_money + your_money
                                        your_money = your_money - your_money
                                    elif your_money > Raise:
                                        table_money = table_money + Raise
                                        your_money = your_money - Raise
                                    while True:
                                        print('-----------------------------------------------------')
                                        print(f'내 패 : {myhandcard}, {myhand}')
                                        print(f'상대 패 : {yourhandcard}, {yourhand}')
                                        print('-----------------------------------------------------')
                                        if myhand < yourhand:
                                            print('이겼당!')
                                            print('-----------------------------------------------------')
                                            time.sleep(0.3)
                                            my_money = my_money + table_money
                                            print(f'보유금액 : {my_money}')
                                            print(f'상대 금액 : {your_money}')
                                            print('-----------------------------------------------------')
                                            time.sleep(0.3)
                                            break
                                        elif yourhand < myhand:
                                            print('졌따')
                                            print('-----------------------------------------------------')
                                            time.sleep(0.3)
                                            your_money = your_money + table_money
                                            print(f'상대 금액 : {your_money}')
                                            print('-----------------------------------------------------')
                                            time.sleep(0.3)
                                            break
                                        break
                                break
                            elif deal == 'b':
                                print('-----------------------------------------------------')
                                print('포기 하시겠습니까 ?')
                                fold = input('a) yes, b) no')
                                print('-----------------------------------------------------')
                                if fold == 'a':
                                    print('나 :포기하겠어')
                                    print('-----------------------------------------------------')
                                    break
                                if fold == 'b':
                                    continue
                                else:
                                    continue
                            else:
                                continue
                            break
                        break
                    else:
                        continue
                elif deal == 'b':
                    print('-----------------------------------------------------')
                    print('나 : 포기하겠습니까 ?')
                    fold = input('a) yes, b) no')
                    print('-----------------------------------------------------')
                    if fold == 'a':
                        print('나 : 포기하겠어')
                        print('-----------------------------------------------------')
                        break
                    if fold == 'b':
                        continue
                    else:
                        continue
                else:
                    continue
                number.remove(5)
    elif start == 'f':
        if number != [6]:
            print('앞의 5가지 동작을 모두 수행 후 시도해 주세요')
            continue
            human = [Person, person2]
            a = random.choice(human)
            b = a()
            b.첫번째()
            b.두번째()
            b.세번째()
            b.네번째()
            b.다섯번째()
            b.여섯번째()
            b.일곱번째()
            b.여덟번째()
            b.아홉번째()
            b.열번째()
            break

