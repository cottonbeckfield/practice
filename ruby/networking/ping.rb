#!/usr/bin/env ruby
#
# ICMP -> Internet Control Message Protocol
# A TCP/IP network layer protocol that reports errors and provides
# other information relevant to IP pcaket processing.
#
# UDP -> User Datagram PRotocol
# A connectionless transport layer protocol in the TCP/IP stack.
# Exchanges datagrams without acknowledgement or guaranteed delivery.
#
# TCP -> Transmission Control protocol
# Provides reliable, ordered, and error-checked delivery of a stream
# of octets between application running on hosts communicating on an
# IP network.
#
require 'net/ping'
include Net
require 'ipaddress'

# Checks to make sure the user provided a valid IP Address.
# Uses the ipaddress gem.
def ip_check(ip)

  IPAddress.valid?(ip) == true ? ip_information(ip) && do_the_pings(ip) : abort("false")

end

# Displays some basic information about the IP Address provided.
def ip_information(ip)

  info = IPAddress(ip)
  puts "Address : #{info.address}"
  puts "Prefix  : #{info.prefix}"
  puts "Netmask : #{info.netmask}"
  puts "Octets  : #{info.octets}"

end

# Asks a user to put in an IP Address.
def user_input

  puts "What IP would you like to ping? "
  user_response = gets

  ip_check(user_response)

end

# Ping, ping, ping, ping, ping--errbody!
def do_the_pings(ip)

  # Check if a Host is up
  ping_check = Ping::External.new(ip)
  if ping_check.ping? == true
    puts "The host is available."
  else
    puts "The host is unavailable."
  end

end

user_input()
