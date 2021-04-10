#Kalkulator jednostek

def km_mile(a):
    return a * 0.6213

def mile_km(b):
    return b * 1.6093

def f_c(f):
   return (f - 32) / 1.8

def c_f(c):
   return (c * 9/5) + 32

print('Witaj w kalkulatorze jednostek.')
print('Aby zamienic km na mile wpisz "km".')
print('Aby zamienic mile na km wpisz "m".')
print('Aby zamienic F na C wpisz "f".')
print('Aby zamienic C na F wpisz "c".')
print('Aby zakończyć działanie, wciśnij "enter"')
print()

while True:
    co_liczyc = input('Napisz co chcesz policzyć:')
    if co_liczyc == 'km':
        l_jedn = float(input('Podaj liczbę jednostek: '))
        print(l_jedn, 'km to:', "%.2f" % (km_mile(l_jedn)) , 'mil.')
    elif co_liczyc == 'm':
        l_jedn = float(input('Podaj liczbę jednostek: '))
        print(l_jedn, 'mil to:', "%.2f" % (mile_km(l_jedn)), 'km.')
    elif co_liczyc == 'f':
        l_jedn = float(input('Podaj liczbę jednostek: '))
        print(l_jedn, 'F to:', "%.1f" % (f_c(l_jedn)), 'C.')
    elif co_liczyc == 'c':
        l_jedn = float(input('Podaj liczbę jednostek: '))
        print(l_jedn, 'C to:', "%.1f" % (c_f(l_jedn)), 'F.')
    elif co_liczyc == '':
        break
    else:
        print('Podałeś nieprawidłową jednostkę, spróbuj jeszcze raz.')





