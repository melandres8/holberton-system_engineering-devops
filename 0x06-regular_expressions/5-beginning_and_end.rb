#!/usr/bin/env ruby
regex = /^h\wn$/
input = ARGV[0]

puts input.scan(regex).join
