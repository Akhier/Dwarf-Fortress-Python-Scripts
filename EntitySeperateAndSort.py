#Reads all entity text files in the current director
#Moves those files to a zip folder that is timestamped
#Then makes new files for each seperate entity which are sorted
#Version Changelog:
#1.0 Completed Jan-23-2015 by Akhier Dragonheart
#1.1 Now headers only show up if they have something under them
#1.2 Changed backup folder to zipping the backups and timestamping them
#1.3 Now only does stuff if something to do
import glob
import re
import os
import zipfile
import time
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def write_entity(entity):
    with open('entity_' + entity + '.txt', 'w') as file:
        file.write('entity_' + entity + '\n\n[OBJECT:ENTITY]\n\n')
        gameplay = []
        placement = []
        population = []
        flavor = []
        religion = []
        tissue = []
        position = {}
        listOfPositions = []
        currentPosition = ""
        leadership = []
        permission = []
        behavior = []
        resource = []
        animal = []
        plant = []
        harvesting = []
        equipment = []
        misc = []
        for line in entities[entity]:
            if re.match(r'(\[ENTITY:)', line):
                file.write(line + '\n')
            elif re.search(p_gameplay, line):
                gameplay.append(line)
            elif re.search(p_placement, line):
                placement.append(line)
            elif re.search(p_population, line):
                population.append(line)
            elif re.search(p_flavor, line):
                flavor.append(line)
            elif re.search(p_religion, line):
                religion.append(line)
            elif re.search(p_tissue, line):
                tissue.append(line)
            elif re.search(p_position, line):
                currentPosition = find_between(line, ':', ']')
                listOfPositions.append(currentPosition)
                position[currentPosition] = []
            elif currentPosition != "" and re.search(p_subposition, line):
                position[currentPosition].append(line)
            elif re.search(p_leadership, line):
                leadership.append(line)
            elif re.search(p_permission, line):
                permission.append(line)
            elif re.search(p_behavior, line):
                behavior.append(line)
            elif re.search(p_resource, line):
                resource.append(line)
            elif re.search(p_animal, line):
                animal.append(line)
            elif re.search(p_plant, line):
                plant.append(line)
            elif re.search(p_harvesting, line):
                harvesting.append(line)
            elif re.search(p_equipment, line):
                equipment.append(line)
            else:
                misc.append(line)
        
        if gameplay or placement or population:
            file.write('\n==================================================\n' + 
                       'Entity Basics\n' + 
                       '==================================================\n')
            if gameplay:
                file.write('    Gameplay Tokens\n' +    
                           '    ----------------------------------------------\n')
                gameplay.sort()
                for line in gameplay:
                    file.write('    ' + line + '\n')

            if placement:
                file.write('\n    Placement Tokens\n' +    
                           '    ----------------------------------------------\n')
                placement.sort()
                for line in placement:
                    file.write('    ' + line + '\n')

            if population:
                file.write('\n    population Tokens\n' +    
                           '    ----------------------------------------------\n')
                population.sort()
                for line in population:
                    file.write('    ' + line + '\n')

        if flavor or religion or tissue:
            file.write('\n==================================================\n' + 
                       'Fluff\n' + 
                       '==================================================\n')
            if flavor:
                file.write('\n    Flavor Tokens\n' +    
                           '    ----------------------------------------------\n')
                flavor.sort()
                for line in flavor:
                    file.write('    ' + line + '\n')

            if religion:
                file.write('\n    Religion Tokens\n' +    
                           '    ----------------------------------------------\n')
                religion.sort()
                for line in religion:
                    file.write('    ' + line + '\n')

            if tissue:
                file.write('\n    Tissue Styling Tokens\n' +    
                           '    ----------------------------------------------\n')
                tissue.sort()
                for line in tissue:
                    file.write('    ' + line + '\n')

        if listOfPositions or leadership:
            file.write('\n==================================================\n' + 
                       'Leadership Tokens\n' + 
                       '==================================================\n')
            listOfPositions.sort()
            for item in listOfPositions:
                for line in position[item]:
                    if '[NAME' not in line:
                        file.write('    ')
                    
                    file.write('    ' + line + '\n')
                    
            leadership.sort()
            for line in leadership:
                file.write('    ' + line + '\n')

        if permission or behavior:
            file.write('\n==================================================\n' + 
                       'Capabilities\n' + 
                       '==================================================\n')
            if permission:
                file.write('\n    Permission Tokens\n' +    
                           '    ----------------------------------------------\n')
                permission.sort()
                for line in permission:
                    file.write('    ' + line + '\n')

            if behavior:
                file.write('\n    Behavior Tokens\n' +    
                           '    ----------------------------------------------\n')
                behavior.sort()
                for line in behavior:
                    file.write('    ' + line + '\n')

        if resource or animal or plant or harvesting or equipment:
            file.write('\n==================================================\n' + 
                       'Resources\n' + 
                       '==================================================\n')
            if resource:
                file.write('\n    General Resource Tokens\n' +    
                           '    ----------------------------------------------\n')
                resource.sort()
                for line in resource:
                    file.write('    ' + line + '\n')

            if animal:
                file.write('\n    Animal Tokens\n' +    
                           '    ----------------------------------------------\n')
                animal.sort()
                for line in animal:
                    file.write('    ' + line + '\n')

            if plant:
                file.write('\n    Plant Tokens\n' +    
                           '    ----------------------------------------------\n')
                plant.sort()
                for line in plant:
                    file.write('    ' + line + '\n')

            if harvesting:
                file.write('\n    Harvesting Tokens\n' +    
                           '    ----------------------------------------------\n')
                harvesting.sort()
                for line in harvesting:
                    file.write('    ' + line + '\n')

            if equipment:
                file.write('\n    Equipment Tokens\n' +    
                           '    ----------------------------------------------\n')
                equipment.sort()
                for line in equipment:
                    file.write('    ' + line + '\n')

        if misc:
            file.write('\n==================================================\n' + 
                       'Misc\n' + 
                       '==================================================\n')
            misc.sort()
            for line in misc:
                file.write('    ' + line + '\n')

