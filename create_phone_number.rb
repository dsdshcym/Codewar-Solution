def createPhoneNumber(numbers)
  numbers = numbers.map(&:to_s).join
  return "(" + numbers[0..2] + ") " + numbers[3..5] + "-" + numbers[6..-1]
end

createPhoneNumber(Array(0..9))
