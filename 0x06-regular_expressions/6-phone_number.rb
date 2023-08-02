#!/usr/bin/env ruby
#The regular expression must match a 10 digit phone numbe

puts ARGV[0].scan(/^[0-9]{3}-?[0-9]{3}-?[0-9]{4}$/).join
