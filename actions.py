from __future__ import annotations

from typing import TYPE_CHECKING

from tcod import desaturated_yellow

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        '''Perform this action with the objects needed to determine its scope.

        `Engine` is the scope this action is being performed in.

        `Entity` is the object performing the action.

        This method must be overriden by Acion subclasses.
        '''

class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

class ActionWithDirection(Action):
    def __init__(self, dx: int, dy: int) -> None:
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()

class MeleeAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if not target:
            return # No entity to attack.
        
        print(f"You kick the {target.name}, much to its annoyance!")

class MovementAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x  = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return # Destination out of bounds.
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return # Destination is blocked by a tiles.
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return # Destination is blocked by an entity.

        entity.move(self.dx, self.dy)

class BumpAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return MeleeAction(self.dx, self.dy).perform(engine, entity)

        else:
            return MovementAction(self.dx, self.dy).perform(engine, entity)