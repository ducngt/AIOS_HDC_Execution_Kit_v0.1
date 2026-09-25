# T02 — Identity, Login, Multi-role Context & Context-bound Authority

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Xây Identity Core, login, role assignment theo thời gian, management-priority default context, role switching và authority evaluation tách khỏi UI visibility.

## Dependencies

T01

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t02-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- Một Identity có nhiều role assignment
- Management role mở dashboard mặc định
- Role switch không cộng dồn authority
- Action permission kiểm tra lại ở backend/control layer
