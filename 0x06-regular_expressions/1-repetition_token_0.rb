#!/usr/bin/env ruby
regex = /hbt{2,5}n/
input = ARGV[0]

puts input.scan(regex).join
