# -*- coding:utf-8 -*-
import argparse

parser = argparse.ArgumentParser()

#square 是必填参数
#type = int 表示输入的为 int
parser.add_argument("square", help="display a square of a given number", type=int)
#verbose 是可选参数, -v 是短选项
#action = store_true 表示该参数可以不带值
#action = count 会记录该参数出现多少次
#choice = [0, 1, 2] 表示输入只接受 0，1，2
parser.add_argument("-v", "--verbose", type=int, choices=[0, 1, 2], help="increase output verbosity")

args = parser.parse_args()

if args.verbose:
	print "verbosity turned on"
