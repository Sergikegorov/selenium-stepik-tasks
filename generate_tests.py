from allpairs import all_pairs2

parameters = [
    ["ЖК", ["Золотое сияние", "Небесный полет"]],
    ["Тип квартиры", ["студия", "1-комнатная", "2-комнатная", "3-комнатная", "4-комнатная"]],
    ["Этаж", [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    ["Отделка", ["черновая", "чистовая"]],
    ["Балкон", ["есть", "нет"]],
]

# Извлекаем только значения для all_pairs2
values = [p[1] for p in parameters]

result = list(all_pairs2(values))

# Вывод в CSV-подобном виде
header = [p[0] for p in parameters]
print(",".join(header))
for row in result:
    print(",".join(str(v) for v in row))
