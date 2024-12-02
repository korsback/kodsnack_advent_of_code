#!/usr/bin/env ruby

require 'bundler/inline'

gemfile do
  source 'https://rubygems.org'
  gem 'debug'
  gem 'fiddle'
end

def solve(line)
  line
end

def parse_line(line)
  line.scan(/\d+/).map(&:to_i)
end

def solve_line(line)
  line.sum
end

File.readlines(ARGV[0]).map(&:strip)
    .map { |line| parse_line(line) }
    .transpose
    .map(&:sort)
    .transpose
    .map { |(a, b)| (a.abs - b.abs).abs }
    .sum
    .then(&method(:puts))
