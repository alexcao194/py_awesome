from py_awesome import *
from py_awesome import Localization as S
from src.configs.assets import Assets
from src.characters.player import Player
from src.characters.monster import Monster
from src.states.pause import Pause
from src.map.circle_struct import CircleStruct
from src.map.collision_box import CollisionBox
from src.states.loose import Loose
from src.map.box import Box
from src.states.win import Win
from src.map.block import *

class Play(BaseState):
    def __init__(self):
        super().__init__(background=Assets.tt_background)

    def __init_state__(self):
        super().__init_state__()
        AudioManager.play_background(Assets.sd_play)

        self.datas = []
        self.message_group = WidgetGroup()
        self.has_key = False
        self.has_box = False

        #Objects
        self.player = Player(position=Vector2(160,421))
        self.circle_struct = CircleStruct()
        self.block1 = Block(texture=Assets.tt_block_1,hitbox=Vector2(40,100), size=Vector2(53,43), offset=Vector2(0,30),position=Vector2(215,543))
        self.block2 = Block(texture=Assets.tt_block_2,hitbox=Vector2(300,300), size=Vector2(0,1), offset=Vector2(0,23),position=Vector2(0,543))
        self.block3 = Block(texture=Assets.tt_block_3,hitbox=Vector2(0,1), size=Vector2(80,175), offset=Vector2(0,50),position=Vector2(420,680))
        self.block4 = Block(texture=Assets.tt_block_4,hitbox=Vector2(50,20), size=Vector2(100,100), offset=Vector2(0,50),position=Vector2(352,703))
        self.block5 = Block(texture=Assets.tt_block_3,hitbox=Vector2(80,10), size=Vector2(80,189), offset=Vector2(0,50),position=Vector2(1136,678))
        self.block6 = Block(texture=Assets.tt_block_2,hitbox=Vector2(298,300), size=Vector2(0,1), offset=Vector2(0,25),position=Vector2(1016,703))
        self.block7 = Block(texture=Assets.tt_block_2,hitbox=Vector2(50,320), size=Vector2(0,1), offset=Vector2(0,25),position=Vector2(30,225))
        self.block8 = Block(texture=Assets.tt_block_2,hitbox=Vector2(400,12), size=Vector2(0,1), offset=Vector2(0,25),position=Vector2(60,225))
        self.block10 = Block(texture=Assets.tt_block_2,hitbox=Vector2(150,250), size=Vector2(0,1), offset=Vector2(0,0),position=Vector2(1080,240))
        self.block11 = Block(texture=Assets.tt_block_2,hitbox=Vector2(170,10), size=Vector2(0,1), offset=Vector2(0,10),position=Vector2(920,240))
        self.block12 = Block(texture=Assets.tt_block_2,hitbox=Vector2(40,95), size=Vector2(0,1), offset=Vector2(0,10),position=Vector2(1173,440))
        self.block13 = Block(texture=Assets.tt_block_2,hitbox=Vector2(43,100), size=Vector2(0,1), offset=Vector2(0,10),position=Vector2(100,195))
        self.block14 = Block(texture=Assets.tt_block_2,hitbox=Vector2(550,100), size=Vector2(0,1), offset=Vector2(0,25),position=Vector2(300,703))



        self.tree1 = Block(texture=Assets.tt_plant_1,hitbox=Vector2(25,25),size=Vector2(240,343),offset=Vector2(105,320),position=Vector2(160,20))
        self.tree2 = Block(texture=Assets.tt_plant_0,hitbox=Vector2(25,25),size=Vector2(290,350),offset = Vector2(130,330), position=Vector2(905,200))
        self.stone1 = Block(texture=Assets.tt_stone_9,hitbox=Vector2(150,75),size=Vector2(150,120),offset=Vector2(0,45),position=Vector2(490,570))
        self.stone2 = Block(texture=Assets.tt_headstone_6,hitbox=Vector2(75,70),size=Vector2(80,115),offset=Vector2(0,45),position=Vector2(432,357))
        self.stone3 = Block(texture=Assets.tt_stone_2,hitbox=Vector2(75,45),size=Vector2(75,45),offset=Vector2(0,0),position=Vector2(685,601))
        self.stone4 = Block(texture=Assets.tt_stone_1,hitbox=Vector2(45,40),size=Vector2(45,40),offset=Vector2(0,0),position=Vector2(805,661))
        self.stone5 = Block(texture=Assets.tt_stone_3,hitbox=Vector2(65,50),size=Vector2(65,50),offset=Vector2(0,0),position=Vector2(975,601))

        self.bin1 = Block(texture=Assets.tt_bin_2,hitbox=Vector2(55,33),size=Vector2(58,88),offset=Vector2(0,55),position=Vector2(950,459))
        self.bin2 = Block(texture=Assets.tt_bin_1,hitbox=Vector2(65,65),size=Vector2(65,65),offset=Vector2(0,0),position=Vector2(850,375))


        self.wall1 = Block(texture=Assets.tt_block_2,hitbox=Vector2(160,155),size=Vector2(160,155),offset=Vector2(0,0),position=Vector2(460,253))
        self.wall2 = Block(texture=Assets.tt_block_2,hitbox=Vector2(160,155),size=Vector2(160,155),offset=Vector2(0,0),position=Vector2(770,253))
        self.wall3 = Block(texture=Assets.tt_block_2,hitbox=Vector2(13,227),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(620,253))
        self.wall4 = Block(texture=Assets.tt_block_2,hitbox=Vector2(13,227),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(757,253))
        self.wall5 = Block(texture=Assets.tt_block_2,hitbox=Vector2(15,230),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(460,30))
        self.wall6 = Block(texture=Assets.tt_block_2,hitbox=Vector2(15,230),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(923,30))
        self.wall7 = Block(texture=Assets.tt_block_2,hitbox=Vector2(90,90),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(460,10))
        self.wall8 = Block(texture=Assets.tt_block_2,hitbox=Vector2(90,90),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(845,10))
        self.wall9 = Block(texture=Assets.tt_block_2,hitbox=Vector2(330,15),size=Vector2(13,227),offset=Vector2(0,0),position=Vector2(545,7))
        
        
        self.glass1 = Block(texture=Assets.tt_plant_4,hitbox=Vector2(0,1),size=Vector2(80,80),offset=Vector2(0,69),position=Vector2(467,80))
        self.glass2 = Block(texture=Assets.tt_plant_3,hitbox=Vector2(0,1),size=Vector2(60,50),offset=Vector2(0,25),position=Vector2(575,2))
        self.glass3 = Block(texture=Assets.tt_plant_6,hitbox=Vector2(0,1),size=Vector2(110,105),offset=Vector2(95,85),position=Vector2(819,154))
        self.glass4 = Block(texture=Assets.tt_block_5,hitbox=Vector2(0,1), size=Vector2(60,75), offset=Vector2(60,55),position=Vector2(401,238))
        
        self.monster_1 = Monster(position=Vector2(819, 154), follower=self.player)
        self.monster_2 = Monster(position=Vector2(467, 80), follower=self.player)
        self.monster_3 = Monster(position=Vector2(500, 400), follower=self.player)
        self.monster_4 = Monster(position=Vector2(800, 400), follower=self.player)
        self.monster_5 = Monster(position=Vector2(865, 650), follower=self.player)
        self.monster_6 = Monster(position=Vector2(1050, 600), follower=self.player)


        self.pos_1 = CollisionBox(position=Vector2(680,50), value=1)
        self.pos_2 = CollisionBox(position=Vector2(680 + 85,115), value=2)
        self.pos_3 = CollisionBox(position=Vector2(680,180), value=3)
        self.pos_4 = CollisionBox(position=Vector2(680 - 85,115), value=4)

        self.entity_group.add(self.circle_struct)   
        self.entity_group.add(self.monster_1)
        self.entity_group.add(self.monster_2)
        self.entity_group.add(self.monster_3)
        self.entity_group.add(self.monster_4)
        self.entity_group.add(self.monster_5)
        self.entity_group.add(self.monster_6)
        self.entity_group.add(self.player)
        self.entity_group.add(self.wall1)
        self.entity_group.add(self.block1)
        self.entity_group.add(self.block2)
        self.entity_group.add(self.block14)
        self.entity_group.add(self.block3)
        self.entity_group.add(self.block4)
        self.entity_group.add(self.block5)
        self.entity_group.add(self.block6)
        self.entity_group.add(self.block7)
        self.entity_group.add(self.block8)
        self.entity_group.add(self.glass4)  
        self.entity_group.add(self.block10) 
        self.entity_group.add(self.block11)
        self.entity_group.add(self.block12)
        self.entity_group.add(self.block13)
        self.entity_group.add(self.tree1)
        self.entity_group.add(self.tree2)
        self.entity_group.add(self.stone1)
        self.entity_group.add(self.stone2)
        self.entity_group.add(self.stone3)
        self.entity_group.add(self.stone4)
        self.entity_group.add(self.stone5)
        self.entity_group.add(self.bin1)
        self.entity_group.add(self.bin2)
        self.entity_group.add(self.wall1)
        self.entity_group.add(self.wall2)
        self.entity_group.add(self.wall3)
        self.entity_group.add(self.wall4)
        self.entity_group.add(self.wall5)
        self.entity_group.add(self.wall6)
        self.entity_group.add(self.wall7)
        self.entity_group.add(self.wall8)
        self.entity_group.add(self.wall9)
        self.entity_group.add(self.glass1)
        self.entity_group.add(self.glass2)
        self.entity_group.add(self.glass3)
        self.entity_group.add(self.glass4)
        self.entity_group.add(self.pos_1)
        self.entity_group.add(self.pos_2)
        self.entity_group.add(self.pos_3)
        self.entity_group.add(self.pos_4)

    def __update__(self, event):
        super().__update__(event=event)
        self.message_group.__update__(event=event)

        if(self.player.hp <= 0):
            StateMachine.push(Loose())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                StateMachine.push(Pause())

            if(event.key == pygame.K_f):
                if(self.bin2 in self.player.collisions):
                    self.send_message(S().hint_message)
            
            if self.has_box and not self.box.is_active and self.player in self.box.collisions and event.key == pygame.K_f:
                self.box.change_state()
                self.has_key = True
                self.send_message(S().get_key)

        for collision in self.player.collisions:
            if(isinstance(collision, CollisionBox)):
                if(collision.value not in self.circle_struct.positions):
                    self.circle_struct.positions.append(collision.value)
                    self.send_message(self.circle_struct.positions.__str__())

        if self.player.position.x > 1200 or self.player.position.y > 800:
            if(self.has_key):
                StateMachine.push(Win())
            self.__init_state__()

        if self.circle_struct.is_active and not self.has_box:
            self.has_box = True
            self.box = Box()
            self.entity_group.add(self.box)
            
    def __render__(self, display):
        super().__render__(display=display)
        self.message_group.__render__(display=display)
    
    def send_message(self, message: str):
        self.datas.append(message)
        if(len(self.datas) > 5):
            self.datas.pop(0)
        
        self.message_group.widgets.clear()
        for i in range(len(self.datas)):
            self.message_group.add(Text(text=self.datas[i], position=Vector2(1000, 0 + i * 17), size=Vector2(100, 100), color=(255, 255, 255), font_size=15))