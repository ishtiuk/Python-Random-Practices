# #!/usr/bin/env python3

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# for i in range(len(lst) // 2):
#     lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]

# print(lst)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# for i in range(len(l) // 2):
#     temp = l[i]
#     l[i] = l[-(i + 1)]
#     l[-(i + 1)] = temp

# print(l)

#!/usr/bin/env python3

import requests
import sys

try:
  server_response = requests.get("https://www.google.com")
  if server_response.status_code == 200:
      print("Connection Good")

except:
  print("Connection ERROR!")
  sys.exit(1)
