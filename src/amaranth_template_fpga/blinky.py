from amaranth import *
from amaranth.lib.wiring import Component, In, Out


class Blinky(Component):
    led: Out(1)

    def __init__(self, frequency):
        super().__init__()

        self.frequency = frequency

    def elaborate(self, platform):
        m = Module()

        timer = Signal(range(int(self.frequency//2)))
        with m.If(timer == int(self.frequency//2) - 1):
            m.d.sync += self.led.eq(~self.led)
            m.d.sync += timer.eq(0)
        with m.Else():
            m.d.sync += timer.eq(timer + 1)

        return m
