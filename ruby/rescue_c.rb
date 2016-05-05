#!/usr/bin/env ruby
# Repo: Practice
#
# This is a simple snippet for handling
# the ^C interrupt when using readline.
#

require 'readline'

# Function to parse user Input. Keepin' it pretty.
def input(prompt=" ", newline=false)

  stty_save = `stty -g`.chomp
  prompt += "\n" if newline

  # If user escapes with ^C, exit kindly.
  begin
    Readline.readline(prompt, true).squeeze(" ").strip
  rescue Interrupt => e
    system('stty', stty_save)
  end

end

def process()

  user_response = input "Type 'yes' or ^C to test > "

  if user_response == "yes"
    abort "Good job. You typed 'yes'."
  else
    puts "\n"
    abort "You chose to exit. BYEEEE~"
  end

end

process()
