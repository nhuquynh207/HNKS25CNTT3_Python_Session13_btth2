saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice_input = input("Nhập lựa chọn: ").strip()

    if not choice_input.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
        continue

    choice = int(choice_input)

    match choice:

        case 1:
            if not saving_accounts:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\nDanh sách sổ tiết kiệm:")
                for index, account in enumerate(saving_accounts, start=1):
                    print(
                        f"{index}. Mã sổ: {account['account_id']} | "
                        f"Khách hàng: {account['customer_name']} | "
                        f"Số tiền gửi: {account['balance']} | "
                        f"Kỳ hạn: {account['term_months']} tháng | "
                        f"Lãi suất: {account['interest_rate']}%/năm | "
                        f"Trạng thái: {account['status']}"
                    )

        case 2:
            account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()

            found = False
            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = True
                    break

            if found:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue

            customer_name = input("Nhập tên khách hàng: ").strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            balance_input = input("Nhập số tiền gửi: ").strip()
            term_input = input("Nhập kỳ hạn gửi theo tháng: ").strip()

            if (
                not balance_input.isdigit()
                or not term_input.isdigit()
                or int(balance_input) <= 0
                or int(term_input) <= 0
            ):
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            interest_rate_input = input("Nhập lãi suất năm: ").strip()

            if (
                interest_rate_input.count(".") > 1
                or interest_rate_input.replace(".", "", 1).isdigit() == False
                or float(interest_rate_input) <= 0
            ):
                print("Lãi suất không hợp lệ!")
                continue

            saving_accounts.append(
                {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": int(balance_input),
                    "term_months": int(term_input),
                    "interest_rate": float(interest_rate_input),
                    "status": "active"
                }
            )

            print("Mở sổ tiết kiệm thành công!")

        case 3:
            account_id = input(
                "Nhập mã sổ tiết kiệm cần cập nhật: "
            ).strip().upper()

            target_account = None

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    target_account = account
                    break

            if target_account is None:
                print("Không tìm thấy mã sổ tiết kiệm!")
                continue

            if target_account["status"] == "closed":
                print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                continue

            customer_name = input(
                "Nhập tên khách hàng mới: "
            ).strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            balance_input = input("Nhập số tiền gửi mới: ").strip()
            term_input = input("Nhập kỳ hạn mới theo tháng: ").strip()

            if (
                not balance_input.isdigit()
                or not term_input.isdigit()
                or int(balance_input) <= 0
                or int(term_input) <= 0
            ):
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            interest_rate_input = input(
                "Nhập lãi suất năm mới: "
            ).strip()

            if (
                interest_rate_input.count(".") > 1
                or interest_rate_input.replace(".", "", 1).isdigit() == False
                or float(interest_rate_input) <= 0
            ):
                print("Lãi suất không hợp lệ!")
                continue

            target_account["customer_name"] = customer_name
            target_account["balance"] = int(balance_input)
            target_account["term_months"] = int(term_input)
            target_account["interest_rate"] = float(interest_rate_input)

            print("Cập nhật thông tin thành công!")

        case 4:
            account_id = input(
                "Nhập mã sổ tiết kiệm cần tất toán/xóa: "
            ).strip().upper()

            target_account = None

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    target_account = account
                    break

            if target_account is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            target_account["status"] = "closed"
            print("Tất toán sổ tiết kiệm thành công!")

        case 5:
            account_id = input(
                "Nhập mã sổ tiết kiệm cần tính lãi: "
            ).strip().upper()

            target_account = None

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    target_account = account
                    break

            if target_account is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if target_account["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue

            interest = (
                target_account["balance"]
                * target_account["interest_rate"]
                / 100
                * target_account["term_months"]
                / 12
            )

            total = target_account["balance"] + interest

            print(f"Tiền lãi dự kiến: {interest:,.0f}")
            print(f"Tổng tiền nhận khi đến hạn: {total:,.0f}")

        case 6:
            account_id = input(
                "Nhập mã sổ tiết kiệm cần kiểm tra: "
            ).strip().upper()

            target_account = None

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    target_account = account
                    break

            if target_account is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if target_account["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue

            actual_months_input = input(
                "Nhập số tháng thực gửi: "
            ).strip()

            if (
                not actual_months_input.isdigit()
                or int(actual_months_input) <= 0
            ):
                print("Số tháng thực gửi không hợp lệ!")
                continue

            actual_months = int(actual_months_input)

            if actual_months < target_account["term_months"]:
                applied_rate = 0.5
                print("Khách hàng rút trước hạn.")
            else:
                applied_rate = target_account["interest_rate"]
                print("Khách hàng đủ điều kiện hưởng lãi đúng hạn.")

            interest = (
                target_account["balance"]
                * applied_rate
                / 100
                * actual_months
                / 12
            )

            total = target_account["balance"] + interest

            print(f"Tiền lãi thực nhận: {interest:,.0f}")
            print(f"Tổng tiền thực nhận: {total:,.0f}")

        case 7:
            print("Đã thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")