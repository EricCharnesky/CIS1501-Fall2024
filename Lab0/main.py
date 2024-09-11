total_credits_required = int(input("How many total credits are required"))
credits_completed = int(input("How many credits have you completed"))

credits_remaining = total_credits_required - credits_completed
#print("credits_reminaing:", credits_remaining)
credits_per_semester = int(input("How many credits do you take per semester"))

# block 12 is average 635
cost_per_credit = int(input("How much does an average credit cost"))

semesters_left = credits_remaining / credits_per_semester

total_cost = credits_remaining * cost_per_credit

print("You have", semesters_left, "semesters left")
print("Estimated cost of $", total_cost)