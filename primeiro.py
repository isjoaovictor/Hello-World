while True:
 try:
  peso = float(input("qual seu peso: "))
  alt = float(input("qual sua altura: "))
  imc = peso/(alt*alt)
  if imc > 30:
   print("gordo")
  print(f'{imc:.2f}')
  break
 except ValueError:
    print('valor invalido')
