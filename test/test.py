# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

 # Set the clock period to 100 ns (10 MHz)
    clock = Clock(dut.clk, 100, units="ns")
    cocotb.start_soon(clock.start())
 
    await ClockCycles(dut.clk, 4) # show startup X state in VCD
    dut.clk.value = 0
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 4) # show propagation of quiescent inputs in VCD
 
 # reset
    dut._log.info("reset")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 1000)
    await Timer(200, units="ns")

    dut.rst_n.value = 1

    dut.ui_in <= 0b00
    await ClockCycles(dut.clk, 1500)

    dut.ui_in <= 0b01
    await ClockCycles(dut.clk, 3000)

    dut.ui_in <= 0b10
    await ClockCycles(dut.clk, 3000)

    dut.ui_in <= 0b11
    await ClockCycles(dut.clk, 750)

    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 250)

    dut.rst_n.value = 1

    dut.ui_in <= 0b11
    await ClockCycles(dut.clk, 2000)

    dut.ui_in <= 0b00
    await ClockCycles(dut.clk, 500)
