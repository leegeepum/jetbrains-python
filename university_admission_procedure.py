total_num, accept_num = int(input()), int(input())
total_applicants = [input().split() for _ in range(total_num)]
sorted_applicants = sorted(
    total_applicants, key=lambda x: (-float(x[3]), x[1], x[2]))

print("Successful applicants:")
print("\n".join(" ".join(x for x in accepted[1:3])
                for accepted in sorted_applicants[:accept_num]))
