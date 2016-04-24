def createPhoneNumber(numbers)
  "(%d%d%d) %d%d%d-%d%d%d%d" % numbers
end

createPhoneNumber(Array(0..9))
