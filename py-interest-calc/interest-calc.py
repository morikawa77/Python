from cmath import log


def getSimpleInterestM(c, t, i):
  m = c+(c.i.t)
  print(m)

def getSimpleInterestC(m, t, i):
  c = (m / (i*t)) / 2
  print(c)

def getSimpleInterestT(c, i, m):
  t = (m-c) / (c*i)
  print(t) 

def getSimpleInterestI(c, t, m):
  i = (m-c) / (t*c)
  print(i)


def getCompoundInterestM(c, t, i):
  m = c(1 + i) ** t
  print(m)

def getCompoundInterestC(m, t, i):
  c = m / ((1+i)**t)
  print(c)

def getCompoundInterestT(c, i, m):
  t = (log(m / c)/log(1 + i))
  print(t) 

def getCompoundInterestI(c, t, m):
  i = ((m/c) ** (1/t)) - 1
  print(i)



while True:
  interest_type = input('Digite S para juros simples ou digite C para composto')
  if interest_type == 'S' or interest_type == 'C':  
    break

while True:
  var_unknown = input('''
      Para obter o valor do Montante digite M
      Para obter o valor de Capital digite C
      Para obter o valor o Tempo digite T
      Para obter o valor da Taxa digite I
    ''')
  if var_unknown == 'M' or var_unknown == 'C' or var_unknown == 'T' or var_unknown == 'I':
    break



if var_unknown == 'M': #obter montante
  c = input('Digite o valor do Capital')
  t = input('Digite o valor do Tempo')
  i = input('Digite o valor da Taxa')
  if interest_type == 'S':
    getSimpleInterestM(c, t, i)
  elif interest_type == 'C':
    getCompoundInterestM(c, t, i)

elif var_unknown == 'C': #obter capital
  m = input('Digite o valor do Montante')
  t = input('Digite o valor do Tempo')
  i = input('Digite o valor da Taxa')
  if interest_type == 'S':
    getSimpleInterestC(m, t, i)
  elif interest_type == 'C':
    getCompoundInterestC(m, t, i)

elif var_unknown == 'T':
  c = input('Digite o valor do Capital')
  i = input('Digite o valor da Taxa')
  m = input('Digite o valor do Montante')
  if interest_type == 'S':
    getSimpleInterestT(c, i, m)
  elif interest_type == 'C':
    getCompoundInterestT(c, i, m)

elif var_unknown == 'I':
  c = input('Digite o valor do Capital')
  t = input('Digite o valor do Tempo')
  m = input('Digite o valor do Montante')
  if interest_type == 'S':
    getSimpleInterestI(c, t, m)
  elif interest_type == 'C':
    getCompoundInterestI(c, t, m)










