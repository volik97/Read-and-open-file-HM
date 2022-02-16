import os

BASE = os.getcwd()
file_name = 'recipes.txt'
file_path = os.path.join(BASE, file_name)
cook_book = {}
def get_cooking_book():
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            dish = line.strip().lower()
            temp_list = []
            for i in range(int(f.readline().strip())):
                value = f.readline().strip()
                split_value = value.split(' | ')
                temp_dict = {'ingridient_name': split_value[0],
                'quantity': int(split_value[1]), 'measure': split_value[2]}
                temp_list.append(temp_dict)
            f.readline()
            cook_book[dish] = temp_list

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите количество персон: '))
    dishes = input('Введите блюда (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

if __name__ == '__main__':
    get_cooking_book()
    create_shop_list()

