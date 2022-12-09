gpa_grades=['A','B','C']
gpa_points=['4.0', '3.5', '3.0']

my_dict={}

while len(gpa_grades) > 0:
 for gpa,gpa_pt in my_dict.items():
  for i in gpa_grades:
    gpa = gpa_grades[i]
    gpa_pt = gpa_points[i]
    my_dict.update(gpa,gpa_pt)

print(my_dict)