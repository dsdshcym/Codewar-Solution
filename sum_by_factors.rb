require 'prime'

def sumOfDivided(lst)
  ans = []
  Prime.each(lst.map(&:abs).max) do |prime|
    temp = lst.select { |x| x % prime == 0 }
    if not temp.empty?
      ans << [prime, temp.reduce(:+)]
    end
  end
  ans
end

p sumOfDivided( [15, 30, -45] )
