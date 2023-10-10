my_variable = "My String variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_srt_variable = str(my_int_variable)
print(my_int_to_srt_variable)
print(type(my_int_to_srt_variable))


my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables
print(my_variable, my_int_variable, my_bool_variable)

#FUNCIONES DEL SISTEMA
print(len(my_variable))#cuenta cantidad de letras y espacios

#VARIABLES EN UNA SOLA LINEA (no muy recomendable)
name, surname, alias, age = "Romi", "Gv", "Chomi", "31"
print("Me llamo:", name, surname, ".mi edad es:", age, "y mi alias es:", alias)

#INPUT
name = input('Cual es tu nombre')
age = input('Cual es tu edad')

print(name)
print(age)