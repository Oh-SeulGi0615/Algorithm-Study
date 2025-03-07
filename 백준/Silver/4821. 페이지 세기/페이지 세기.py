while True:
    n = int(input())
    if n == 0:
        break
    page_list = list(input().split(','))

    print_list = []
    for page in page_list:
        if '-' in page:
            start, end = map(int, page.split('-'))

            if start <= end:
                for i in range(start, end+1):
                    if i <= n:
                        print_list.append(i)
        else:
            if int(page) not in print_list and int(page) <= n:
                print_list.append(int(page))
    
    print(len(set(print_list)))