#!/usr/bin/env ruby

require_relative "splitter.rb"

module Cotton
  class Decryptor
    def self.decrypt_message_with_key encrypted_message, key
      split_encrypted_msg = Cotton::MessageSplitter.make_ascii_array encrypted_message
      split_key = Cotton::MessageSplitter.make_ascii_array key 

      decrypted_message = []
      split_encrypted_msg.each_with_index { |x, i| 
        key_digit = split_key[i]
        decrypted_message << (x^key_digit).chr
      }
      decrypted_message.join
    end
  end
end
