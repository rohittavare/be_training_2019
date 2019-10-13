import csv
from pokemon.models import Pokemon
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('../postgres/pokemon.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            count = 0
            for row in spamreader:

                if count != 0:
                    new_pokemon = Pokemon(
                        abilities = row[0],
                        against_bug=row[1],
                        against_dark=row[2],
                        against_dragon=row[3],
                        against_electric=row[4],
                        against_fairy=row[5],
                        against_fight=row[6],
                        against_fire=row[7],
                        against_flying=row[8],
                        against_ghost=row[9],
                        against_grass=row[10],
                        against_ground=row[11],
                        against_ice=row[12],
                        against_normal=row[13],
                        against_poison=row[14],
                        against_psychic=row[15],
                        against_rock=row[16],
                        against_steel=row[17],
                        against_water=row[18],
                        attack=row[19],
                        base_egg_steps=row[20],
                        base_happiness=row[21],
                        base_total=row[22],
                        capture_rate=row[23],
                        classfication=row[24],
                        defense=row[25],
                        experience_growth=row[26],
                        height_m=row[27],
                        hp=row[28],
                        japanese_name=row[29],
                        name=row[30],
                        percentage_male=row[31],
                        pokedex_number=row[32],
                        sp_attack=row[33],
                        sp_defense=row[34],
                        speed=row[35],
                        type1=row[36],
                        type2=row[37],
                        weight_kg=row[38],
                        generation=row[39],
                        is_legendary=row[40]
                    )
                    new_pokemon.save()
                # except:
                #     with open('failed.txt', 'a+') as file:
                #         file.write('Error:' + row[29] + '\n')
                #     print("Error: " + row[29])
                count += 1
# some logic here



