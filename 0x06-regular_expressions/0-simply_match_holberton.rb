#!/usr/bin/env ruby
regex = /Holberton/   # Regular expression
input = ARGV[0] # Input string

puts input.scan(regex).join
