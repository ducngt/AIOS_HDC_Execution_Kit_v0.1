# Cài HDC Execution Kit vào repository AIOS

## Dành cho AI Engineering Executor

1. Đọc `HDC_MASTER_PROMPT.md` và `docs/INVARIANTS.md`.
2. Khám phá repository đích trước khi copy/merge bất kỳ file nào.
3. Nếu repo đã có cấu trúc tương đương, merge theo capability/contract; không ghi đè mù.
4. Đưa các thư mục `hdc/`, `tasks/`, `schemas/`, `templates/`, `docs/` và `.github/` vào root repository.
5. Không đưa `state.json` cũ từ dự án khác vào repo đang chạy; khởi tạo state cho repo đó.
6. Chạy:

```bash
python hdc/hdc.py status
python hdc/hdc.py next
python hdc/hdc.py prompt T00
```

7. Thực hiện T00 trước mọi task khác.

## Quyền GitHub cho AI

Dùng AI engineering identity riêng, cấp quyền tối thiểu cần thiết để đọc repository, tạo branch, commit/push branch, mở/cập nhật pull request, đọc CI và chạy workflow được phép. Không cấp mặc định quyền xóa repository, thay branch protection, force-push main hoặc truy cập repository không liên quan.

Secrets phải ở secret store/GitHub secrets/environment secrets, không commit vào repository hoặc prompt.
