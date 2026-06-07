student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

def display_grades(records):

    if (len(records) == 0):
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("--- BẢNG ĐIỂM SINH VIÊN ---")
    for index,student in enumerate(records, start=1):
        average = ( student.get('math') + student.get('physics') + student.get('chemistry') ) / 3

        if (average >= 8.0):
            rank = "Giỏi"
        elif (average >= 6.5):
            rank = "Khá"
        elif (average >= 5.0):
            rank = "Trung bình"
        else:
            rank = "Yếu (Cảnh báo đỏ)"
        
        print(f"{index}. [{student.get('student_id')}] {student.get('name'):<13} | Toán: {student.get('math')} | Lý: {student.get('physics')} | Hóa: {student.get('chemistry')} | ĐTB: {average:.2f} - {rank}")

    print("---------------------------")

def update_student_score(records):
    found = False

    while True:
        student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()

        if (student_id != ""):
            break
    
        print("Mã sinh viên không được để trống!!\n")

    for student in records:
        if (student.get('student_id') == student_id):
            found = True

            while True:
                subject = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ").strip()

                if (subject == ""):
                    print("Môn học không được để trống!!\n")
                    continue

                if (not subject.isdigit()):
                    print("Chọn môn học chỉ được nhập số\n")
                    continue

                subject = int(subject)

                if (subject in (1, 2, 3) ):
                    break

                print("Lựa chọn không hợp lý!!\n")

            while True:
                new_score = input("Nhập điểm mới: ").strip()

                if (new_score == ""):
                    print("Điểm không được để trống!!\n")
                    continue

                if not new_score.replace(".", "", 1).isdigit():
                    print("Điểm phải là số!!\n")
                    continue

                new_score = float(new_score)

                if not (0 <= new_score <= 10):
                    print("Điểm phải từ 0 đến 10!!")
                    continue

                break

            if subject == 1:
                student["math"] = new_score
                subject_name = "Toán"
            elif subject == 2:
                student["physics"] = new_score
                subject_name = "Lý"
            else:
                student["chemistry"] = new_score
                subject_name = "Hóa"

            print(f">> Đã cập nhật điểm {subject_name} của sinh viên '{student.get('name')}' thành {new_score}.")

            break

    if (not found):
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!\n")

def generate_report(records):
    if (len(records) == 0):
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    
    total = len(records)
    pass_count = 0
    fail_count = 0

    for student in records:
        average = ( student.get('math') + student.get('physics') + student.get('chemistry') ) / 3

        if (average >= 5):
            pass_count += 1
        else:
            fail_count += 1

    pass_percent = (pass_count / total) * 100
    fail_parcent = (fail_count / total) * 100

    print("--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {pass_count} sinh viên (Chiếm {pass_percent:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {fail_count} sinh viên (Chiếm {fail_parcent:.2f}%)")
    print("----------------------")

def find_valedictorian(records):
    if (len(records) == 0):
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    
    top_student = records[0]
    top_average = (top_student.get('math') + top_student.get('physics') + top_student.get('chemistry')) / 3

    for student in records:
        average = ( student.get('math') + student.get('physics') + student.get('chemistry') ) / 3

        if average > top_average:
            top_average = average
            top_student = student

    print("--- VINH DANH THỦ KHOA ---")
    print(f" Sinh viên: {top_student.get('name')} (Mã: {top_student.get('student_id')})")
    print(f" Điểm Trung Bình: {top_average:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")

def menu():
    print("===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("=======================================================")

while True:
    menu()

    choice = input("Chọn chức năng (1-5): ")

    match choice:
        case "1":
            display_grades(student_records)
        case "2":
            update_student_score(student_records)
        case "3":
            generate_report(student_records)
        case "4":
            find_valedictorian(student_records)
        case "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        case _:
            print("Lỗi: Lựa chọn của bạn không hợp lệ!!\n")