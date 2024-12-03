#!/usr/bin/env ruby

def solve(enabled: true)
  lambda do |(match, one, two)|
    enabled = match.start_with? 'do(' if match.start_with? 'do'
    enabled && match.start_with?('mul(') ? one.to_i * two.to_i : 0
  end
end

File.read(ARGV[0])
    .scan(/(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))/)
    .sum(&solve)
    .then(&method(:pp))
