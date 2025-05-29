import math
import time

import engine
from engine.events import *
from engine.operators import *
from engine.types import *


@sprite('Stage')
class Stage(Target):
    """Sprite Stage"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "None", [
            {
                'name': "backdrop1",
                'path': "cd21514d0531fdffb22204e0ec5ed84a.svg",
                'center': (240, 180),
                'scale': 2
            }
        ])

        self.sprite.layer = 0


@sprite('Video')
class SpriteVideo(Target):
    """Sprite Video"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 36
        self._ypos = 28
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sprite.layer = 1

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        pass

    @on_broadcast('stop')
    async def broadcast_Stop(self, util):
        pass


@sprite('Play')
class SpritePlay(Target):
    """Sprite Play"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -173
        self._ypos = 140
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "c865a06960cf7a019ed83d17b52c2332.svg",
                'center': (54, 22),
                'scale': 1
            }
        ])

        self.sprite.layer = 2

    @on_green_flag
    async def green_flag(self, util):
        self.shown = True

    @on_clicked
    async def sprite_clicked(self, util):
        util.send_broadcast("Start")


@sprite('Stop')
class SpriteStop(Target):
    """Sprite Stop"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -57.87777729826233
        self._ypos = 140.51433116454695
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "a037a07b938092fa03a09bb6d87a2716.svg",
                'center': (54, 22),
                'scale': 1
            }
        ])

        self.sprite.layer = 3

    @on_green_flag
    async def green_flag(self, util):
        self.shown = True

    @on_clicked
    async def sprite_clicked(self, util):
        util.send_broadcast("Stop")


@sprite('DVR')
class SpriteDVR(Target):
    """Sprite DVR"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 51
        self._ypos = 139
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "6b25ddc8a683c194cbd528db0c0a32a7.svg",
                'center': (48, 21),
                'scale': 1
            }
        ])

        self.list_Console = List(
            ["Info : Started vvideo recording"]
        )

        self.sprite.layer = 4

    @on_broadcast('close console')
    async def broadcast_closeconsole(self, util):
        self.list_Console.hide()

    @on_green_flag
    async def green_flag(self, util):
        self.list_Console.hide()

    @on_broadcast('open console')
    async def broadcast_OpenConsole(self, util):
        self.list_Console.show()

    @on_clicked
    async def sprite_clicked(self, util):
        util.send_broadcast("Open Console")

    @on_broadcast('stop')
    async def broadcast_Stop(self, util):
        self.list_Console.append("Info : Stop video")

    @on_broadcast('start')
    async def broadcast_Start(self, util):
        self.list_Console.append("Info : Started video recording")

    @on_green_flag
    async def green_flag1(self, util):
        self.list_Console.delete_all()


@sprite('Sprite1')
class Sprite1(Target):
    """Sprite Sprite1"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 150
        self._ypos = 86
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "0e03a96db5610c18ab84a6bd5afac7ca.svg",
                'center': (11, 23),
                'scale': 1
            }
        ])

        self.sprite.layer = 5

    @on_clicked
    async def sprite_clicked(self, util):
        self.shown = False
        util.send_broadcast("Close Console")

    @on_broadcast('open console')
    async def broadcast_OpenConsole(self, util):
        self.shown = True

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False


if __name__ == '__main__':
    engine.start_program()
