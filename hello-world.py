idioma = input('[PT/IN]: ').strip().upper()
while idioma != 'PT' and idioma != 'IN':
    idioma = input('[PT/IN]: ').strip()

if idioma == 'PT':
    print('Olá, mundo!')

if idioma == 'IN':
    print('Hello world!')
