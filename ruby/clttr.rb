#!/usr/bin/env ruby
# I think this was an "exercise" from somewhere.
# It's just using input + get to ask a question
# and return a message if interest is high.

def cover_message()
  puts "
Denta samtempe us sep, iom i tempo senforte postpostmorgaŭ. Ed fore frikativo mia, et tio verba intere. Nk fin kombi minusklo, peto pleje kaŭze ad dio. Ina tiama retro supreniro ko, dz oficiala frazmelodio cis.
  "
end

carrot = '> '
puts "Is interest high or low? (high or low) ", carrot
interest = gets 
interest = interest.chomp.downcase

interest == "high" ? cover_message() : abort("Sorry")
