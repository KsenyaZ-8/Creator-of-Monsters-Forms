import file_operations
from faker import Faker
import random


fake = Faker('ru_RU')
runic_alphabet = {
    'а': 'а͠', 
    'б': 'б̋', 
    'в': 'в͒͠',
    'г': 'г͒͠', 
    'д': 'д̋', 
    'е': 'е͠',
    'ё': 'ё͒͠', 
    'ж': 'ж͒', 
    'з': 'з̋̋͠',
    'и': 'и', 
    'й': 'й͒͠', 
    'к': 'к̋̋',
    'л': 'л̋͠', 
    'м': 'м͒͠', 
    'н': 'н͒',
    'о': 'о̋', 
    'п': 'п̋͠', 
    'р': 'р̋͠',
    'с': 'с͒', 
    'т': 'т͒', 
    'у': 'у͒͠',
    'ф': 'ф̋̋͠', 
    'х': 'х͒͠', 
    'ц': 'ц̋',
    'ч': 'ч̋͠', 
    'ш': 'ш͒͠', 
    'щ': 'щ̋',
    'ъ': 'ъ̋͠', 
    'ы': 'ы̋͠', 
    'ь': 'ь̋',
    'э': 'э͒͠͠', 
    'ю': 'ю̋͠', 
    'я': 'я̋',
    'А': 'А͠', 
    'Б': 'Б̋', 
    'В': 'В͒͠',
    'Г': 'Г͒͠', 
    'Д': 'Д̋', 
    'Е': 'Е',
    'Ё': 'Ё͒͠', 
    'Ж': 'Ж͒', 
    'З': 'З̋̋͠',
    'И': 'И', 
    'Й': 'Й͒͠', 
    'К': 'К̋̋',
    'Л': 'Л̋͠', 
    'М': 'М͒͠', 
    'Н': 'Н͒',
    'О': 'О̋', 
    'П': 'П̋͠', 
    'Р': 'Р̋͠',
    'С': 'С͒', 
    'Т': 'Т͒', 
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 
    'Х': 'Х͒͠', 
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 
    'Ш': 'Ш͒͠', 
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 
    'Ы': 'Ы̋͠', 
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 
    'Ю': 'Ю̋͠', 
    'Я': 'Я̋',
    ' ': ' '
}
skills = [
    'Стремительный прыжок', 
    'Электрический выстрел', 
    'Ледяной удар', 
    'Стремительный удар', 
    'Кислотный взгляд', 
    'Тайный побег', 
    'Ледяной выстрел', 
    'Огненный заряд'
]

number_of_skills_in_form = 3
min_grade = 8
max_grade = 14
runic_skills = []
forms_total_nunber = 10

for skill in skills:
    for letter in skill:
        skill = skill.replace(letter, runic_alphabet[letter]) 
    runic_skills.append(skill)  

for number in range(1, forms_total_nunber, +1):
    skills_for_hero = random.sample(runic_skills, number_of_skills_in_form) 
    skill_1, skill_2, skill_3 = skills_for_hero

    context = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'job': fake.job(),
        'town': fake.city(),
        'strength': random.randint(min_grade, max_grade),
        'agility': random.randint(min_grade, max_grade),
        'endurance': random.randint(min_grade, max_grade),
        'intelligence': random.randint(min_grade, max_grade), 
        'luck': random.randint(min_grade, max_grade),
        'skill_1': skill_1,
        'skill_2': skill_2,
        'skill_3': skill_3
    }
    file_operations.render_template('src/charsheet.svg', f'output/monsters_form_{number}.svg', context)
