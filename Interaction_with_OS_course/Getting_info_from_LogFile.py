import re
def show_time_of_pid(line):
  pattern = r"^(\w+ [1-9]+ [0-9]{2}:[0-9]{2}:[0-9]{2}).*([0-9]{5})"
  result = re.search(pattern, line)
  return result[1] + " pid:" + result[2]

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187