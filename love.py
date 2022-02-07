from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
from zodiac_sign import get_zodiac_sign
from age_difference import age
from horoscope import horoscope
from emoji import emojize


# girl info information 😍
print(emojize("👧👧👧👧 GIRL's TIME 👧👧👧👧👧👧"))
girl_name = input(Fore.LIGHTBLUE_EX + "What's the girl's name ? \n => ")
girl_birthday = input(Fore.LIGHTBLUE_EX + "What's Her date of birth => ")
day, month, year = girl_birthday.split('-')
girl_zodiac_sign = get_zodiac_sign(int(day), int(month))
print('')
print('')
print(emojize("👦👦👦👦 BOY's TIME 👦👦👦👦"))
boy_name = input(Fore.LIGHTGREEN_EX + "What's the boy's name ? \n => ")
boy_birthday = input(Fore.LIGHTGREEN_EX +"What is his date of birth => ")
day, month, year = boy_birthday.split('-')
boy_zodiac_sign = get_zodiac_sign(int(day), int(month))
print('')
print('')

'''
👌 Perfect Macth: fire and wind - earth and water
👍 Good Match : earth and earth - water and water
❎ Earthache without effort : fire and water - earth and fire - wind and earth
'''

color = {
        'Water' : Fore.CYAN + 'Water',
        'Earth' : Fore.MAGENTA + 'Earth',
        'Fire' : Fore.RED + 'Fire',
        'Wind' : Fore.GREEN + 'Wind',
}
girl_in_malagasy = horoscope[girl_zodiac_sign]['In Malagasy'].capitalize()
boy_in_malagasy = horoscope[boy_zodiac_sign]['In Malagasy'].capitalize()
love = 50

girl_element = horoscope[girl_zodiac_sign]['Element']
boy_element = horoscope[boy_zodiac_sign]['Element']

print(emojize(Fore.LIGHTRED_EX + '🍃🍃🍃🍃 ELEMENT 🍃🍃🍃🍃'))
print(f"{girl_name}'s element is  {color[girl_element]}")
print(f"{boy_name}'s element is  {color[boy_element]}")
print(emojize('🍃🍃🍃🍃 ELEMENT 🍃🍃🍃🍃'))

print('')
print('           🥁🥁🥁🥁🥁🥁🥁🥁🥁 Horoscope Result 🥁🥁🥁🥁🥁🥁🥁🥁🥁              ')
print('')

if girl_element == boy_element:
    love += 10
    print(f'''
                {boy_name} and {girl_name},
                You have the same element,
                you are a good match, 
            so 10 points will be added to love''')

elif (girl_element == 'Wind' and boy_element== 'Earth') or (girl_element == 'Earth' and boy_element == 'Fire') or (girl_element == 'Fire' and boy_element == 'Water') or (girl_element == 'Water' and boy_element == 'Wind'):
    love -= 15
    print(f'''
                    {boy_name} and {girl_name}, 
                Sorry, but you aren't made to be together, 
              *** 15 point will be deducted from love ***''')
elif (boy_element == 'Wind' and girl_element== 'Earth') or (boy_element == 'Earth' and girl_element == 'Fire') or (boy_element == 'Fire' and girl_element == 'Water') or (boy_element == 'Water' and girl_element == 'Wind'):
    love -= 5
    print(f'''
                    {boy_name} and {girl_name}, s
               It will be difficult but you can do it, 
            *** 5 point will be deducted from love ****''')

else:
    love += 20
    print(f'''
                {boy_name} 🔔 {girl_name}
            You are a match made by the heaven, the perfect match,
                Send me an invitation 
                Congratulations, 
    ''')


print(f'love is {love}')
print(f'The days difference is {age(girl_birthday, boy_birthday)}')
