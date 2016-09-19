#!/usr/bin/env ruby
# This is my simple ruby logger module.

require 'logger'

module Logging

  def self.logger
    @logger ||= Logger.new($stdout)
  end

  def logger
    Logging.logger
  end

end # End Module Logger
