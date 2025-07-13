from quanlycanbo import CongNhan, NhanVien, KySu, QLCB

def nhap_can_bo():
    loai = input("Loại cán bộ (1: Công nhân, 2: Kỹ sư, 3: Nhân viên): ").strip()
    ho_ten = input("Họ tên: ")
    tuoi = int(input("Tuổi: "))
    gioi_tinh = input("Giới tính (Nam/Nữ/Khác): ")
    dia_chi = input("Địa chỉ: ")

    if loai == "1":
        bac = int(input("Bậc (1-10): "))
        return CongNhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
    elif loai == "2":
        nganh = input("Ngành đào tạo: ")
        return KySu(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
    elif loai == "3":
        cong_viec = input("Công việc: ")
        return NhanVien(ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec)
    else:
        print("Lựa chọn không hợp lệ.")
        return None


def menu():
    qlcb = QLCB()
    while True:
        print("\n----- MENU -----")
        print("1. Thêm mới cán bộ")
        print("2. Tìm kiếm cán bộ theo họ tên")
        print("3. Hiển thị danh sách cán bộ")
        print("4. Xóa cán bộ theo tên (nâng cao)")
        print("5. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == "1":
            cb = nhap_can_bo()
            if cb:
                qlcb.them_can_bo(cb)
                print("Đã thêm cán bộ.")
        elif chon == "2":
            ten = input("Nhập tên cần tìm: ")
            ket_qua = qlcb.tim_kiem_theo_ho_ten(ten)
            if ket_qua:
                for cb in ket_qua:
                    print(cb.hien_thi_thong_tin())
            else:
                print("Không tìm thấy cán bộ.")
        elif chon == "3":
            qlcb.hien_thi_danh_sach()
        elif chon == "4":
            ten = input("Nhập tên cần xóa: ")
            qlcb.xoa_can_bo_theo_ten(ten)
            print(f"Đã xóa cán bộ tên '{ten}'.")
        elif chon == "5":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

menu()
