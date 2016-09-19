#!/usr/bin/env ruby
# Creates a SSH connection and runs a command on a supplied host
# with some basic rescue logic.
require 'net/ssh'
include Net

# Connect to a provided host and issue a command.
def ssh_connection(host)

  begin
    SSH.start(host) do |session|
      run_cmd = 'ls -lah'
      response = session.exec!(run_cmd)
      puts response
      session.close
    end
  rescue Exception => e
    abort "Exception: " + e.message
  end

end #ssh_connection

# Asks a user to put in a host or IP Address.
def user_input

  puts "What hostname/IP would you like to ping? "
  user_response = gets.chomp.downcase

  ssh_connection(user_response)
end

user_input()
