#!/usr/bin/python3
import openpyxl

wb = openpyxl.load_workbook('student.xlsx')
ws = wb.active

midterm_num = 3
final_num = 4
homework_num = 5
attendance_num = 6
total_num = 7

midterm_w = 0.3
final_w = 0.35
homework_w = 0.34
attendance_w = 0.01

def total_grade(total):
    if total < 40:
       return "F"
    elif total >= 95:
       return "A+"
    elif total >= 90:
       return "A0"
    elif total >= 85:
       return "B+"
    elif total >= 80:
       return "B0"
    elif total >= 40:
       return "C+"
    else:
       return "C0"

row_index = 2
for row in ws.iter_rows(min_row=2, values_only=True):
    midterm = row[midterm_num]
    final = row[final_num]
    homework = row[homework_num]
    attendance = row[attendance_num]

    total_score = (midterm * midterm_w + final * final_w + homework_w + attendance_w)
    grade = total_grade(total_score)

    ws.cell(row=row_index, column=total_num, value=total_score)
    ws.cell(row=row_index, column=total_num+1, value=grade)
    row_index += 1

wb.save("student_total.xlsx")
wb.close()
