import math
import time
class permutaties():
    def __init__(self, permorcomb, k, nummers, herhaling):
        self.k = k
        self.permorcomb = permorcomb
        self.nummers = nummers
        self.herhaling = herhaling
        if permorcomb == 'permutatie':
            if herhaling == 'ja':
                nummer = str(nummers)
                getelde_nummer = nummer.count(',') + 1
                antwoord = int(getelde_nummer) ** int(k)
                antwoord = str(antwoord)
                getelde_nummer = str(getelde_nummer)
                k = str(k)
                print('het antwoord is: ' + getelde_nummer + '^' + k + ' = ' + antwoord)
                time.sleep(3)
                print('')
                print('')
                permorcomb = input('is het een permutatie of een combinatie; (permutatie, combinatie): ')
                print('**************************************************************************')
                print(
                    'voorbeeld permutatie; een wachtwoord bestaand uit 4 cijfer (k = 4) gekozen uit 3, 4, 7, 8, 23 (n = 3, 4, 7, 8, 23)')
                print('voorbeeld combinatie; uit de 20 kinderen (k = 20) worden er 4 gekozen (n = 4) om te voetballen')
                print('**************************************************************************')
                time.sleep(3)
                k = input('wat is de K; (bijvoorbeeld 5): ')
                nummers = input('wat zijn je N elementen, perm=(23, 54, 26, 98), comb=(4): ')
                herhaling = input('is herhaling toegestaan of niet; (ja, nee): ')
                permutatie = permutaties(permorcomb, k, nummers, herhaling)
            elif herhaling == 'nee':
                nummer = str(nummers)
                getelde_nummer = nummer.count(',') + 1
                antwoord = int(math.perm(int(getelde_nummer), int(k)))
                antwoord = str(antwoord)
                getelde_nummer = str(getelde_nummer)
                k = str(k)
                print('het antwoord is: ' + getelde_nummer + 'P' + k + ' = ' + antwoord)
                time.sleep(3)
                print('')
                print('')
                permorcomb = input('is het een permutatie of een combinatie; (permutatie, combinatie): ')
                print('**************************************************************************')
                print(
                    'voorbeeld permutatie; een wachtwoord bestaand uit 4 cijfer (k = 4) gekozen uit 3, 4, 7, 8, 23 (n = 3, 4, 7, 8, 23)')
                print('voorbeeld combinatie; uit de 20 kinderen (k = 20) worden er 4 gekozen (n = 4) om te voetballen')
                print('**************************************************************************')
                time.sleep(3)
                k = input('wat is de K; (bijvoorbeeld 5): ')
                nummers = input('wat zijn je N elementen, perm=(23, 54, 26, 98), comb=(4): ')
                herhaling = input('is herhaling toegestaan of niet; (ja, nee): ')
                permutatie = permutaties(permorcomb, k, nummers, herhaling)
        elif permorcomb == 'combinatie':
            if herhaling == 'nee':
                nummer = int(nummers)
                #getelde_nummer = nummer.count(',') + 1
                antwoord = int(math.comb(int(k), int(nummer)))
                antwoord = str(antwoord)
                nummer = str(nummer)
                k = str(k)
                print('het antwoord is: ' + k + 'C' + nummer + ' = ' + antwoord)
                #print('herhaling is niet toegestaan in herhalingen')
                time.sleep(3)
                print('')
                print('')
                permorcomb = input('is het een permutatie of een combinatie; (permutatie, combinatie): ')
                print('**************************************************************************')
                print(
                    'voorbeeld permutatie; een wachtwoord bestaand uit 4 cijfer (k = 4) gekozen uit 3, 4, 7, 8, 23 (n = 3, 4, 7, 8, 23)')
                print('voorbeeld combinatie; uit de 20 kinderen (k = 20) worden er 4 gekozen (n = 4) om te voetballen')
                print('**************************************************************************')
                time.sleep(3)
                k = input('wat is de K; (bijvoorbeeld 5): ')
                nummers = input('wat zijn je N elementen, perm=(23, 54, 26, 98), comb=(4): ')
                herhaling = input('is herhaling toegestaan of niet; (ja, nee): ')
                permutatie = permutaties(permorcomb, k, nummers, herhaling)
            elif herhaling == 'ja':
                print('herhaling is niet toegestaan in combinaties')
                time.sleep(1)
                print('')
                print('')
                permorcomb = input('is het een permutatie of een combinatie; (permutatie, combinatie): ')
                print('**************************************************************************')
                print(
                    'voorbeeld permutatie; een wachtwoord bestaand uit 4 cijfer (k = 4) gekozen uit 3, 4, 7, 8, 23 (n = 3, 4, 7, 8, 23)')
                print('voorbeeld combinatie; uit de 20 kinderen (k = 20) worden er 4 gekozen (n = 4) om te voetballen')
                print('**************************************************************************')
                time.sleep(2)
                k = input('wat is de K; (bijvoorbeeld 5): ')
                nummers = input('wat zijn je N elementen, perm=(23, 54, 26, 98), comb=(4): ')
                herhaling = input('is herhaling toegestaan of niet; (ja, nee): ')
                permutatie = permutaties(permorcomb, k, nummers, herhaling)

permorcomb = input('is het een permutatie of een combinatie; (permutatie, combinatie): ')
print('**************************************************************************')
print('voorbeeld permutatie; een wachtwoord bestaand uit 4 cijfer (k = 4) gekozen uit 3, 4, 7, 8, 23 (n = 3, 4, 7, 8, 23)')
print('voorbeeld combinatie; uit de 20 kinderen (k = 20) worden er 4 gekozen (n = 4) om te voetballen')
print('**************************************************************************')
time.sleep(4)
k = input('wat is de K; (bijvoorbeeld 5): ')
nummers = input('wat zijn je N elementen; perm(4, 5, 2), comb(3): ')
herhaling = input('is herhaling toegestaan of niet; (ja, nee): ')
permutatie = permutaties(permorcomb, k, nummers, herhaling)
