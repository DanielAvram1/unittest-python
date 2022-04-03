R_NU_E_INT = 'R nu e un int.'
C_NU_E_INT = 'C nu e un int.'
R_ESTE_MAI_MIC_CA_1 = 'R este mai mic ca 1.'
C_ESTE_MAI_MIC_CA_1 = "C este mai mic ca 1."
R_ESTE_MAI_MARE_CA_1000 = "R este mai mare ca 1000."
C_ESTE_MAI_MARE_CA_1000 = "C este mai mare ca 1000."
NU_SUNT_DRAGONI = "Fisierul de intrare nu contine dragoni."

def fis_nu_are_linii(R):
  return f'Fisierul de intrare nu are {R} linii.'

def linia_nu_are_caract(i, C):
  return f'Linia {i} nu are {C} caractere.'

def caract_nu_e_permis(char):
  return f'Caracterul {char} nu este permis.'

NO_I = 'Nu a fost introdus un caracter I.'

NO_O = 'Nu a fost introdus un caracter O.'

def nu_este_numar(line):
  return f'{line} nu este un numar.'