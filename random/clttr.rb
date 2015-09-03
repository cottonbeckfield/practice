#!/usr/bin/env ruby

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
