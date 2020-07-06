#!/usr/bin/env ruby
regex = /^\d{1,10}$/
input = ARGV[0]

puts input.scan(regex).join
