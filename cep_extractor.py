import re

address: str = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
statement: str = "O cpf do senhor Jose é: 123.123.123-12"

# [0-9]{5} = Estabelece um intervalo, 0 a 9. {5} indica que este padrão irá se repetir 5 vezes.
cep_pattern = re.compile("[0-9]{5}[-]?[0-9]{3}")

cpf_pattern = re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}")

# Pesquisa dentro de uma string por um "match" com a expressão.
cep = cep_pattern.search(address)
cpf = cpf_pattern.search(statement)

# match.group() = Retorna None ou o valor encontrado pela expressão.
if cep:
    print(cep.group())

if(cpf):
    print(cpf.group())
