# T15 — Hardening, Release, Storage Redundancy & Continuous Evolution

## HDC Instruction

Đọc `HDC_MASTER_PROMPT.md`, `docs/INVARIANTS.md`, trạng thái repository và task manifest này trước khi hành động.

## Goal

Hoàn thiện architecture audit, security/privacy, backup/restore, server primary storage + secondary cloud/iCloud adapter theo policy, release/rollback, evolution workflow và acceptance baseline.

## Dependencies

T14

## Quy trình bắt buộc

1. Discover repository, registries, capabilities, contracts và tests hiện có.
2. Trình Human Understanding Package: Intent, reuse/new capability, contract, data/semantic/authority/UI impact, acceptance criteria.
3. Chỉ sau G1/G2 mới tạo branch `change/t15-<slug>` và Change Package.
4. AI tự implementation, build, test, debug, migration và documentation.
5. Chạy Architecture Guard và các test liên quan.
6. Chuẩn bị preview và Acceptance Package.
7. Chờ Human ACCEPT/RETURN/REJECT. Không coi code chạy được là acceptance.

## Acceptance criteria

- Primary operational store tách GitHub
- Secondary storage adapter có contract
- Rollback được kiểm thử
- Architecture/security gates pass
- Main phản ánh accepted state
