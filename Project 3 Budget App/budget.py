class Category:
  balance = 0.00
  cat = ""
  def __init__(self, budget_category):
    self.cat = budget_category
    self.ledger = []

  def deposit(self, amount, description=""):
    (self.ledger).append({"amount": amount, "description":description})
    self.balance += amount

  def withdraw(self, amount, description=""):
    if (self.check_funds(amount) == False):
      return(False)
    else:
      self.ledger.append({"amount": -1 * amount, "description":description})
      self.balance -= amount
      return(True)
  
  def get_balance(self):
    return(self.balance)

  def transfer(self, amount, dest_cat):
    if(self.check_funds(amount) == True):
      self.withdraw(amount, "Transfer to "+dest_cat.cat)
      dest_cat.deposit(amount, "Transfer from "+self.cat)
      return(True)
    else:
      return(False)
  
  def check_funds(self, amount):
    if(amount > self.balance):
      return(False)
    else:
      return(True)

  def __str__(self):
    length = len(self.cat)
    num_stars = (int)((30-length)/2)
    title = "*"*num_stars+self.cat+"*"*num_stars+"\n"
    content = ""
    for item in self.ledger:
      cont_desc = item["description"][:23]
      pad_len = 30 - len(cont_desc)
      cont_amount = "{:.2f}".format(item["amount"])[:7].rjust(pad_len, " ")
      content = content+(cont_desc+cont_amount+"\n")
    total = "Total: "+ str(self.balance)

    category_display = title+content+total
    return(category_display)
    
    
def create_spend_chart(categories):
  title = "Percentage spent by category\n"
  chart_area = ""
  xlabels = ""
  totals = []
  total = 0
  tot_expenditure = 0
  names = []
  name_lens = []
  for category in categories:
    names.append(category.cat)
    name_lens.append(len(category.cat))
    for item in category.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    tot_expenditure += total
    totals.append(total)
    total = 0
  bars = []
  for amount in totals:
    percent = (amount / tot_expenditure)*100
    percent = (int) (percent - (percent%10))
    bars.append(percent)
  for ylabel in range(100, -10, -10):
    yaxis = (str(ylabel)+"|").rjust(4, " ")
    data = ""
    for amount in bars:
      if amount >= ylabel:
        data = data + " o "
      else:
        data = data + "   "
    chart_area = chart_area+(yaxis+data)+" \n"

  bottom_axis=("    "+len(categories)*"---"+"-\n")
  #print("100|")
  #print(bottom_axis)
  row = 0
  for i in names:
    row = max(row, len(i))
  col = len(names)
  ans = ["" for i in range(row)]
  j = 0
  for i in range(col):
    j = 0
    while j < len(names[i]):
      while i - len(ans[j]) >= 1:
        ans[j] += " "
      ans[j] += names[i][j]
      j += 1
  for row in ans:
    i=0
    label = "    "
    while i < len(row):
      label = label + " "+row[i]+" "
      i += 1
    xlabels = xlabels + label + " \n"
  bar_chart = title+chart_area+bottom_axis+xlabels[:-2]+" "
  return (bar_chart)
