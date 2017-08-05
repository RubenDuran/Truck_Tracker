import urllib2
import re
from bs4 import BeautifulSoup

trucks_url = [
    "https://www.monsterjam.com/en-US/trucks",
    "https://www.monsterjam.com/en-US/trucks?page=1",
    "https://www.monsterjam.com/en-US/trucks?page=2"
    ]
trucks = []
truck_imgs= []

for truck in trucks_url:

    req = urllib2.Request(truck, headers={'User-Agent' : "Magic Browser"})
    soup = BeautifulSoup(urllib2.urlopen( req ), "lxml")
    all_trucks=soup.find_all(name='span', class_='field-content')
    for truck in all_trucks:
        name=truck.get_text()
        trucks.append(name)

    all_truck_imgs=soup.find_all('div', class_='field-content',)
    for truck in all_truck_imgs:
        truck_imgs.append(truck.find('img')['src'])


truck_img_and_name = []
if len(trucks) != len(truck_imgs):
    del truck_imgs[len(trucks):]

for i in range(len(trucks)):
    temp=[trucks[i], truck_imgs[i]]
    truck_img_and_name.append(temp)

print truck_img_and_name

for truck in truck_img_and_name:
    print truck[0]
    print truck[1]
    Category.objects.create(category_name=truck[0], image_url=truck[1])

return redirect('/trucks')


