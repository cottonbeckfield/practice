#!/usr/bin/env ruby

require_relative "splitter.rb"

module Cotton
  class Encryptor
    def initialize encryption_key
      @encryption_key = encryption_key  
    end

    def encrypt message
      msg_array = MessageSplitter.make_ascii_array message
      key_array = MessageSplitter.make_ascii_array @encryption_key
      encrypted = []
      msg_array.each_with_index { |c, i|
        xored_value = c^key_array[i]
        encrypted << xored_value.chr
      }
      encrypted.join
    end 
  end
end
