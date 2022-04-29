from constants import *

R_NU_E_INT = 'R nu e un int.'
C_NU_E_INT = 'C nu e un int.'
R_PREA_MIC = f'R este mai mic ca {MIN_NR}.'
C_PREA_MIC = "C este mai mic ca {MIN_NR}."
R_PREA_MARE = "R este mai mare ca {MAX_NR}."
C_PREA_MARE = "C este mai mare ca {MAX_NR}."
NU_SUNT_DRAGONI = "Fisierul de intrare nu contine dragoni."
FISIER_DE_INTRARE_GOL = 'Fisierul de intrare este gol.'
FISIER_DE_INTRARE_GRESIT = 'Fisierul de intrare nu exista.'
FARA_C = 'Fisierul de intrare nu contine C.'

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