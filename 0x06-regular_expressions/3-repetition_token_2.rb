#!/usr/bin/env ruby
regex = /hbt{1,}n/
input = ARGV[0]

puts input.scan(regex).join
