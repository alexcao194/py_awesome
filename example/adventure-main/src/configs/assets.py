from py_awesome import *

class Assets(Singleton):
    # Animations
   ani_monster_idle = 'assets/animations/monster/monster_idle/'
   ani_monster_dead = 'assets/animations/monster/monster_dead/'
   ani_monster_die = 'assets/animations/monster/monster_die/'
   ani_monster_stand = 'assets/animations/monster/monster_stand/'
   ani_monster_attack_skewer = 'assets/animations/monster/attack/monster_attack_skewer/'
   ani_monster_attack_arround = 'assets/animations/monster/attack/monster_attack_arround/'
   ani_monsterattack_dam = 'assets/animations/monster/attack/monsterattack_dam/'
   ani_monster_run = 'assets/animations/monster/monster_run/'
   ani_death = 'assets/animations/hero/death/'
   ani_run_behind = 'assets/animations/hero/run/run_behind/'
   ani_run_opposite = 'assets/animations/hero/run/run_opposite/'
   ani_run_right = 'assets/animations/hero/run/run_right/'
   ani_run_left = 'assets/animations/hero/run/run_left/'
   ani_die = 'assets/animations/hero/die/'
   ani_attack_opposite = 'assets/animations/hero/attack/attack_opposite/'
   ani_attack_right = 'assets/animations/hero/attack/attack_right/'
   ani_attack_behind = 'assets/animations/hero/attack/attack_behind/'
   ani_attack_left = 'assets/animations/hero/attack/attack_left/'
   ani_walk_behind = 'assets/animations/hero/walk/walk_behind/'
   ani_walk_right = 'assets/animations/hero/walk/walk_right/'
   ani_walk_left = 'assets/animations/hero/walk/walk_left/'
   ani_walk_opposite = 'assets/animations/hero/walk/walk_opposite/'

