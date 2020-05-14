''' bu kendime not '''
''' not2 bunu yeni ekledim 14/05/2020'''
import random


ihtimaller = ['taş','kağıt','makas']

def zar():
  a = random.choice(ihtimaller)
  return a


while True:
  print(' 1 - Taş \n 2 - Kağıt \n 3 - Makas \n Seçiminizi yapın?')
  secim = int(input())
  if secim == 1:
    osecim = 'taş'
  elif secim == 2:
    osecim = 'kağıt'
  elif secim == 3:
    osecim = 'makas'
  else:
    osecim = 'gecersiz'
  zarsonuc = zar()
  print('\n Seçiminiz = ',osecim,'\n Benim secimim = ',zarsonuc)

  if osecim == zarsonuc:
    print('\n Berabere. \n')
  elif (osecim == 'taş' and zarsonuc == 'makas'):
    print('\n Kazandınız.')
  elif (osecim == 'kağıt' and zarsonuc == 'taş'):
    print('\n Kazandınız.')
  elif (osecim == 'makas' and zarsonuc == 'kağıt'):
    print('\n Kazandınız.')  
  else:
    print('\n Kaybettiniz.')
  print(2 * '\n ***********************\n')
  print('Tekrar Oynamak istermisiniz? (y/n)')
  toyun = input()
  if toyun == 'n':
    print('Hoşçakal.')
    break
  else:
    print("\033c")


