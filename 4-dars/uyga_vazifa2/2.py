subject_scores = { 
    'Math':  {101: 90, 102: 85, 104: 92},
    'Science': {101: 88, 103: 75, 104: 80},
    'English': {102: 78, 103: 82, 104: 85}
}
count = 0
print()
for key,value in subject_scores['Math'].items():
    count += value
  
# print(count//3)
print(f"Math {count//3}")
count = 0
for key,value in subject_scores['Science'].items():
    count += value
  
# print(count//3)
print(f"Science {count//3}")
count = 0
for key,value in subject_scores['English'].items():
    count += value
  
# print(count//3)
print(f"English {count//3}")
