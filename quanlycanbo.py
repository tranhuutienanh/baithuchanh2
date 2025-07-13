from abc import ABC, abstractmethod

class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = str(ho_ten)
        self.tuoi = int(tuoi)
        self.gioi_tinh = str(gioi_tinh)
        self.dia_chi = str(dia_chi)

    def hien_thi_thong_tin(self):
        return f"Tên: {self.ho_ten},\ntuổi: {self.tuoi},\ngiới tính: {self.gioi_tinh},\nđịa chỉ:{self.dia_chi}"
    

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = int(bac)

    def hien_thi_thong_tin(self):
        return super().hien_thi_thong_tin() + f", Bậc: {self.bac}"


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = int(nganh_dao_tao)

    def hien_thi_thong_tin(self):
        return super().hien_thi_thong_tin() + f", Ngành đào tạo: {self.nganh_dao_tao}"


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = int(cong_viec)

    def hien_thi_thong_tin(self):
        return super().hien_thi_thong_tin() + f", Công việc: {self.cong_viec}"
    

class QLCB:
    def __init__(self):
        self.danh_sach_can_bo = []

    def them_can_bo(self, cb):
        if isinstance(cb, CanBo):
            self.danh_sach_can_bo.append(cb)
        else:
            print("Đối tượng không hợp lệ, không phải là cán bộ.")

    def tim_kiem_theo_ho_ten(self, ten):
        if isinstance(ten, CanBo):
            return [cb for cb in self.danh_sach_can_bo if cb.ho_ten.lower() == ten.lower()]
        else:
            print("Không tìm thấy tên")

    def hien_thi_danh_sach(self):
        if not self.danh_sach_can_bo:
            print("Danh sách trống.")
        else:
            for cb in self.danh_sach_can_bo:
                print(cb.hien_thi_thong_tin())
                print("================")

    def xoa_can_bo_theo_ten(self, ten):
        if isinstance(ten, CanBo):
            ban_dau = len(self.danh_sach_can_bo)
            self.danh_sach_can_bo = [cb for cb in self.danh_sach_can_bo if cb.ho_ten.lower() != ten.lower()]
            return ban_dau - len(self.danh_sach_can_bo)













