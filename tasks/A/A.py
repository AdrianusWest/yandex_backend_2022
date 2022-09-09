def main(alices_name, zelibobas_name):
    type_of_match = ['?'] * len(zelibobas_name)
    alices_quantity = {}
    zelibobas_quantity = {}
    for i in range(len(alices_name)):
        if zelibobas_name[i] == alices_name[i]:
            type_of_match[i] = 'P'
        else:
            zelibobas_quantity[alices_name[i]] = (zelibobas_quantity[alices_name[i]]
                                                  if alices_name[i] in zelibobas_quantity else 0) + 1
            alices_quantity[zelibobas_name[i]] = (alices_quantity[zelibobas_name[i]]
                                                  if zelibobas_name[i] in alices_quantity else 0) + 1

    for i in range(len(zelibobas_name)):
        if type_of_match[i] == '?':
            set_i_or_s(zelibobas_name[i], zelibobas_quantity, i, type_of_match)
            set_i_or_s(zelibobas_name[i], alices_quantity, i, type_of_match)

    return ''.join(type_of_match)


def set_i_or_s(letter, dictionary, i, type_of_match):
    if letter in dictionary and dictionary[letter] != 0:
        dictionary[letter] -= 1
        type_of_match[i] = 'I' if type_of_match[i] == '?' else 'S'


alices_name = input()
zelibobas_name = input()
print(main(alices_name, zelibobas_name))
