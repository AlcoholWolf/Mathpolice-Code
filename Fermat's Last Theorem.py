#페르마의 마지막 정리 / 사용법 : 이 셀을 실행(L-Shift+Enter) 후 perma(숫자, 계산식, 등등 수가 반환되는 모든 값) 을 다른 셀에 적고 실행
def perma(Num):
  for a in range(2,101):
      for b in range(2,101):
          for c in range(b+1,101):
                  if a**Num==(b**Num+c**Num):
                      print("{},{},{}".format(a,b,c))
                  if a**Num<(b**Num+c**Num):     
                    break    
  print('더는없다')          
for Aut in range(2,101):
  print(Aut,'제곱일때. a^2+b^2=c^2을 만족하는 수는')
  perma(Aut)