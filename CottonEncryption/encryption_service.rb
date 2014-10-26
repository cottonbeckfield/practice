#!/usr/bin/env ruby

require_relative "encryptor.rb"
require_relative "decryptor.rb"

e = Cotton::Encryptor.new("testkey")
encrypted = e.encrypt("message")

decrypted = Cotton::Decryptor.decrypt_message_with_key(encrypted,"testkey")
p decrypted

