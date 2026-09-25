# T01 — Experience Shell

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Xây khung giao diện AIOS: menu ngang phía trên, vùng workspace lớn, dashboard mặc định, Work, Catalog tile, AI panel, notifications và account/context area.

## Dependencies

T00

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t01-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- Login shell render được với dữ liệu giả lập
- Top navigation không dùng side menu lớn
- Catalog dạng tile/card
- UI responsive tối thiểu desktop/mobile
