from ...game.entity.entity import *


class EntityGroup:
    '''
    EntityGroup is a group of entities.
    entities: list - the list of entities
    '''
    def __init__(self):
        self.sort_by_possition = True
        self.entities = []
    
    def add(self, entity: Entity):
        self.entities.append(entity)
    
    def remove(self, entity: Entity):
        self.entities.remove(entity)
    
    def __render__(self, display):
        for entity in self.entities:
            entity.__render__(display)
    def __update__(self, event):
        if(self.sort_by_possition):
            self.entities.sort(key=lambda entity: entity.rect.y)
        
        for entity in self.entities:
            collision_list = []
            for other_entity in self.entities:
                if(entity == other_entity):
                    continue
                if(entity.rect.colliderect(other_entity.rect)):
                    collision_list.append(other_entity)
            entity.__on_collision__(collision_list)
            entity.__update__(event)