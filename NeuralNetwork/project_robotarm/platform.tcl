# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct /home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork/project_robotarm/platform.tcl
# 
# OR launch xsct and run below command.
# source /home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork/project_robotarm/platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {project_robotarm}\
-hw {/home/jacob/workspace/embedded/FinalAssignment/hdl/projects/u96v2_sbc_mp4d_2020_2/u96v2_sbc_mp4d_wrapper.xsa}\
-proc {psu_cortexa53_0} -os {standalone} -arch {64-bit} -fsbl-target {psu_cortexa53_0} -out {/home/jacob/workspace/embedded/FinalAssignment/NeuralNetwork}

platform write
platform generate -domains 
platform active {project_robotarm}
domain active {zynqmp_fsbl}
bsp reload
bsp reload
bsp reload
bsp config stdin "psu_uart_1"
bsp config stdout "psu_uart_1"
bsp write
bsp reload
catch {bsp regenerate}
bsp reload
domain active {zynqmp_pmufw}
bsp reload
bsp config stdin "psu_uart_1"
bsp config stdout "psu_uart_1"
bsp write
bsp reload
catch {bsp regenerate}
platform generate
platform active {project_robotarm}
