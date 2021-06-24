def print_array(array, format="default"):
    n = len(array)

    if format == "default":
        for i in range(n):
            print("Del dia {} al dia {}: {}".format(i + 1, i + 2, array[i]))
    elif format == "porcentage":
        for i in range(n):
            print("Del dia {} al dia {}: {}%".format(i + 1, i + 2, array[i]))
    else:
        print("INVALID ARGUMENT")


def get_change(array):
    n = len(array) - 1
    aumento_de_casos_por_dia = []

    for i in range(n):
        aumento = array[i + 1] - array[i]
        aumento_de_casos_por_dia.append(aumento)

    return aumento_de_casos_por_dia


def increase_percentage(array):
    n = len(array) - 1
    porcentaje_de_aumento_de_casos_por_dia = []

    for i in range(n):
        porcentaje_de_aumento_de_casos_por_dia.append(round((100 * (array[i + 1] - array[i])) / array[i], 2))
    
    return porcentaje_de_aumento_de_casos_por_dia


def get_growth_factor(casos):
    n = len(casos) - 1
    growth_factor = []
    for i in range(n):
        growth_factor.append(round(casos[i+1] / casos[i], 5)) 
    
    return growth_factor


def get_average_growth_factor(growth_factor):
    n = len(growth_factor)
    sum = 0

    for i in range(n - 1):
        sum = sum + growth_factor[i]

    average_growth_factor = sum / n

    return average_growth_factor


def get_expected_cases(average_growth_factor, current_cases):
    expected_cases = round(current_cases * average_growth_factor)

    return expected_cases


def get_status_statistics(cases, deaths, in_house, in_hospital, in_intensive_care):
    status_statistics = {}

    status_statistics["death_porcentage"] = round((deaths / cases) * 100, 2)
    status_statistics["in_house_porcentage"] = round((in_house / cases) * 100, 2)
    status_statistics["in_hospital_porcentage"] = round((in_hospital / cases) * 100, 2)
    status_statistics["in_intensive_care_porcentage"] =  round((in_intensive_care / cases) * 100, 2)

    return status_statistics


def main():
    cases_per_day = [1, 8, 14, 27, 36, 43, 55, 69, 86, 109, 137, 200, 245, 313, 345, 443, 558, 674, 786, 901, 989, 1075, 1181] #1, 8, 14,
    cases_per_day_length = len(cases_per_day) 
    deaths = 30
    in_house = 969
    in_hospital = 123
    in_intensive_care = 50
    
    status_statistics = get_status_statistics(cases_per_day[cases_per_day_length - 1], deaths, in_house, in_hospital, in_intensive_care)
    

    print("Aumento de casos al dia: ")
    print_array(get_change(cases_per_day))

    print("")

    print("Porcentaje de aumento de casos al dia: ")
    print_array(increase_percentage(cases_per_day), "porcentage") 

    print("")

    print("Estadistica del estado de los casos: ")
    print("Porcentaje de muerte: {}%".format(status_statistics["death_porcentage"]))
    print("Porcentaje de casos en casa: {}%".format(status_statistics["in_house_porcentage"]))
    print("Porcentaje de casos en sala: {}%".format(status_statistics["in_hospital_porcentage"]))
    print("Porcentaje de casos en cuidados intensivos: {}%".format(status_statistics["in_intensive_care_porcentage"]))

    print("")

    print("Factor de crecimiento por dia: ")
    print_array(get_growth_factor(cases_per_day))

    print("")

    print("Factor de crecimiento promedio: ")
    print(get_average_growth_factor(get_growth_factor(cases_per_day)))

    print("")

    print("Casos esperados para el dia {}: {}".format(
        cases_per_day_length + 1, 
        get_expected_cases(
            get_average_growth_factor(
                get_growth_factor(cases_per_day)
                ), 
                cases_per_day[cases_per_day_length - 1]
            )
        ))


if __name__ == "__main__":
    main()

