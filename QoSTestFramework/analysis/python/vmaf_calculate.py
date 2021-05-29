# Copyright (C) <2019> Intel Corporation
#
# SPDX-License-Identifier: Apache-2.0
import os
import os.path
import subprocess as sp


old_cwd = os.getcwd()
targ_cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(targ_cwd)

cmd = "/home/jack-ma/vmaf/python/vmaf/script/run_vmaf.py"
ref1 = "/home/jack-ma/webrtc_m76/src/vloud/qos_test/video_file/culture_640x380_1M.yuv"
ref2 = "/home/jack-ma/webrtc_m76/src/vloud/qos_test/QoSTestFramework/analysis/dataset/Data/LocalYUV.yuv"
fmt = "yuv420p"
width = "640"
height = "380"
out = "--out-fmt.json"

cmd_out = sp.check_output([cmd, fmt, width, height, ref1, ref2, out])
output = cmd_out.splitlines()

VMAF_score = []
f = open('../dataset/output/VMAF_score', 'w')
for frame in output:
    if frame[0:5] == "Frame":
        pos = frame.find("VMAF_score:")
        if pos != -1:
            print(frame[pos+11:].strip('\n'))
            f.write(frame[pos+11:].strip('\n'))
            f.write(',')
            VMAF_score.append(frame[pos+11:].strip('\n'))
f.close()

os.chdir(old_cwd)
