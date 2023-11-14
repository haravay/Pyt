import json
def ParseData(line):
    name, _, revenue, costs = line.split()
    revenue = int(revenue)
    costs = int(costs)
    profit = revenue - costs
    return name, profit



companies = []
totalProfit = 0
chProfit = 0
with open('companies.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    if len(lines) < 1:
        print("Данные в файле некорректны")
    else:
        for line in lines:
            name, profit = ParseData(line)
            companies.append({name: profit})
            if profit > 0:
                totalProfit += profit
                chProfit += 1
        AvgProfit = totalProfit / chProfit if chProfit > 0 else 0
        result = [companies, {"AvgProfit": AvgProfit}]

        with open('result.json', 'w', encoding='utf-8') as file:
            json.dump(result, file)

        print(result)