#!/usr/bin/env ruby

entry = ARGV[0]

sender = entry.match(/\[from:(.*?)\]/)[1]
receiver = entry.match(/\[to:(.*?)\]/)[1]
flags = entry.match(/\[flags:(.*?)\]/)[1]

puts "#{sender},#{receiver},#{flags}"
