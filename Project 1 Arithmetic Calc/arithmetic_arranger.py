def arithmetic_arranger(problems, ans=False):
  n_problems = len(problems)
  if (n_problems > 5):
    return "Error: Too many problems."
  j = 1
  operator = []
  operand_1 = []
  operand_2 = []
  max_len = []
  for problem in problems:
    problem = problem.replace(" ", "")
    i = problem.find("+")
    if (i == -1):
      i = problem.find("-")
      if (i == -1):
        return "Error: Operator must be '+' or '-'."
      problem = problem.split('-')
      operator.append('-')
    else: 
      problem = problem.split('+')
      operator.append('+')

    if len(problem[0]) > 4 or len(problem[1]) > 4:
      return "Error: Numbers cannot be more than four digits."
    max_len.append(max(len(problem[0]), len(problem[1])) + 2)
    try:
      problem[0] = int(problem[0])
      problem[1] = int(problem[1])
    except ValueError:
      return "Error: Numbers must only contain digits."
    operand_1.append(problem[0])
    operand_2.append(problem[1])
    j += 1

  i = 0
  while i < 5:
    i += 1

  i=0
  line1 = ""
  line2 = ""
  line3 = ""
  while i < n_problems:
    offset = max_len[i] - len(str(operand_1[i]))
    line1 += offset * " " + str(operand_1[i]) + "    "
    offset = max_len[i] - (1+len(str(operand_2[i])))
    line2 += str(operator[i]) + (offset * " ") + str(operand_2[i]) + "    "
    line3 += max_len[i] * "-" + "    " 
    i += 1
  arranged = line1.rstrip()+"\n"+line2.rstrip()+"\n"+line3.rstrip()
  if ans:
    i = 0
    soln = []
    line4 = ""
    while i < n_problems:
      if operator[i] == "+":
        soln.append(operand_1[i] + operand_2[i])
      elif operator[i] == "-":
        soln.append(operand_1[i] - operand_2[i])
      offset = max_len[i] - len(str(soln[i]))
      line4 += (offset * " ") + str(soln[i]) + "    "
      i += 1
    arranged=line1.rstrip()+"\n"+line2.rstrip()+"\n"+line3.rstrip()+"\n"+line4.rstrip()
  return arranged
