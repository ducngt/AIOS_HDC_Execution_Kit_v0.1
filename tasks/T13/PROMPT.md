# T13 — Remaining Domain Intelligence Systems

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Triển khai TIS, SIS, PIS, FIS, OIS, EIS, QIS, DIS bằng Domain Factory; ưu tiên vertical slice nhỏ cho từng domain và tái sử dụng shared capabilities.

## Dependencies

T11, T12

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t13-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- Mỗi domain có manifest
- Không domain silo core entities
- Mỗi domain có ít nhất một end-to-end slice
- Cross-domain contracts versioned