contents = []
entityFiles = glob.glob('entity_*')
if entityFiles:
    for filename in entityFiles:
        with open(filename) as ef:
            for line in ef:
                contents.append(line)

    with zipfile.ZipFile('EntityBackup_' +
                         time.strftime("%b-%d-%Y_%H-%M-%S") +
                         '.zip', mode = 'w') as backupZip:
        for filename in entityFiles:
            backupZip.write(filename, compress_type=compression)
            os.remove(filename)

    entities = {}
    currentEntity = ""
    for line in contents:
        if '[' in line:
            if re.match(r'(\[OBJECT:ENTITY\])', line):
                pass
            elif re.match(r'(\[ENTITY:)', line):
                currentEntity = find_between(line, ':', ']').lower()
                entities[currentEntity] = []
                entities[currentEntity].append('[' + find_between(line, '[', ']') + ']')
            elif currentEntity != "":
                entities[currentEntity].append('[' + find_between(line, '[', ']') + ']')

    p_gameplay = re.compile(r'(ADVENTURE_TIER|INDIV_CONTROLLABLE|CIV_CONTROLLABLE|CREATURE:|CREATURE_HFID)')
    p_placement = re.compile(r'(START_BIOME|EXCLUSIVE_START_BIOME|DEFAULT_SITE_TYPE|BIOME_SUPPORT|SETTLEMENT_BIOME|LIKES_SITE|TOLERATES_SITE|WORLD_CONSTRUCTION)')
    p_population = re.compile(r'(MAX_POP_NUMBER|MAX_SITE_POP_NUMBER|MAX_STARTING_CIV_NUMBER)')
    p_flavor = re.compile(r'(CURRENCY_BY_YEAR|TRANSLATION|FRIENDLY_COLOR|CURRENCY:|ART_FACET_MODIFIER|ART_IMAGE_ELEMENT_MODIFIER|ITEM_IMPROVEMENT_MODIFIER|SELECT_SYMBOL|SUBSELECT_SYMBOL|CULL_SYMBOL)')
    p_religion = re.compile(r'(RELIGION:|RELIGION_SPHERE|SPHERE_ALIGNMENT)')
    p_tissue = re.compile(r'(TISSUE_STYLE|TS_MAINTAIN_LENGTH|TS_PREFERRED_SHAPING)')
    p_position = re.compile(r'(POSITION)')
    p_subposition = re.compile(r'(ACCOUNT_EXEMPT|ALLOWED_CLASS|ALLOWED_CREATURE|APPOINTED_BY|BRAG_ON_KILL|CHAT_WORTHY|COLOR:|COMMANDER|CONQUERED_SITE|DEMAND_MAX|DETERMINES_COIN_DESIGN|DO_NOT_CULL|DUTY_BOUND|ELECTED|EXECUTION_SKILL|EXPORTED_IN_LEGENDS|FLASHES|GENDER:|KILL_QUEST|LAND_HOLDER|LAND_NAME|MANDATE_MAX|MENIAL_WORK_EXEMPTION|MENIAL_WORK_EXEMPTION_SPOUSE|MILITARY_SCREEN_ONLY|NAME|NAME_MALE|NAME_FEMALE|NUMBER|PRECEDENCE|PUNISHMENT_EXEMPTION|QUEST_GIVER|REJECTED_CLASS|REJECTED_CREATURE|REPLACED_BY|REQUIRED_BEDROOM|REQUIRED_BOXES|REQUIRED_CABINETS|REQUIRED_DINING|REQUIRED_OFFICE|REQUIRED_RACKS|REQUIRED_STANDS|REQUIRED_TOMB|REQUIRED_POPULATION|RESPONSIBILITY|RULES_FROM_LOCATION|SITE\]|SLEEP_PRETENSION|SPECIAL_BURIAL|SPOUSE|SPOUSE_FEMALE|SPOUSE_MALE|SQUAD|SUCCESSION|ACCOUNTING|ATTACK_ENEMIES|BUILD_MORALE|COLLECT_TAXES|EQUIPMENT_MANIFESTS|ESCORT_TAX_COLLECTOR|ESTABLISH_COLONY_TRADE_AGREEMENTS|EXECUTIONS|HEALTH_MANAGEMENT|LAW_ENFORCEMENT|LAW_MAKING|MAKE_INTRODUCTIONS|MAKE_PEACE_AGREEMENTS|MAKE_TOPIC_AGREEMENTS|MANAGE_PRODUCTION|MEET_WORKERS|MILITARY_GOALS|MILITARY_STRATEGY|PATROL_TERRITORY|RECEIVE_DIPLOMATS|RELIGION\]|TRADE)')
    p_leadership = re.compile(r'(LAND_HOLDER_TRIGGER|SITE_VARIABLE_POSITIONS|VARIABLE_POSITIONS)')
    p_permission = re.compile(r'(PERMITTED_BUILDING|PERMITTED_JOB|PERMITTED_REACTION)')
    p_behavior = re.compile(r'(WILL_ACCEPT_TRIBUTE|WANDERER|BEAST_HUNTER|SCOUT|ABUSE_BODIES|AMBUSHER|AT_PEACE_WITH_WILDLIFE|BABYSNATCHER|BUILDS_OUTDOOR_FORTIFICATIONS|BUILDS_OUTDOOR_TOMBS|BANDITRY:|DIPLOMAT_BODYGUARDS|INVADERS_IGNORE_NEUTRALS|ITEM_THIEF|LOCAL_BANDITRY|MECHANT_BODYGUARDS|MERCHANT_NOBILITY|PROGRESS_TRIGGER_POPULATION|PROGRESS_TRIGGER_PRODUCTION|PROGRESS_TRIGGER_TRADE|PROGRESS_TRIGGER_POP_SIEGE|PROGRESS_TRIGGER_PROD_SIEGE|PROGRESS_TRIGGER_TRADE_SIEGE|SIEGER|SKULKING|TREE_CAP_DIPLOMACY|LAYER_LINKED|UNDEAD_CANDIDATE|ETHIC|VALUE|ACTIVE_SEASON|GENERATED)')
    p_resource = re.compile(r'(AMMO|ARMOR|DIGGER|GLOVES|HELM|INSTRUMENT|PANTS|SHIELD|SHOES|SIEGEAMMO|TOOL|TOY|TRAPCOMP|WEAPON:)')
    p_animal = re.compile(r'(USE_ANIMAL_PRODUCTS|USE_ANY_PET_RACE|USE_CAVE_ANIMALS|USE_EVIL_ANIMALS|USE_GOOD_ANIMALS|COMMON_DOMESTIC_MOUNT|COMMON_DOMESTIC_PACK|COMMON_DOMESTIC_PET|COMMON_DOMESTIC_PULL)')
    p_plant = re.compile(r'(USE_EVIL_PLANTS|USE_EVIL_WOOD|USE_GOOD_PLANTS|USE_GOOD_WOOD|USE_MISC_PROCESSED_WOOD_PRODUCTS|INDOOR_WOOD|OUTDOOR_WOOD|WOOD_WEAPONS|WOOD_ARMOR)')
    p_harvesting = re.compile(r'(RIVER_PRODUCTS|OCEAN_PRODUCTS|INDOOR_FARMING|OUTDOOR_FARMING|INDOOR_GARDENS|OUTDOOR_GARDENS|INDOOR_ORCHARDS|OUTDOOR_ORCHARDS)')
    p_equipment = re.compile(r'(CLOTHING\]|SUBTERRANEAN_CLOTHING|EQUIPMENT_IMPROVEMENTS|IMPROVED_BOW|METAL_PREF|STONE_PREF|GEM_PREF|GEM_SHAPE|STONE_SHAPE|DIVINE_MAT_CLOTH|DIVINE_MAT_WEAPONS|DIVINE_MAT_ARMOR)')

    for entity in entities:
        write_entity(entity)

    print('done')
else:
    print('nothing to do')
