%load KB
:- [truongDaiHoc].

:- writeln('Cau 1: PTN Tri tue nhan tao thuoc khoa CNTT phai khong?').
:- writeln('Cau 2: Khoa Toan hoc thanh lap nam 2000 phai khong?').
:- writeln('Cau 3: Khoa Vat ly co cac bo mon nao?').
:- writeln('Cau 4: PTN Ky thuat hat nhan thanh lap nam nao?').
:- writeln('Cau 5: Giao vien Tran Thai Son thuoc phong ban nao?').
:- writeln('Cau 6: Giao vien Le Hoai Bac thuoc bo mon Khoa hoc may tinh phai khong?').
:- writeln('Cau 7: Giao vien Tran Minh Triet la truong PTN Cong nghe phan mem phai khong?').
:- writeln('Cau 8: Luong cua giao vien Dinh Ba Tien la bao nhieu?').
:- writeln('Cau 9: Luong cua giao vien Tran Vu lon hon cua giao vien Tran Trung Dung phai khong?').
:- writeln('Cau 10: Que cua giao vien Ly Quoc Ngoc o dau?').
:- writeln('Cau 11: Giao vien cung que voi giao vien Nguyen Chi Nhan?').
:- writeln('Cau 12: Giao vien Trinh Thanh Deo nam nay bao nhieu tuoi?').
:- writeln('Cau 13: Giao vien Nguyen Thi Thanh Mai thuoc bo mon nao?').
:- writeln('Cau 14: Giao vien cung tuoi voi giao vien Truong Thi Hong Loan?').
:- writeln('Cau 15: Ai la truong khoa Vat ly?').
:- writeln('Cau 16: Giao vien Le Vu Tuan Hung chung khoa voi giao vien Nguyen Chi Nhan phai khong?').
:- writeln('Cau 17: Giao vien Vu Hai Quan la Tien si phai khong?').
:- writeln('Cau 18: Liet ke danh sach thac si.').
:- writeln('Cau 19: Liet ke danh sach giao su.').
:- writeln('Cau 20: Liet ke danh sach giao vien thuoc khoa CNTT.').
:- writeln(' ').
:- writeln('Press cau_1, cau_2, cau_3,..., cau_20 to see question and answer.').




cau_1 :- 
	writeln('PTN Tri tue nhan tao thuoc khoa CNTT phai khong?'),
	phong_thi_nghiem_thuoc_khoa('Tri tue nhan tao', 'CNTT') -> writeln('Phai'); writeln('Khong phai').

cau_2 :- 
	writeln('Khoa Toan hoc thanh lap nam 2000 phai khong?'),
	nam_thanh_lap('Toan hoc', 2000) -> writeln('Phai'); writeln('Khong phai').

cau_3 :- 
	writeln('Khoa Vat ly co cac bo mon nao?'),		
	setof(BM, bo_mon_thuoc_khoa(BM, 'Vat ly'), List),
	writeln(List).

cau_4 :-
	writeln('PTN Ky thuat hat nhan thanh lap nam nao?'),
	nam_thanh_lap('Ky thuat hat nhan', Nam) -> writeln(Nam); writeln('Khong biet').

cau_5 :-
	writeln('Giao vien Tran Thai Son thuoc phong ban nao?'),
	giao_vien_thuoc_phong_ban('Tran Thai Son', PB) -> writeln(PB); writeln('Khong biet').

cau_6 :-
	writeln('Giao vien Le Hoai Bac thuoc bo mon Khoa hoc may tinh phai khong?'),
	giao_vien_thuoc_bo_mon('Le Hoai Bac', 'Khoa hoc may tinh') -> writeln('Phai'); writeln('Khong phai').

cau_7 :-
	writeln('Giao vien Tran Minh Triet la truong PTN Cong nghe phan mem phai khong?'),
	truong_phong_thi_nghiem('Tran Minh Triet', 'Cong nghe phan mem') -> writeln('Phai'); writeln('Khong phai').

cau_8 :-
	writeln('Luong cua giao vien Dinh Ba Tien la bao nhieu?'),
	luong('Dinh Ba Tien', Luong) -> writeln(Luong); writeln('Khong biet').

cau_9 :-
	writeln('Luong cua giao vien Tran Vu lon hon cua giao vien Tran Trung Dung phai khong?'),
	luong_cao_hon('Tran Vu', 'Tran Trung Dung') -> writeln('Phai'); writeln('Khong phai').

cau_10 :-
	writeln('Que cua giao vien Ly Quoc Ngoc o dau?'),
	que_quan('Ly Quoc Ngoc', QQ) -> writeln(QQ); writeln('Khong biet').

cau_11 :-
	writeln('Giao vien cung que voi giao vien Nguyen Chi Nhan?'),
	setof(GV, cung_que_quan(GV, 'Nguyen Chi Nhan'), List),
	writeln(List).

cau_12 :-
	writeln('Giao vien Trinh Thanh Deo nam nay bao nhieu tuoi?'),
	tuoi('Trinh Thanh Deo', Tuoi) -> writeln(Tuoi); writeln('Khong biet').

cau_13 :-
	writeln('Giao vien Nguyen Thi Thanh Mai thuoc bo mon nao?'),
	giao_vien_thuoc_bo_mon('Nguyen Thi Thanh Mai', BM) -> writeln(BM); writeln('Khong biet').

cau_14 :-
	writeln('Giao vien cung tuoi voi giao vien Truong Thi Hong Loan?'),
	setof(GV, bang_tuoi(GV, 'Truong Thi Hong Loan'), List),
	writeln(List).

cau_15 :-
	writeln('Ai la truong khoa Vat ly?'),
	truong_phong_thi_nghiem(TPTN, 'Ky thuat hat nhan') -> writeln(TPTN); writeln('Khong biet').

cau_16 :-
	writeln('Giao vien Le Vu Tuan Hung chung khoa voi giao vien Nguyen Chi Nhan phai khong?'),
	giao_vien_cung_khoa('Le Vu Tuan Hung', 'Nguyen Chi Nhan') -> writeln('Phai'); writeln('Khong phai').

cau_17 :-
	writeln('Giao vien Vu Hai Quan la Tien si phai khong?'),
	tien_si('Vu Hai Quan') -> writeln('Phai'); writeln('Khong phai').

cau_18 :-
	writeln('Liet ke danh sach thac si.'),
	setof(ThS, thac_si(ThS), List),
	writeln(List).

cau_19 :-
	writeln('Liet ke danh sach giao su.'),
	setof(GS, giao_su(GS), List),
	writeln(List).

cau_20 :-
	writeln('Liet ke danh sach giao vien thuoc khoa CNTT.'),
	setof(GV, giao_vien_thuoc_khoa(GV, 'CNTT'), List),
	writeln(List).
