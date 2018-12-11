"""
CSE583 Project
According to user's input for lmer, creates a formular and
its name
"""

def formula_creator():
    """
    Creates a formular based on user's input for Lmer, 
    and a name describing the formular.
    """
    outcome = input('Input outcome value:')
    print()

    level_list = []
    print('Input level values one by one, "s" to stop:')
    level = input()
    while (level != 's'):
        level_list.append(level)
        level = input()
    print()

    inter_list = []
    inter_flag = input('Interaction? (y/n)')
    if inter_flag == 'y':
        print('Input interaction:')
        stop_flag = ''
        while (stop_flag != 'y'):
            inter_1 = input('Input first var:')
            inter_2 = input('Input second var:')
            inter_list.append((inter_1, inter_2))
            stop_flag = input('Stop inputing? (y/n)')
    print()
          
    fixed_list = []
    fixed = input('Fixed effect? (y/n)')
    if fixed == 'y':
        print('Input fixed effect, "s" to stop:')
        fixed_effect = input()
        while (fixed_effect != 's'):
            fixed_list.append(fixed_effect)
            fixed_effect = input()
    print()

    random_dic ={}
    random = input('Random effect? (y/n)')
    if random == 'y':
        print('Input random effect:')
        stop_flag = ''
        while (stop_flag != 'y'):
            ran_var = input('Input variable:')
            ran_lvl = input('Input level:')
            random_dic[ran_lvl] = ran_var
            stop_flag = input('Stop inputing? (y/n)')
    print()

    res = "Lmer('" + outcome + " ~ "

    if fixed == 'y':
        for var in fixed_list:
            res += "" + var + " + "
    else:
        grand = input('Want to input grand mean intercept? (y/n)')
        if grand == 'y':
            res += "1 + "

    for inter in inter_list:
        res += inter[0] + "*" + inter[1] + " + "

    if random == 'y':
        for lvl in random_dic.keys():
            res += "(" + random_dic.get(lvl) + "|" + lvl + ") + "
    if len(random_dic.keys()) != len(level_list):
        res += "(1|"
        level_group = ""
        for lvl in level_list:
            if lvl not in random_dic.keys():
                level_group += lvl + "/"
        level_group = level_group[:-1]
        res += level_group + ")"

    res += "')"

    name = ""

    if random == 'y' and fixed == 'y':
        name += 'Mixed effect, '
    elif random == 'n':
        name += 'Fixed effect, '
    else:
        name += 'Random effect, '

    name += str(len(level_list)) + '-level, '

    if inter_flag == 'y':
        name += 'interation '

    name += 'model'

    return res, name

def main():
    """
    Generates the formular specified by the user
    """
    f, n = formular_creator()
    print(f)
    print(n)

if __name__ == '__main__':
    main()





