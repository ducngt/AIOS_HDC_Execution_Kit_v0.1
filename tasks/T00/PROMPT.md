# T00 — Repository Bootstrap & Architecture Guard

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Thiết lập repository theo HDC, protected main, Change Package, CI guard, cấu trúc Core/Domain/Box/Agent và quy tắc không code trực tiếp vào main.

## Dependencies

Không có

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t00-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- hdc CLI chạy được
- Architecture Guard chạy trong CI
- Mẫu Change Package hoạt động
- Không có production data trong repo
