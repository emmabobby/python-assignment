pass_mark = 45
pass_count = 0
fail_count = 0

for i in range(1, 16):
    score = int(input(f"Enter the score for student {i}: "))
    if score >= pass_mark:
        pass_count += 1
    else:
        fail_count += 1

print("Pass :", pass_count)
print("Fail :", fail_count)