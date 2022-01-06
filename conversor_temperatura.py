print('-='*30)
print('(1)Fahrenheit')
print('(2)Celsius')
print('(3)Kelvin')
print ('-='*30)

escolha = input('Escolha qual dos medidores de  temperatura Você deseja inserir:')
print('-='*30)
escolha2 = input ('Escolha qual dos medidores você deseja converter:')
if escolha.isnumeric() and escolha2.isnumeric():
    escolha= int(escolha)
    escolha2 = int(escolha2)
    if escolha == 1 and escolha2 == 2:
        print('-='*30)
        medidor_fah = input('Digite uma temperatura em fahrenheit:')
        conv_temp = float(medidor_fah)
        conta_fah = (conv_temp-32)*5/9
        print(f'O resultado da conversão de Fahrenheit para Celsius é  {conta_fah}')

    elif escolha == 2 and escolha2 == 1:
        print ('-='*30)
        medidor_cel = input('Digite uma temperatura em celsius:')
        conv_temp = float(medidor_cel)
        conta_celsius = (conv_temp*9/5)+32
        print(f'O resultado da conversão de celsius para Farenheit é {conta_celsius}')

    elif escolha == 3 and escolha2 == 1:
        print('-='*30)
        medidor_kelvin = input ('Digite uma temperatura em kelvin:')
        conv_temp = float(medidor_kelvin)
        conta_kelvin = (conv_temp-273.15)*9/5+32
        print(f'O resultado da conversão de kelvin para Fahrenheit é {conta_kelvin:.2f}')

    elif escolha == 3 and escolha2 == 2:
        medidor_kelvin = input ('Digite uma temperatura em kelvin:')
        conv_temp = float(medidor_kelvin)
        conta_kelvin = conv_temp - 273.15
        print(f'O resultado da conversão de kelvin para celisus é {conta_kelvin:.2f}')

    elif escolha == 2 and escolha2 == 3:
        medidor_celsius = input('Digite uma temperatura em celisus:')
        conv_temp = float(medidor_celsius)
        conta_celsius = conv_temp+273.15
        print(f'O resultado da conversão de celsius para kelvin é {conta_celsius}')
    elif escolha == 1 and escolha2 == 3:
        medidor_fahr = input('Digite uma temperatura em Fahrenheit:')
        conv_temp = float(medidor_fahr)
        conta_fah = (conv_temp-32)*5/9+273.15
        print(f'O resultado da conversão de Fahrenheit para kelvin é {conta_fah}')
else:
    print(f'ops ouve um erro você digitou {escolha} e {escolha2 }isses caracteres são  invalidos!!')













