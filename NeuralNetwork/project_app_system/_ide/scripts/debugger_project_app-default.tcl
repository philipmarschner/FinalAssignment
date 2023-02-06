# Usage with Vitis IDE:
# In Vitis IDE create a Single Application Debug launch configuration,
# change the debug type to 'Attach to running target' and provide this 
# tcl script in 'Execute Script' option.
# Path of this script: /home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork/project_app_system/_ide/scripts/debugger_project_app-default.tcl
# 
# 
# Usage with xsct:
# To debug using xsct, launch xsct and run below command
# source /home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork/project_app_system/_ide/scripts/debugger_project_app-default.tcl
# 
connect -url tcp:127.0.0.1:3121
source /tools/Xilinx/Vitis/2020.2/scripts/vitis/util/zynqmp_utils.tcl
targets -set -nocase -filter {name =~"APU*"}
rst -system
after 3000
targets -set -filter {jtag_cable_name =~ "Avnet USB-to-JTAG/UART Pod V1 1234-oj1A" && level==0 && jtag_device_ctx=="jsn-USB-to-JTAG/UART Pod V1-1234-oj1A-14710093-0"}
fpga -file /home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork/project_app/_ide/bitstream/u96v2_sbc_mp4d_wrapper.bit
targets -set -nocase -filter {name =~"APU*"}
loadhw -hw /home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork/example_plz_work/export/example_plz_work/hw/example_plz_work.xsa -mem-ranges [list {0x80000000 0xbfffffff} {0x400000000 0x5ffffffff} {0x1000000000 0x7fffffffff}] -regs
configparams force-mem-access 1
targets -set -nocase -filter {name =~"APU*"}
set mode [expr [mrd -value 0xFF5E0200] & 0xf]
targets -set -nocase -filter {name =~ "*A53*#0"}
rst -processor
dow /home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork/example_plz_work/export/example_plz_work/sw/example_plz_work/boot/fsbl.elf
set bp_6_58_fsbl_bp [bpadd -addr &XFsbl_Exit]
con -block -timeout 60
bpremove $bp_6_58_fsbl_bp
targets -set -nocase -filter {name =~ "*A53*#0"}
rst -processor
dow /home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork/project_app/Debug/project_app.elf
configparams force-mem-access 0
targets -set -nocase -filter {name =~ "*A53*#0"}
con
