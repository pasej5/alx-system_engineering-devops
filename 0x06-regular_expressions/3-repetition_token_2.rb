#!/usr/bin/env ruby
#Ruby script that accepts one argument and pass it to a regex
#Method

puts ARGV[0].scan(/hbt{1,}n/).join
