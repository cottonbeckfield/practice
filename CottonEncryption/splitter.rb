#!/usr/bin/env

module Cotton
  class MessageSplitter
    def self.make_ascii_array message
      message.split(//).map(&:ord)
    end
  end
end