def temp(request):
    truck_list = [[u'Aftershock', 'https://www.monsterjam.com/sites/default/files/Aftershock.jpg'], [u'Alien Invasion', 'https://www.monsterjam.com/sites/default/files/Alien%20Invasion%201021-680_1.jpg'], [u'Avenger', 'https://www.monsterjam.com/sites/default/files/Avenger2017.jpg'], [u'Bad News Travels Fast', 'https://www.monsterjam.com/sites/default/files/BadNewsTravelsFast16_02.jpg'], [u'Barbarian', 'https://www.monsterjam.com/sites/default/files/Barbarian2017.jpg'], [u'Big Kahuna', 'https://www.monsterjam.com/sites/default/files/BigKahuna16_02.jpg'], [u'Black Stallion', 'https://www.monsterjam.com/sites/default/files/BlackStallion16_01.jpg'], [u'Blue Thunder', 'https://www.monsterjam.com/sites/default/files/BlueThunder16_02.jpg'], [u'Bounty Hunter','https://www.monsterjam.com/sites/default/files/BountyHunter17.jpg'], [u'Brutus','https://www.monsterjam.com/sites/default/files/Brutus16_01.jpg'],[u'CarolinaCrusher','https://www.monsterjam.com/sites/default/files/CarolinaCrusher16_01.jpg'], [u'Devastator', 'https://www.monsterjam.com/sites/default/files/Devastator.jpg'], [u'Dragon', 'https://www.monsterjam.com/sites/default/files/Dragon16_02.jpg'], [u'EarthShaker', 'https://www.monsterjam.com/sites/default/files/EarthShaker16_01.jpg'], [u'El Toro Loco', 'https://www.monsterjam.com/sites/default/files/ElToroLocoOrange16_04.jpg'], [u'Fluffy', 'https://www.monsterjam.com/sites/default/files/Fluffy.jpg'], [u'FS1 Cleatus', 'https://www.monsterjam.com/sites/default/files/FS1Cleatus17.jpg'], [u'Fullboar 2.0', 'https://www.monsterjam.com/sites/default/files/Fullboar%202.0.jpg'], [u'Gas Monkey Garage', 'https://www.monsterjam.com/sites/default/files/GasMonkeyGarage16_02_0.jpg'], [u'Grave Digger ', 'https://www.monsterjam.com/sites/default/files/GraveDigger16_02.jpg'], [u'Great Clips Mohawk Warrior', 'https://www.monsterjam.com/sites/default/files/Great%20Clips%20bio.jpg'], [u'Hooked', 'https://www.monsterjam.com/sites/default/files/Hooked16_02.jpg'], [u'Hotsy', 'https://www.monsterjam.com/sites/default/files/Hotsy15_01.jpg'], [u'Hurricane Force', 'https://www.monsterjam.com/sites/default/files/HurricaneForce16_02.jpg'], [u'Ice Cream Man', 'https://www.monsterjam.com/sites/default/files/IceCreamMan16_02.jpg'], [u'Incinerator', 'https://www.monsterjam.com/sites/default/files/Incinerator16_01.jpg'], [u'Instigator', 'https://www.monsterjam.com/sites/default/files/Instigator16_02.jpg'], [u'Iron Outlaw',
     'https://www.monsterjam.com/sites/default/files/IronOutlaw2017.jpg'], [u'Jailbird', 'https://www.monsterjam.com/sites/default/files/Jailbird16_01.jpg'], [u'Jester', 'https://www.monsterjam.com/sites/default/files/Jester2017.jpg'], [u'Krazy Train', 'https://www.monsterjam.com/sites/default/files/KrazyTrain16_01.jpg'], [u'Lucas Oil Crusader', 'https://www.monsterjam.com/sites/default/files/LucasOilCrusader16_01.jpg'], [u'Madusa', 'https://www.monsterjam.com/sites/default/files/Madusa15_03.jpg'], [u'Master of Disaster', 'https://www.monsterjam.com/sites/default/files/master%20of%20Disaster17.jpg'], [u'Max-D', 'https://www.monsterjam.com/sites/default/files/Max-D16_01.jpg'], [u'McGruff', 'https://www.monsterjam.com/sites/default/files/McGruff15_01.jpg'],
     [u'Mechanical Mischief','https://www.monsterjam.com/sites/default/files/MechanicalMischief16_01.jpg'],
     [u'Megalodon','https://www.monsterjam.com/sites/default/files/Megalodon%20real.jpg'], [u'Metal Mulisha', 'https://www.monsterjam.com/sites/default/files/MetalMulisha17_02.jpg'], [u'Midnight Rider', 'https://www.monsterjam.com/sites/default/files/MidnightRider16_01.jpg'], [u'Monster Energy ', 'https://www.monsterjam.com/sites/default/files/MonsterEnergy17_02%20Damon.jpg'], [u'Monster Mutt', 'https://www.monsterjam.com/sites/default/files/MonsterMutt16_01.jpg'], [u'Monster Mutt Dalmatian', 'https://www.monsterjam.com/sites/default/files/MonsterMuttDalmatian16_02.jpg'], [u'Monster Mutt Rottweiler', 'https://www.monsterjam.com/sites/default/files/MonsterMuttRottweiler16_02.jpg'], [u'Mutant', 'https://www.monsterjam.com/sites/default/files/Mutantbio.jpg'], [u'New Earth Authority ', 'https://www.monsterjam.com/sites/default/files/NEA_Blue16_03.jpg'], [u'Northern Nightmare ', 'https://www.monsterjam.com/sites/default/files/NorthernNightmare16_01%202.jpg'], [u'Obsessed', 'https://www.monsterjam.com/sites/default/files/Obsessed16_01.jpg'], [u'Obsession ', 'https://www.monsterjam.com/sites/default/files/Obsession2017.jpg'], [u'Over Bored', 'https://www.monsterjam.com/sites/default/files/OverBored16_01_0.jpg'], [u'Overkill Evolution ', 'https://www.monsterjam.com/sites/default/files/OverkillEvolution16_02.jpg'], [u"Pirate's Curse", 'https://www.monsterjam.com/sites/default/files/PiratesCurse16_01.jpg'], [u'Predator', 'https://www.monsterjam.com/sites/default/files/Predator16_02.jpg'], [u'Prowler', 'https://www.monsterjam.com/sites/default/files/Prowler16_01.jpg'], [u'RAGE', 'https://www.monsterjam.com/sites/default/files/Rage16_02.jpg'], [u'Raminator', 'https://www.monsterjam.com/sites/default/files/Raminator16_01.jpg'], [u'Rammunition', 'https://www.monsterjam.com/sites/default/files/Rammunition16_01.jpg'], [u'Razin Kane', 'https://www.monsterjam.com/sites/default/files/RazinKane16_02.jpg'], [u'Saigon Shaker', 'https://www.monsterjam.com/sites/default/files/SaigonShaker16_01.jpg'], [u'Scarlet Bandit ', 'https://www.monsterjam.com/sites/default/files/scarletbandit2017.jpg'], [u'Scooby-Doo', 'https://www.monsterjam.com/sites/default/files/Scooby-Doo16_01.jpg'], [u'Slinger', 'https://www.monsterjam.com/sites/default/files/Slinger17_01.jpg'], [u'Soldier Fortune', 'https://www.monsterjam.com/sites/default/files/SoldierFortune16_01.jpg'], [u'Soldier Fortune Black Ops', 'https://www.monsterjam.com/sites/default/files/SoldierFortune%20%20Black%20ops%20thumb.jpg'], [u'Son-uva Digger', 'https://www.monsterjam.com/sites/default/files/Son-uvaDigger16_01.jpg'], [u'Stinger', 'https://www.monsterjam.com/sites/default/files/Stinger16_02.jpg'], [u'Stone Crusher', 'https://www.monsterjam.com/sites/default/files/StoneCrusher16_02.jpg'], [u'Storm Damage', 'https://www.monsterjam.com/sites/default/files/StormDamage16_02.jpg'], [u'Team Hot Wheels Firestorm', 'https://www.monsterjam.com/sites/default/files/TeamHotWheelsFirestorm16_01.jpg'], [u'Thunder 4X4', 'https://www.monsterjam.com/sites/default/files/Thunder4x416_02.jpg'], [u'Time Flys', 'https://www.monsterjam.com/sites/default/files/TimeFlys16_01.jpg'], [u'VP Racing Mad Scientist', 'https://www.monsterjam.com/sites/default/files/VPRacingFuelsMadScientist16_01.jpg'], [u'War Wizard ', 'https://www.monsterjam.com/sites/default/files/WarWizard16_02.jpg'], [u'Wild Flower', 'https://www.monsterjam.com/sites/default/files/WildFlower16_02.jpg'], [u'Wild Thang', 'https://www.monsterjam.com/sites/default/files/WildThang16_01.jpg'], [u'Wrecking Crew ', 'https://www.monsterjam.com/sites/default/files/Wrecking%20Crew2017.jpg'], [u'Xtermigator', 'https://www.monsterjam.com/sites/default/files/Xtermigator16_02.jpg'], [u'Xtreme Diesel', 'https://www.monsterjam.com/sites/default/files/XtremeDiesel16_01.jpg'], [u'Zombie', 'https://www.monsterjam.com/sites/default/files/Zombie16_02.jpg']]

    # for truck in truck_list:
    #     print truck[0]
    #     print truck[1]
    #     Category.objects.create(category_name=truck[0], image_url=truck[1])
    #
    # return redirect('/trucks')
