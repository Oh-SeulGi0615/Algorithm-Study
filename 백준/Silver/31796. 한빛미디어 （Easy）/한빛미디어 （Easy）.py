n = int(input())
arr = list(map(int, input().split()))
arr.sort()

pages = []
page = []

for p in arr:
  if not page:
    page.append(p)
  elif p < page[0] * 2:
    page.append(p)
  elif p >= page[0] * 2:
    pages.append(page)
    page = [p]

if page:
  pages.append(page)

print(len(pages))