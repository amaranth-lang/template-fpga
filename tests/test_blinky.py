from amaranth.sim import Simulator

from amaranth_template_fpga.blinky import Blinky


def test_blinky_frequency():
    blinky = Blinky(frequency=10)

    def testbench():
        for _ in range(5):
            assert (yield blinky.led) == 0
            yield
        for _ in range(5):
            assert (yield blinky.led) == 1
            yield
        assert (yield blinky.led) == 0

    sim = Simulator(blinky)
    sim.add_clock(period=1e-2)
    sim.add_sync_process(testbench)
    sim.run()
