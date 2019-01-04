#!/usr/bin/env ruby

require 'net/smtp'

RECEPIENTS=['vyncem@gmail.com', 'offering.europe@ishafoundation.org', 'shaktijaiswal13@gmail.com']

message = <<MESSAGE_END
From: Automation  <automation@achillesmail.com>
To: Isha Offering <offering.europe@ishafoundation.org>
MIME-Version: 1.0
Content-type: text/html
Subject: Offering Automation report

MESSAGE_END

File.open("#{ENV['FREE_OFFERING_WORKSPACE']}/.email", "r") do |f|
  f.each_line do |line|
    message << line
  end
end
Net::SMTP.start('localhost') do |smtp|
   smtp.send_message message, 'automation@achillesmail.com', RECEPIENTS
end
