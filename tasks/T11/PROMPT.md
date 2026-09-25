# T11 — RIS Vertical Slice

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Triển khai RIS theo vertical slice bắt đầu Research Project, đi xuyên Data->Work->AI->Approval->Evidence->Dashboard; sau đó mở rộng publication/IP/discovery theo cùng pattern.

## Dependencies

T10

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t11-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- Research Project chạy end-to-end
- PI/manager dashboards khác nhau
- Có evidence/provenance
- RIS không truy cập trực tiếp DB domain khác
