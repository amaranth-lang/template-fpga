from amaranth.sim import Simulator

from amaranth_template_fpga.blinky import Blinky


def test_blinky_frequency():
    blinky = Blinky(frequency=10)

    async def testbench(ctx):
        for _ in range(5):
            assert ctx.get(blinky.led) == 0
            await ctx.tick()
        for _ in range(5):
            assert ctx.get(blinky.led) == 1
            await ctx.tick()
        assert ctx.get(blinky.led) == 0

    sim = Simulator(blinky)
    sim.add_clock(period=1e-2)
    sim.add_testbench(testbench)
    sim.run()
