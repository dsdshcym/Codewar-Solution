def isValidWalk(walk)
  walk.count('w') == walk.count('e') and
  walk.count('s') == walk.count('n') and
  walk.length == 10
end
