#!/usr/bin/env ruby
regex = /hbt{0,4}n/
input = ARGV[0]

puts input.scan(regex).join
