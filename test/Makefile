# Makefile
# See https://docs.cocotb.org/en/stable/quickstart.html for more info

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog
SRC_DIR = $(PWD)/../src
PROJECT_SOURCES = tt_um_joerdsonsilva_modem.v
PROJECT_SOURCES += modem.v
PROJECT_SOURCES += bask.v
PROJECT_SOURCES += mult1.v
PROJECT_SOURCES += clk_rdg1.v
PROJECT_SOURCES += rdg1.v
PROJECT_SOURCES += ffd1.v
PROJECT_SOURCES += wave11.v
PROJECT_SOURCES += bfsk.v
PROJECT_SOURCES += clk_rdg2.v
PROJECT_SOURCES += clk_25MHz.v
PROJECT_SOURCES += wave12.v
PROJECT_SOURCES += wave22.v
PROJECT_SOURCES += rdg2.v
PROJECT_SOURCES += ffd2.v
PROJECT_SOURCES += freq_select.v
PROJECT_SOURCES += bpsk.v
PROJECT_SOURCES += clk_rdg3.v
PROJECT_SOURCES += rdg3.v
PROJECT_SOURCES += ffd3.v
PROJECT_SOURCES += wave13.v
PROJECT_SOURCES += wave23.v
PROJECT_SOURCES += control_0.v
PROJECT_SOURCES += demod_bask.v
PROJECT_SOURCES += demod_bfsk.v
PROJECT_SOURCES += wave122.v
PROJECT_SOURCES += mult2.v
PROJECT_SOURCES += integrator2.v
PROJECT_SOURCES += demod_bpsk.v
PROJECT_SOURCES += wave133.v
PROJECT_SOURCES += mult3.v
PROJECT_SOURCES += integrator3.v
PROJECT_SOURCES += control_1.v

ifneq ($(GATES),yes)

# RTL simulation:
SIM_BUILD				= sim_build/rtl
VERILOG_SOURCES += $(addprefix $(SRC_DIR)/,$(PROJECT_SOURCES))

else

# Gate level simulation:
SIM_BUILD				= sim_build/gl
COMPILE_ARGS    += -DGL_TEST
COMPILE_ARGS    += -DFUNCTIONAL
COMPILE_ARGS    += -DUSE_POWER_PINS
COMPILE_ARGS    += -DSIM
COMPILE_ARGS    += -DUNIT_DELAY=\#1
VERILOG_SOURCES += $(PDK_ROOT)/sky130A/libs.ref/sky130_fd_sc_hd/verilog/primitives.v
VERILOG_SOURCES += $(PDK_ROOT)/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v

# this gets copied in by the GDS action workflow
VERILOG_SOURCES += $(PWD)/gate_level_netlist.v

endif

# Allow sharing configuration between design and testbench via `include`:
COMPILE_ARGS 		+= -I$(SRC_DIR)

# Include the testbench sources:
VERILOG_SOURCES += $(PWD)/tb.v
TOPLEVEL = tb

# MODULE is the basename of the Python test file
MODULE = test

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
