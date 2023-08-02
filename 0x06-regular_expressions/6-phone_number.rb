#!/usr/bin/env ruby
#The regular expression must match a 10 digit phone numbe

puts ARGV[0].scan(^\d{3}-\d{3}-\d{4}).join
