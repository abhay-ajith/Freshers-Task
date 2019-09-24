#!/usr/bin/ruby -w
require 'nokogiri'
require 'open-uri'
require 'pry'

document= Nokogiri::HTML(open("https://www.google.com/search?q=linux"))
nd=document.xpath("//a")
nd.each do |nd|
puts nd.text
end