# T14 — Cross-Domain Assembly & Institutional Intelligence

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Lắp ráp quy trình xuyên domain, executive/leadership dashboards, institutional intelligence, benchmark/forecast/simulation với Human decision authority.

## Dependencies

T13

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t14-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- Dashboard không query DB domain trực tiếp
- Cross-domain work có connection plan
- AI recommendation không thành decision tự động
- Leadership scope theo authority/portfolio
