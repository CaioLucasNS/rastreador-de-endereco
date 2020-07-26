import webbrowser

print('Informe seu endereço.')
rua = 'R.+' + input('Rua: ')
rua = rua.replace(' ', '+')

numero = input('N° da residência: ')
bairro = input('Bairro: ')
bairro = bairro.replace(' ', '+')

cidade = input('Cidade: ')
cidade = cidade.replace(' ', '+')

estado = input('Estado [XX]:')
cep = input('Cep (facultativo): ')

endereco = rua + numero + bairro + cidade + cep
complemento_url = rua + '+' + numero + '+' + bairro + '+' + cidade + '+' + estado + '+' + cep

webbrowser.open(f'https://www.google.com/maps/place/{complemento_url}')
