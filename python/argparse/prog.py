# -*- coding:utf-8 -*-
import argparse

parser = argparse.ArgumentParser()

#square 是必填参数
parser.add_argument("square", help="display a square of a given number", type=int)
#verbose 是可选参数, -v 是短选项
#action = store_true 表示该参数可以不带值
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()

if args.verbose:
	print "verbosity turned on"