# Textures
   tt_flag_vi = 'assets/textures/flag/flag_vi.png'
   tt_flag_uk = 'assets/textures/flag/flag_uk.png'
   tt_block_5 = 'assets/textures/block/block_5.png'
   tt_block_4 = 'assets/textures/block/block_4.png'
   tt_block_1 = 'assets/textures/block/block_1.png'
   tt_block_3 = 'assets/textures/block/block_3.png'
   tt_block_2 = 'assets/textures/block/block_2.png'
   tt_background = 'assets/textures/background/background.jpg'
   tt_background_setting_toggle_music_on = 'assets/textures/background/background_setting_toggle_music_on.png'
   tt_background_setting_toggle_audio_on = 'assets/textures/background/background_setting_toggle_audio_on.png'
   tt_background_button = 'assets/textures/background/background_button.png'
   tt_button_close = 'assets/textures/background/button_close.png'
   tt_background_loose = 'assets/textures/background/background_loose.png'
   tt_background_setting = 'assets/textures/background/background_setting.jpg'
   tt_background_about = 'assets/textures/background/background_about.png'
   tt_background_setting_toggle_audio_off = 'assets/textures/background/background_setting_toggle_audio_off.png'
   tt_background_setting_toggle_music_off = 'assets/textures/background/background_setting_toggle_music_off.png'
   tt_box_0 = 'assets/textures/map/props/box/box_0.png'
   tt_box_1 = 'assets/textures/map/props/box/box_1.png'
   tt_column_stone_2 = 'assets/textures/map/props/column_stone/column_stone_2.png'
   tt_column_stone_1 = 'assets/textures/map/props/column_stone/column_stone_1.png'
   tt_column_stone_0 = 'assets/textures/map/props/column_stone/column_stone_0.png'
   tt_door_0 = 'assets/textures/map/props/door/door_0.png'
   tt_door_1 = 'assets/textures/map/props/door/door_1.png'
   tt_direction_1 = 'assets/textures/map/props/direction/direction_1.png'
   tt_direction_0 = 'assets/textures/map/props/direction/direction_0.png'
   tt_bin_1 = 'assets/textures/map/props/bin/bin_1.png'
   tt_bin_0 = 'assets/textures/map/props/bin/bin_0.png'
   tt_bin_3 = 'assets/textures/map/props/bin/bin_3.png'
   tt_bin_2 = 'assets/textures/map/props/bin/bin_2.png'
   tt_headstone_3 = 'assets/textures/map/props/headstone/headstone_3.png'
   tt_headstone_1 = 'assets/textures/map/props/headstone/headstone_1.png'
   tt_headstone_4 = 'assets/textures/map/props/headstone/headstone_4.png'
   tt_headstone_5 = 'assets/textures/map/props/headstone/headstone_5.png'
   tt_headstone_6 = 'assets/textures/map/props/headstone/headstone_6.png'
   tt_headstone_0 = 'assets/textures/map/props/headstone/headstone_0.png'
   tt_headstone_2 = 'assets/textures/map/props/headstone/headstone_2.png'
   tt_stone_2 = 'assets/textures/map/props/stone/stone_2.png'
   tt_stone_6 = 'assets/textures/map/props/stone/stone_6.png'
   tt_stone_3 = 'assets/textures/map/props/stone/stone_3.png'
   tt_stone_0 = 'assets/textures/map/props/stone/stone_0.png'
   tt_stone_5 = 'assets/textures/map/props/stone/stone_5.png'
   tt_stone_4 = 'assets/textures/map/props/stone/stone_4.png'
   tt_stone_8 = 'assets/textures/map/props/stone/stone_8.png'
   tt_stone_7 = 'assets/textures/map/props/stone/stone_7.png'
   tt_stone_1 = 'assets/textures/map/props/stone/stone_1.png'
   tt_stone_9 = 'assets/textures/map/props/stone/stone_9.png'
   tt_conffin_1 = 'assets/textures/map/props/conffin/conffin_1.png'
   tt_conffin_0 = 'assets/textures/map/props/conffin/conffin_0.png'
   tt_chair_0 = 'assets/textures/map/props/chair/chair_0.png'
   tt_chair_2 = 'assets/textures/map/props/chair/chair_2.png'
   tt_chair_1 = 'assets/textures/map/props/chair/chair_1.png'
   tt_statue_0 = 'assets/textures/map/props/statue/statue_0.png'
   tt_box2_1 = 'assets/textures/map/props/box2/box2_1.png'
   tt_box2_0 = 'assets/textures/map/props/box2/box2_0.png'
   tt_well_1 = 'assets/textures/map/props/well/well_1.png'
   tt_well_0 = 'assets/textures/map/props/well/well_0.png'
   tt_struct_6 = 'assets/textures/map/structs/struct_6.png'
   tt_struct_2 = 'assets/textures/map/structs/struct_2.png'
   tt_struct_7 = 'assets/textures/map/structs/struct_7.png'
   tt_struct_0 = 'assets/textures/map/structs/struct_0.png'
   tt_struct_3 = 'assets/textures/map/structs/struct_3.png'
   tt_struct_4 = 'assets/textures/map/structs/struct_4.png'
   tt_struct_1 = 'assets/textures/map/structs/struct_1.png'
   tt_struct_5 = 'assets/textures/map/structs/struct_5.png'
   tt_tileset_wall_8 = 'assets/textures/map/tileset_wall/tileset_wall_8.png'
   tt_tileset_wall_3 = 'assets/textures/map/tileset_wall/tileset_wall_3.png'
   tt_tileset_wall_7 = 'assets/textures/map/tileset_wall/tileset_wall_7.png'
   tt_tileset_wall_10 = 'assets/textures/map/tileset_wall/tileset_wall_10.png'
   tt_tileset_wall_9 = 'assets/textures/map/tileset_wall/tileset_wall_9.png'
   tt_tileset_wall_4 = 'assets/textures/map/tileset_wall/tileset_wall_4.png'
   tt_tileset_wall_0 = 'assets/textures/map/tileset_wall/tileset_wall_0.png'
   tt_tileset_wall_1 = 'assets/textures/map/tileset_wall/tileset_wall_1.png'
   tt_tileset_wall_6 = 'assets/textures/map/tileset_wall/tileset_wall_6.png'
   tt_tileset_wall_5 = 'assets/textures/map/tileset_wall/tileset_wall_5.png'
   tt_tileset_wall_2 = 'assets/textures/map/tileset_wall/tileset_wall_2.png'
   tt_plant_7 = 'assets/textures/map/plants/plant_7.png'
   tt_plant_0 = 'assets/textures/map/plants/plant_0.png'
   tt_plant_1 = 'assets/textures/map/plants/plant_1.png'
   tt_plant_6 = 'assets/textures/map/plants/plant_6.png'
   tt_plant_5 = 'assets/textures/map/plants/plant_5.png'
   tt_plant_4 = 'assets/textures/map/plants/plant_4.png'
   tt_plant_2 = 'assets/textures/map/plants/plant_2.png'
   tt_plant_8 = 'assets/textures/map/plants/plant_8.png'
   tt_plant_3 = 'assets/textures/map/plants/plant_3.png'
   tt_hero_death = 'assets/textures/hero/death/hero_death.png'
   tt_hero_attack = 'assets/textures/hero/attack/hero_attack.png'
   tt_monster_stand = 'assets/textures/monster/monster_stand.png'
   tt_background_firework_1 = 'assets/textures/background/background_firework_1.png'
   tt_background_firework_2 = 'assets/textures/background/background_firework_2.png'

# Sounds
   sd_play = 'assets/sounds/play.wav'
   sd_heal = 'assets/sounds/Heal.wav'
   sd_fireball = 'assets/sounds/Attack/Fireball.wav'
   sd_claw = 'assets/sounds/Attack/Claw.wav'
   sd_slash = 'assets/sounds/Attack/Slash.wav'
   sd_home = 'assets/sounds/home.wav'
   sd_main = 'assets/sounds/Main.ogg'
   sd_hit = 'assets/sounds/Hit.wav'
   sd_fire = 'assets/sounds/Fire.wav'
   sd_sword = 'assets/sounds/Sword.wav'
   sd_death = 'assets/sounds/Death.wav'