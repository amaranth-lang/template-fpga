from amaranth import *
from amaranth_boards.icestick import ICEStickPlatform
from amaranth_boards.versa_ecp5 import VersaECP5Platform
from amaranth_boards.tang_nano import TangNanoPlatform


class Blinky(Elaboratable):
    def elaborate(self, platform):
        m = Module()

        led = platform.request("led", 0).o
        timer = Signal(range(int(platform.default_clk_frequency//2)),
                       reset=int(platform.default_clk_frequency//2) - 1)
        with m.If(timer == 0):
            m.d.sync += led.eq(~led)
            m.d.sync += timer.eq(timer.reset)
        with m.Else():
            m.d.sync += timer.eq(timer - 1)

        return m


def build_ice40():
    ICEStickPlatform().build(Blinky())


def build_ecp5():
    VersaECP5Platform().build(Blinky())


def build_gowin():
    TangNanoPlatform().build(Blinky())
