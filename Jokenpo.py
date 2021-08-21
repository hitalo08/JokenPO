import random
import emoji

print('\033[36m-=\033[m'*65)
print('')
e = str('''\033[36m        Bem vindo ao JokenPÔ! Este programa foi criado com o objetivo da máquina brincar com o usuário!
Para representar o papel, informe papel. Para representar a tesoura, informe tesoura. E para representar a pedra, informe pedra\033[m
''')
print(e)
print('\033[36m-=\033[m'*65)
v = str(input('\033[31m                                                 O que você deseja jogar?\033[m ')).lower()
print('')
print('\033[35mJogador:\033[m {}'.format(v).center(133))
r = random.choice(['papel','pedra','tesoura'])
print('\033[35mMáquina:\033[m {}'.format(r).center(133))
if v == r:
    print('')
    print(emoji.emojize('\033[1;36mNÃO HOUVE VENCEDOR POIS JOGAMOS A MESMA COISA!\033[m'.center(137)))
    print('')
elif v == 'papel' and r == 'pedra':
    print('')
    print(emoji.emojize('\033[32mPAPEL EMBRULHA A PEDRA! VOCÊ É O VENCEDOR! :grinning_face_with_smiling_eyes::thumbs_up_dark_skin_tone:\033[m'.center(195)))
    print('')
elif v == 'pedra' and r == 'papel':
    print('')
    print(emoji.emojize('\033[31mPAPEL EMBRULHA A PEDRA. VOCÊ PERDEU! :weary_face::thumbs_down_dark_skin_tone:\033[m'.center(170)))
    print('')
elif v == 'tesoura' and r == 'pedra':
    print('')
    print(emoji.emojize('\033[31mTESOURA AMASSA E QUEBRAL NA PEDRA. VOCÊ PERDEU! :weary_face::thumbs_down_dark_skin_tone:\033[m '.center(170)))
    print('')
elif v =='pedra' and r=='tesoura':
    print('')
    print(emoji.emojize('\033[32mPEDRA AMASSA E QUEBRA TESOURA! VOCÊ É O VENCEDOR! :grinning_face_with_smiling_eyes::thumbs_up_dark_skin_tone:\033[m'.center(195)))
    print('')
elif v =='tesoura' and r=='papel':
    print('')
    print(emoji.emojize('\033[32mTESOURA CORTA O PAPEL! VOCÊ É O VENCEDOR! :grinning_face_with_smiling_eyes::thumbs_up_dark_skin_tone:\033[m'.center(195)))
    print('')
elif v=='papel' and r=='tesoura':
    print('')
    print(emoji.emojize('\033[31mTESOURA CORTA O PAPEL. VOCÊ PERDEU! :weary_face::thumbs_down_dark_skin_tone:\033[m'.center(170)))
    print('')
else:
    print('Valor inválido!')
    print('\n')
x = input('Digite algo pra sair.....'.center(138))