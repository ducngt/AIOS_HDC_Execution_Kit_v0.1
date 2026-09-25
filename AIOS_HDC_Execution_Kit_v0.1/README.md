# AIOS HDC Execution Kit v0.1

Bộ mã điều phối **Huma Don't Code (HDC)** để AI trực tiếp thực hiện software engineering cho AIOS dưới sự kiểm duyệt của Human.

## Mục tiêu

- Human cung cấp Intent, Meaning, Authority và Acceptance.
- AI đọc repository, thiết kế capability/contract, viết code, build, test, debug, migration, tài liệu hóa và chuẩn bị Acceptance Package.
- Mọi thay đổi đi qua Change Package, Architecture Guard và Human Gate.
- AIOS được phát triển tăng trưởng từng bước nhưng không phá Core, không tạo silo, không trùng capability và không bypass authority/data contracts.

## Bắt đầu

```bash
python hdc/hdc.py status
python hdc/hdc.py next
python hdc/hdc.py prompt T00
```

AI nên đọc `HDC_MASTER_PROMPT.md` trước khi thực hiện bất kỳ task nào.
Human dùng `HUMA_RUNBOOK.md` để kiểm duyệt mà không cần đọc code.

## Trình tự chuẩn

Xem `docs/SEQUENCE.md` và thư mục `tasks/`.

## Các nguyên tắc bắt buộc

Xem `docs/INVARIANTS.md`.
