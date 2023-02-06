############################################################
## This file is generated automatically by Vitis HLS.
## Please DO NOT edit it.
## Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
############################################################
open_project ai_hls
set_top nn_inference
add_files matmul.cpp
add_files matmul.hpp
add_files -tb matmul_tb.cpp
open_solution "solution_ai" -flow_target vivado
set_part {xczu3eg-sbva484-1-i}
create_clock -period 10 -name default
config_export -format ip_catalog -output /home/jacob/workspace/embedded/FinalAssignment/hls/nn_inference.zip -rtl vhdl
#source "./ai_hls/solution_ai/directives.tcl"
csim_design
csynth_design
cosim_design
export_design -rtl vhdl -format ip_catalog -output /home/jacob/workspace/embedded/FinalAssignment/src/nn_inference.zip
