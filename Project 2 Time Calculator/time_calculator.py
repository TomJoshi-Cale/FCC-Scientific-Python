def add_time(start, duration, start_day=None):
  flag = 0
  day=""
  day_num = 0
  week = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
  if start_day:
    day = start_day.capitalize()
    day_num = list(week.keys())[list(week.values()).index(day)]
    flag = 1

  duration = duration.split(":")
  dr_hour = duration[0]
  dr_min = duration[1]
  start = start.split(":")
  st_hour = start[0]
  start = start[1].split(" ")
  st_min = start[0]
  st_M = start[1]
  if st_M == "PM":
    st_hour = str(int(st_hour)+12)
  end_min = int(st_min) + int(dr_min)
  add_hrs = end_min // 60
  end_min = end_min % 60
  end_hr = int(st_hour) + int(dr_hour) + add_hrs
  days = end_hr // 24
  end_hr = end_hr%24
  if (flag == 1):
    day_num += days
    day_num = day_num % 7
    day = ", "+str(week[day_num])

  if (end_hr // 12) != 0:
    end_hr = end_hr % 12
    M = " PM"
  else:
    M = " AM"
  if end_hr == 0:
    end_hr = 12
  elif end_hr == 12:
    end_gr = 0
  end_min = str(end_min).zfill(2)
  new_time = ""
  if days == 0:
    new_time = (str(end_hr)+":"+str(end_min)+M+day)
  elif days == 1:
    new_time = (str(end_hr)+":"+str(end_min)+M+day+" (next day)")
  else:
    new_time = (str(end_hr)+":"+str(end_min)+M+day+" ("+str(days)+" days later)")


  return new_time
