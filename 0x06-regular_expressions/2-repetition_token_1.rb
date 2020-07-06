#!/usr/bin/env ruby
regex = /h.t{0,1}n/
input = ARGV[0]

puts input.scan(regex).join
