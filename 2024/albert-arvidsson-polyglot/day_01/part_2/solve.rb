#!/usr/bin/env ruby

require 'bundler/inline'

gemfile do
  source 'https://rubygems.org'
  gem 'debug'
  gem 'fiddle'
end

def solve(line) = line

def parse_line(line) = line.scan(/\d+/).map(&:to_i)

def solve_columns((one, two))
  one.zip(one.map { |n| two.count { |m| m == n } }).map { |(o, t)| o * t }
end

File.readlines(ARGV[0]).map(&:strip)
    .map { |line| parse_line(line) }
    .transpose
    .then(&method(:solve_columns))
    .sum
    .then(&method(:pp))
