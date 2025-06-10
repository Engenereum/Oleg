for i in range(1, 11, 2):
    for j in range(0, 11):
        if i == 9 and j == 10:
            print(f"#\t{i} * {j} = {j * i}\t\t#\t{i + 1} * {j} = {j * (i + 1)}\t#")
            continue
        print(f"#\t{i} * {j} = {j * i}\t\t#\t{i + 1} * {j} = {j * (i + 1)}\t\t#")
    print('+###################+####################')
