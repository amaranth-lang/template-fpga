from amaranth import *

from amaranth_boards.icestick import ICEStickPlatform
from amaranth_boards.versa_ecp5 import VersaECP5Platform
from amaranth_boards.tang_nano import TangNanoPlatform

from .blinky import Blinky


class Toplevel(Elaboratable):
    def elaborate(self, platform):
        m = Module()

        m.submodules.blinky = blinky = Blinky(frequency=platform.default_clk_frequency)
        m.d.comb += platform.request("led", 0).o.eq(blinky.led)

        return m


def build_ice40():
    ICEStickPlatform().build(Toplevel())


def build_ecp5():
    VersaECP5Platform().build(Toplevel())


def build_gowin():
    TangNanoPlatform().build(Toplevel())
