#!/usr/bin/env ruby
#Regular expression that starts with h and ends n

puts ARGV[0].scan(/^h.*?n$/).join
