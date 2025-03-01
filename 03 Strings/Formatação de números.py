
"""
Original file is located at
    https://colab.research.google.com/drive/1MnAABdPDOlnIRE8a5vAaEnijCm2YWbd0

# Format - Aula de Consulta

### Como usar o format para criar formatações personalizadas em prints e textos.

:<		Alinha o texto à esquerda (se tiver espaço na tela para isso)
print(f'Para rodar 1000 km: \n {"Veiculo":<10} )

:>		Alinha o texto à direita (se tiver espaço na tela para isso)
print(f'Para rodar 1000 km: \n {"Veiculo":>10} )


:^		Alinha o texto ao centro (se tiver espaço na tela para isso)
print(f' {"Relatório Final":^60}\n ')


:+		Coloca o sinal sempre na frente do número (independente se é positivo ou negativo)
:,		Coloca a vírgula como separador de milhar
:_		Coloca o _ como separador de milhar
:e		Formato Científico
:f		Número com quantidade fixa de casas decimais
:x		Formato HEX minúscula (para cores)
:X		Formato HEX maiúscula (para cores)
:%		Formato Percentual

- Exemplo de Alinhamento
"""

email = 'lira@gmail.com'
print('Meu e-mail não é {:<30}, show?'.format(email))

"""- Exemplo de Edição de Sinal"""

custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:+} e lucro foi {:+}'.format(faturamento, lucro))

"""- Exemplo de Separador de Milhar"""

custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:+} e lucro foi {:+}'.format(faturamento, lucro))

"""- Formato com casas Decimais fixas"""

custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:.2f} e lucro foi {:2f}'.format(faturamento, lucro))

"""- Formato Percentual"""

custo = 500                               
faturamento = 1300
lucro = faturamento - custo    
margem = lucro / faturamento                  #OU          margem = (lucro / faturamento) * 100
print('Margem de lucro foi de {:.2%}'.format(margem))      #print('Margem de lucro foi de {:.2f}%'.format(margem))


"""- Formato Moeda -> Combinação de Formatos

Existem módulos/bibliotecas que vão facilitar isso, caso a gente queira, mas vamos ver como usar módulos mais a frente do curso. Por enquanto, se você precisar, pode fazer substituições em string
"""

custo = 5000
faturamento = 27000
lucro = faturamento - custo
print('Faturamento foi R${:,.2f} e lucro foi R${:,.2f}'.format(faturamento, lucro))

#transformando no formato brasileiro
lucro_texto = 'R${:_.2f}'.format(lucro)
print(lucro_texto.replace('.', ',').replace('_', '.'))

"""- Função round() para arredondar números, caso seja necessário"""

imposto = 0.15758
preco = 100
valor_imposto = round(preco * imposto, 1)
print('Imposto sobre o preço é de {}'.format(valor_imposto))